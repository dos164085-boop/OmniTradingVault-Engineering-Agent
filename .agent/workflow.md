# Flujo de Trabajo del Engineering Agent

## Ciclo de Desarrollo


## Fases Detalladas

### 1. Recepción del Work Item
- Clasificar el tipo de trabajo
- Estimar complejidad y riesgo
- Identificar dependencias

### 2. Análisis
- Analizar impacto en arquitectura
- Identificar módulos afectados
- Evaluar riesgos de seguridad

### 3. Planificación
- Descomponer en tareas pequeñas
- Estimar tiempo por tarea
- Identificar puntos de bloqueo potenciales

### 4. Implementación
- Crear rama `ai/lab/{issue-id}-{description}`
- Implementar cambios en batches pequeños
- Commit con mensajes descriptivos

### 5. Compilación
- Ejecutar `forge build`
- Verificar warnings
- Validar tamaño de bytecode

### 6. Tests
- Ejecutar `forge test`
- Verificar cobertura
- Validar invariantes

### 7. Documentación
- Actualizar spec del módulo
- Documentar nuevas funciones
- Crear o actualizar ADRs

### 8. Pull Request
- Crear PR con template completo
- Incluir enlaces a Engineering Cases
- Solicitar revisión

## Engineering Cases

Cuando el agente encuentra un bloqueo, crea un Engineering Case:

### Estructura del Case

```markdown
# Case ID: ENG-XXXX

## Título
[Descripción clara del problema]

## Contexto
- Work Item: WI-XXX
- Módulo: [nombre]
- Fecha: [timestamp]

## Síntoma
[Descripción del problema observado]

## Hipótesis Evaluadas
1. [Hipótesis 1] - Resultado: [✓/✗]
2. [Hipótesis 2] - Resultado: [✓/✗]

## Causa Raíz
[Explicación de la causa real]

## Solución Adoptada
[Descripción de la solución implementada]

## Lecciones Aprendidas
- [Lección 1]
- [Lección 2]

---

## ✅ **Verificar**

```bash
cat .agent/workflow.md
