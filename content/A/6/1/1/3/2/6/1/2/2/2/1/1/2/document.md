---
id: 2b42015c-c76a-4364-b8b5-c9a2b9f6f484
docNo: A.6.1.1.3.2.6.1.2.2.2.1.1.2
name: Relayer Role
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.2.1.1.2 - Relayer Role [Core]

The Relayer role is the address(es) for the Keel Liquidity Layer ALM Planner off-chain system that calls functions on `SvmAlmController` program to perform actions on funds held by Keel's Solana Controller. The Relayer Role has `can_execute_swap` and `can_reallocate` permissions. The Relayer Role may be granted to an address by any address with `can_manage_permissions` privileges and can be revoked by one with `can_suspend_permissions` privileges.
