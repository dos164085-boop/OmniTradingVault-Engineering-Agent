# DEC-01

## Decision

Do not modify production Solidity contracts.

Treat the compilation failure as an engineering environment incident until sufficient evidence demonstrates otherwise.

## Rationale

Hardhat compiled successfully while Forge failed.

This inconsistency indicated that the problem was more likely related to the development toolchain than to the protocol implementation.

## Result

The protocol source code remained unchanged.

The investigation shifted toward validating the engineering environment.
