# Pattern: Stack Too Deep Resolution

The "Stack too deep" error occurs when a Solidity function uses too many local variables or parameters, exceeding the EVM stack limit.

## Resolution Strategies

1. Reduce the number of local variables.
2. Split large functions into smaller functions.
3. Group related variables into structs.
4. Use `unchecked` blocks when appropriate.
5. Consider enabling `viaIR` only after validating that the issue is architectural rather than environmental.

## Prevention

- Keep functions focused on a single responsibility.
- Prefer fewer than 8–10 local variables.
- Prefer fewer than 6–8 function parameters.
- Review function complexity during code review.

## Related Cases

- ENG-0001 — Stack Too Deep in VaultCore
- Foundry / Hardhat toolchain stabilization

## References

- Solidity Compiler
- Foundry
- Hardhat
