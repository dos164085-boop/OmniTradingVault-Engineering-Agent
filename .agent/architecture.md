# Arquitectura de Referencia

## Visión Arquitectónica

OmniTradingVault es un protocolo DeFi que opera en múltiples blockchains. Su arquitectura debe ser:

- **Segura**: Priorizando la seguridad sobre la eficiencia
- **Modular**: Permitir actualizaciones y extensiones
- **Transparente**: Operaciones verificables on-chain
- **Eficiente**: Gas optimizado sin sacrificar seguridad

## Patrones Arquitectónicos

### 1. Proxy Pattern (UUPS)

**Uso:** Actualizaciones de contratos sin migrar estado

**Razón:** Permite correcciones de seguridad y mejoras sin interrumpir el servicio

**Implementación:** OpenZeppelin UUPSUpgradeable

### 2. Diamond Pattern (EIP-2535)

**Uso:** Gestión de funcionalidades modulares

**Razón:** Permite añadir/remover funciones sin límite de tamaño de contrato

### 3. Access Control

**Uso:** Roles y permisos granular

**Razón:** Principio de mínimo privilegio

**Implementación:** OpenZeppelin AccessControl con roles específicos

### 4. Emergency Stop (Circuit Breaker)

**Uso:** Pausa de operaciones en caso de emergencia

**Razón:** Permite reacción rápida ante vulnerabilidades

## Componentes Principales
- **Modular**: Permitir actualizaciones y extensiones
- **Transparente**: Operaciones verificables on-chain
- **Eficiente**: Gas optimizado sin sacrificar seguridad

## Patrones Arquitectónicos

### 1. Proxy Pattern (UUPS)

**Uso:** Actualizaciones de contratos sin migrar estado

**Razón:** Permite correcciones de seguridad y mejoras sin interrumpir el servicio

### 2. Diamond Pattern (EIP-2535)

**Uso:** Gestión de funcionalidades modulares

**Razón:** Permite añadir/remover funciones sin límite de tamaño de contrato

### 3. Access Control

**Uso:** Roles y permisos granular

**Razón:** Principio de mínimo privilegio

### 4. Emergency Stop (Circuit Breaker)

**Uso:** Pausa de operaciones en caso de emergencia

**Razón:** Permite reacción rápida ante vulnerabilidades

## Componentes Principales


## Decisiones Arquitectónicas Clave

### Almacenamiento
**Decisión:** Usar storage estructurado con layout consistente
**Razón:** Evitar colisiones en upgrades y facilitar debugging

### Actualizaciones
**Decisión:** UUPS Proxy para contratos principales
**Razón:** Menor costo de deployment y actualización

### Interacciones Cross-Chain
**Decisión:** Abstraction layer para mensajería cross-chain
**Razón:** Permitir múltiples proveedores sin cambiar lógica core

## Restricciones Arquitectónicas

1. **No usar `viaIR`** - Mantener IR offline para debuggear
2. **Evitar `assembly`** - Solo cuando sea estrictamente necesario
3. **Máximo 24KB por contrato** - Limitar tamaño para evitar problemas
4. **Sin dependencias no auditadas** - Solo librerías con auditoría pública

---

*"La arquitectura no es sobre cómo se ve, sino sobre cómo funciona."*
