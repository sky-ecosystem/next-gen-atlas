---
id: e96da090-34ff-4445-a1d3-22cc69be2e51
docNo: A.3.2.2.1.1.1.1.4
name: Reference Implementation
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.3.2.2.1.1.1.1.4 - Reference Implementation [Core]

A reference implementation of the calculation of Instance Financial RRC for lending markets is included herein.

`import math
from collections import defaultdict
import numpy as np
from scipy.stats import norm

# Constants
RISK_FREE_RATE = 0.04  # SOFR
TIME_HORIZON = 1       # 1 year

class FinancialRRCModel:
    def __init__(self):
        # For demo purposes, we hardcode a dummy correlation map
        self.token_correlation_map = {
            'TOKENA': {'TOKENB': 0.5},
            'TOKENB': {'TOKENA': 0.5},
        }

    def _calculate_effective_volatility(self, list_1, list_2):
        """
        Calculate the effective variance between two sets of positions.
        """
        effective_variance = 0.0
        for sym1, pos1 in list_1.items():
            for sym2, pos2 in list_2.items():
                if sym1 == sym2:
                    corr = 1.0
                else:
                    corr = self.token_correlation_map.get(sym1, {}).get(sym2,
                           self.token_correlation_map.get(sym2, {}).get(sym1, 0.0))
                effective_variance += (
                    pos1["share"]
                    * pos2["share"]
                    * pos1["volatility_30d"]
                    * pos2["volatility_30d"]
                    * corr
                )
        return effective_variance

    def _estimate_rrc_for_position(self, wallet_data):
        """
        Estimate the required-risk capital (RRC) for a given wallet_data dict.
        """
        # 1) compute effective volatilities
        var_coll = self._calculate_effective_volatility(
            wallet_data["collateral_positions"],
            wallet_data["collateral_positions"],
        )
        var_debt = self._calculate_effective_volatility(
            wallet_data["debt_positions"],
            wallet_data["debt_positions"],
        )
        vol_coll = math.sqrt(var_coll)
        vol_debt = math.sqrt(var_debt)

        # 2) correlation collateral↔debt
        cov_cd = self._calculate_effective_volatility(
            wallet_data["collateral_positions"],
            wallet_data["debt_positions"],
        )
        corr_cd = cov_cd / (vol_coll * vol_debt) if vol_coll * vol_debt > 0 else 0.0

        # 3) drift terms
        eff_coll_rate = sum(p["share"] * p["supply_apy_30d"]
                            for p in wallet_data["collateral_positions"].values())
        eff_borrow_rate = sum(p["share"] * p["borrow_apy_30d"]
                              for p in wallet_data["debt_positions"].values())
        eff_stake_rate = sum(p["share"] * p["staking_apy_30d"]
                             for p in wallet_data["collateral_positions"].values())

        drift_cd = (
            eff_coll_rate + eff_stake_rate - eff_borrow_rate
            + (var_debt - var_coll) / 2
        )

        vol_cd = math.sqrt(
            max(var_coll + var_debt - 2 * corr_cd * vol_coll * vol_debt, 0)
        )

        # 4) Black-Cox inputs
        a = (drift_cd - vol_cd**2 / 2) / (vol_cd**2) if vol_cd > 0 else 0.0
        L = wallet_data["collateral_usd_lt"]
        D = wallet_data["debt_usd"]
        log_term = math.log(L / D) if L > 0 and D > 0 else float("-inf")
        denom = vol_cd * math.sqrt(TIME_HORIZON) if vol_cd > 0 else 1e-10

        d1 = (log_term + (drift_cd - vol_cd**2/2) * TIME_HORIZON) / denom
        d2 = (log_term - (drift_cd - vol_cd**2/2) * TIME_HORIZON) / denom

        # 5) Probability of Default
        try:
            pd = (
                norm.cdf(-d1)
                + norm.cdf(-d2) * (L / D) ** (-2 * a)
            )
        except OverflowError:
            pd = 1.0
        pd = max(0.0, min(pd, 1.0))

        # 6) Loss Given Default
        recovery = sum(
            p["share"] * (1 - p["liquidation_penalty"]) * (1 - p["slippage"])
            / p["liquidation_threshold"]
            for p in wallet_data["collateral_positions"].values()
        )
        lgd = max(0.0, min(1 - recovery, 1.0))

        # 7) Exposure at Default
        ead = sum(
            debt["debt_usd"] * math.exp((RISK_FREE_RATE + debt["borrow_apy_30d"]) * TIME_HORIZON)
            for debt in wallet_data["debt_positions"].values()
        )

        # 8) Asset Correlation Coefficient
        a_acc, b_acc, c_acc = 0.13, 10, 0.33
        exp_term = math.exp(-b_acc * pd)
        acc = a_acc * (1 - exp_term)/(1-math.exp(-b_acc)) + c_acc*(1 - (1-exp_term)/(1-math.exp(-b_acc)))

        # 9) Credit risk weight
        default_threshold = (
            norm.ppf(max(pd, 1e-10)) + math.sqrt(acc) * norm.ppf(0.999)
        ) / math.sqrt(1 - acc)
        credit_risk = max(lgd * norm.cdf(default_threshold) - lgd * pd, 0)

        # 10) RRC
        rrc = credit_risk * ead
        return rrc

# -------- DEMO USAGE --------

if __name__ == "__main__":
    # 1) Build a dummy wallet_data structure
    wallet_data = {
        "collateral_positions": {
            "TOKENA": {
                "share": 0.6,
                "volatility_30d": 0.2,
                "supply_apy_30d": 0.05,
                "staking_apy_30d": 0.02,
                "liquidation_penalty": 0.1,
                "liquidation_threshold": 0.8,
                "slippage": 0.01,
            },
            "TOKENB": {
                "share": 0.4,
                "volatility_30d": 0.25,
                "supply_apy_30d": 0.04,
                "staking_apy_30d": 0.015,
                "liquidation_penalty": 0.12,
                "liquidation_threshold": 0.85,
                "slippage": 0.015,
            },
        },
        "debt_positions": {
            "TOKENA": {
                "share": 0.7,
                "volatility_30d": 0.2,
                "borrow_apy_30d": 0.06,
                "debt_usd":  100_000,
            },
            "TOKENB": {
                "share": 0.3,
                "volatility_30d": 0.25,
                "borrow_apy_30d": 0.07,
                "debt_usd":  50_000,
            },
        },
        "collateral_usd_lt": 200_000,
        "debt_usd": 150_000,
    }

    # 2) Instantiate and run
    model = FinancialRRCModel()
    rrc = model._estimate_rrc_for_position(wallet_data)
    print(f"Estimated Required Risk Capital (RRC): ${rrc:,.2f}")
`
