---
id: 35ec7382-0613-4e74-b5ba-d86c647b1d73
docNo: A.3.2.2.1.2.3.4
name: Reference Implementation
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.3.2.2.1.2.3.4 - Reference Implementation [Core]

The document herein contains a reference implementation of the calculation of Instance Smart Contract RRC based on the Smart Contract Risk Rating.

`import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# Function Definition
# ------------------------------------------------------------------

def piecewise_coverage(x, x_start, x_kink, x_max):
    """
    Returns a coverage fraction in [0.0 ... 1.0] given x
    and piecewise linear thresholds:
      - 0% coverage if x < x_start
      - linear 0%→25% from x_start to x_kink
      - linear 25%→100% from x_kink to x_max
      - 100% if x > x_max
    """
    # Safely handle edge cases
    if x <= x_start:
        return 0.0
    if x >= x_max:
        return 1.0

    # If between x_start and x_kink -> map linearly from 0% to 25%
    if x_start < x <= x_kink:
        span = x_kink - x_start
        # fraction of the way through that segment
        frac = (x - x_start) / span
        # coverage goes 0 -> 0.25 (25%)
        return 0.25 * frac

    # If between x_kink and x_max -> map linearly from 25% to 100%
    else:  # x_kink < x < x_max
        span = x_max - x_kink
        frac = (x - x_kink) / span
        # coverage goes 0.25 -> 1.0
        return 0.25 + (0.75 * frac)

# ------------------------------------------------------------------
# Thresholds
# ------------------------------------------------------------------

def f1_thresholds_low_risk(rating):
    """
    Return (x_start, x_kink, x_max)
    in % terms, e.g. 5%, 23.75%, 30%, etc.
    """
    x_start = (50 - rating) * 0.01  # e.g. rating=0 -> 0.5 (50%)
    x_max   = x_start + 0.50       # always a 50% gap to max
    # kink is 75% of the way from start to max
    x_kink  = x_start + 0.75 * (x_max - x_start)
    return (x_start, x_kink, x_max)

def f2_thresholds_high_risk(rating):
    """
    Return (x_start, x_kink, x_max)
    in fraction form (0.50, 0.875, 1.00, etc).
    """
    # starting threshold = (75 - rating) * 2%:
    x_start = (75 - rating) * 0.02
    x_max = x_start + 0.50
    x_kink = x_start + 0.75 * (x_max - x_start)  # 75% of the way
    return (x_start, x_kink, x_max)

# ------------------------------------------------------------------
# RRC Calculation
# ------------------------------------------------------------------

def calculate_rrc_coverage(
    rating,
    exposure_internal,
    exposure_total,
    liquid_surplus_internal,
    total_exposure_beyond_surplus,
    total_collateral
):
    """
    Returns the coverage fraction (0 - 1) for a given rating & scenario.
    For the absolute coverage amount, multiply coverage_fraction
    by \`exposure_internal\`.
    """

    # 1) Compute the two driver ratios
    f1 = max(0.0, total_exposure_beyond_surplus / total_collateral) # Ensuring it is non-negative when surplus > exposure
    f2 = (exposure_internal + 0.1 * (exposure_total - exposure_internal)) / liquid_surplus_internal

    # 2) Determine which category the rating is in
    if rating <= 25:
        # TRR Category 1 (Low Risk)  => use only f1 piecewise
        x_start, x_kink, x_max = f1_thresholds_low_risk(rating)
        coverage_fraction = piecewise_coverage(f1, x_start, x_kink, x_max)

    elif rating <= 50:
        # TRR Category 2 (Medium Risk) => blend coverage from f1-curve and f2-curve
        # First get coverage from the "f1 low-risk"
        x_start_1, x_kink_1, x_max_1 = f1_thresholds_low_risk(25)
        cov_f1 = piecewise_coverage(f1, x_start_1, x_kink_1, x_max_1)

        # Then get coverage from the "f2 high-risk"
        x_start_2, x_kink_2, x_max_2 = f2_thresholds_high_risk(50)
        cov_f2 = piecewise_coverage(f2, x_start_2, x_kink_2, x_max_2)

        # Blend factor alpha
        alpha = (rating - 25) / (50 - 25)
        coverage_fraction = (1 - alpha) * cov_f1 + 0.15 * alpha * cov_f2

    elif rating <= 75:
        # TRR Category 3 (High Risk) => use only f2
        x_start, x_kink, x_max = f2_thresholds_high_risk(rating)
        coverage_fraction = piecewise_coverage(f2, x_start, x_kink, x_max)

    else:
        # TRR Category 4 (Extreme Risk) => special piecewise lumps.
        if rating > 75:
            return 1.0

    return coverage_fraction
`
