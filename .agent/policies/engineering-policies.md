# Políticas de Ingeniería

## Políticas de Código

### Estilo y Formato
- **Solidity**: Seguir guía de estilo de Solidity
- **Nombres**: 
  - Funciones: `camelCase`
  - Variables: `snake_case` (internal), `camelCase` (public)
  - Constantes: `UPPER_SNAKE_CASE`

### Comentarios
- **Natspec**: Obligatorio para todas las funciones públicas y externas
- **Complejidad**: Comentarios para lógica no trivial
- **TODO/FIXME**: Permitidos pero deben tener issue asociado

### Estructura de Archivos

## Políticas de Seguridad

### Auditoría Interna
- **Pre-commit**: Análisis estático con Slither
- **Pre-PR**: Revisión de seguridad por pares
- **Pre-merge**: Validación con herramientas automáticas

### Dependencias
- **Actualización**: Semanal (día establecido)
- **Vulnerabilidades**: Monitoreo continuo
- **Versiones**: Siempre especificar versiones exactas

## Políticas de Testing

### Cobertura
- **Mínimo**: 90% de cobertura de líneas
- **Obligatorio**: Todos los branches de seguridad
- **Excepciones**: Documentadas y justificadas

### Tipos de Tests
1. **Unitarios**: Por función, rápidos, aislados
2. **Integración**: Entre módulos, más lentos
3. **End-to-End**: Simulando condiciones reales
4. **Invariantes**: Propiedades que siempre deben cumplirse

## Políticas de Git

### Commits
- **Formato**: `type(scope): subject`
  - Tipos: `feat`, `fix`, `docs`, `style`, `refactor`
- **Tamaño**: Commits atómicos, pequeños

### Branches
- **Main**: Solo código probado y revisado
- **Develop**: Integración continua
- **Feature**: `ai/lab/{issue-id}-{description}`
- **Hotfix**: `hotfix/{issue-id}-{description}`

### Pull Requests
- **Título**: `[WI-XXX] Descripción del cambio`
- **Revisores**: Al menos 2 aprobaciones
- **CI**: Todos los checks deben pasar

---

*"Las políticas existen para que podamos enfocarnos en lo importante."*
