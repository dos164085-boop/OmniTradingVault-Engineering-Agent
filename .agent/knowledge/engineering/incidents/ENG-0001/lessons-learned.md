# Lessons Learned

## Root Cause

The production Solidity contracts were not responsible for the failure.

The actual root cause was a mismatch between the local development toolchain
and the compilation environment.

## Engineering Lesson

Do not modify production contracts before isolating and validating the build
environment.

Always compare compiler behavior across toolchains before proposing protocol
changes.

## Preventive Actions

- Verify toolchain versions.
- Compare Foundry and Hardhat outputs.
- Record evidence before implementing fixes.
- Convert validated incidents into reusable engineering knowledge.
