# Modelo de Confianza del Agente

## Visión General

El modelo de confianza define cómo el agente gana y mantiene autonomía en el desarrollo. Es un sistema progresivo donde el agente debe demostrar competencia antes de obtener más libertad.

## Niveles de Confianza

### Nivel 0: Observador (Read-Only)
**Propósito:** Familiarización con el código base

**Capacidades:**
- ✅ Lectura de código y documentación
- ✅ Análisis estático
- ✅ Sugerencias no vinculantes

**Restricciones:**
- ❌ No puede crear branches
- ❌ No puede hacer commits
- ❌ No puede abrir PRs

---

### Nivel 1: Asistente (Helper)
**Propósito:** Proponer cambios bajo supervisión

**Capacidades:**
- ✅ Crear branches de análisis
- ✅ Generar planes de implementación
- ✅ Proponer cambios concretos

**Restricciones:**
- ❌ No puede hacer commits directos
- ❌ No puede mergear PRs
- ✅ Cada PR requiere 100% revisión humana

---

### Nivel 2: Ingeniero Junior (Nivel Actual)
**Propósito:** Implementar features con supervisión parcial

**Capacidades:**
- ✅ Implementar features completas
- ✅ Crear Engineering Cases
- ✅ Actualizar documentación

**Restricciones:**
- ❌ No puede tocar módulos críticos (security, core)
- ✅ 50% de PRs requieren revisión aleatoria

---

### Nivel 3: Ingeniero Senior
**Propósito:** Autonomía total en módulos designados

**Capacidades:**
- ✅ Implementar cualquier feature
- ✅ Refactorizar arquitectura
- ✅ Decidir estrategias de implementación

**Restricciones:**
- ❌ No puede cambiar principios fundamentales (requiere ADR)
- ✅ 20% de PRs requieren sample review

---

## Mecanismo de Promoción

### Métricas de Evaluación

| Métrica | Peso | Nivel 1 | Nivel 2 | Nivel 3 |
|---------|------|---------|---------|---------|
| Build Success Rate | 25% | > 80% | > 90% | > 95% |
| Test Pass Rate | 25% | > 90% | > 95% | > 99% |
| Review Approval | 20% | > 80% | > 85% | > 90% |
| Incident Rate | 15% | < 10% | < 5% | < 1% |
| Learning Rate | 15% | > 50% | > 70% | > 80% |

### Proceso de Promoción

1. **Evaluación Periódica** (Cada 2 semanas)
2. **Revisión de Métricas**
3. **Decisión** - Si cumple criterios → Promoción
4. **Documentación** - ADR para cambios de nivel
5. **Período de Prueba** - 2 semanas en nuevo nivel

---

## Plan de Degradación

### Señales de Degradación

| Señal | Acción | Plazo |
|-------|--------|-------|
| 3 builds fallidos consecutivos | Revisión inmediata | < 1 hora |
| 2 incidentes P1 en una semana | Degradación de nivel | < 24 horas |

### Proceso de Degradación

1. **Alerta Automática** - Notificación al equipo
2. **Análisis de Causa** - Revisión de logs
3. **Acción Correctiva** - Degradación temporal
4. **Recuperación** - Demostrar mejora por 2 semanas

---

*"La confianza se gana, no se da."*
