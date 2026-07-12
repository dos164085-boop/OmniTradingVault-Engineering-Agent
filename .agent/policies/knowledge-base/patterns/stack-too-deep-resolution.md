# Pattern: Stack Too Deep Resolution

El error 'Stack too deep' ocurre cuando hay demasiadas variables locales en una función Solidity.

## Estrategias para resolverlo:
1. Reducir el número de variables locales
2. Dividir la función en funciones más pequeñas
3. Usar structs para agrupar variables
4. Usar unchecked blocks

## Prevención:
- Máximo 8-10 variables por función
- Máximo 6-8 parámetros por función
- Funciones pequeñas y enfocadas

## Casos relacionados:
- ENG-0001: Stack too deep en VaultCore
