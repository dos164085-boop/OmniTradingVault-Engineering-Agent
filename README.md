# 🏦 OmniTradingVault Engineering Agent v3.0

**Agente de Ingeniería Autónomo para el Protocolo OmniTradingVault**

[![Version](https://img.shields.io/badge/version-3.0.0-blue)](.agent/version.yaml)
[![Trust Level](https://img.shields.io/badge/trust-level%202-yellow)](.agent/policies/trust-model.md)

## 🎯 Misión

Crear un asistente de ingeniería que **piensa como un ingeniero senior**, priorizando arquitectura, calidad y mantenibilidad sobre velocidad.

## 🚀 Quick Start

```bash
# Configurar entorno
./scripts/setup-dev.sh

# Ver estado del agente
python scripts/agent-cli.py status

# Analizar un work item
python scripts/agent-cli.py analyze WI-001