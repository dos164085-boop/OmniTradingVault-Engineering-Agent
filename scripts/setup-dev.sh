#!/bin/bash
set -e

echo "🚀 Configurando entorno de desarrollo..."

# Crear entorno virtual Python
echo "🐍 Creando entorno virtual..."
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Verificar Foundry
if ! command -v forge &> /dev/null; then
    echo "⚠️ Foundry no encontrado"
    echo "📦 Instalando Foundry..."
    curl -L https://foundry.paradigm.xyz | bash
    export PATH="$HOME/.foundry/bin:$PATH"
    foundryup
else
    echo "✅ Foundry encontrado: $(forge --version)"
fi

# Inicializar Foundry
if [ ! -d "lib" ]; then
    echo "📁 Inicializando Foundry..."
    forge init --no-commit 2>/dev/null || true
fi

# Crear .env si no existe
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ .env creado"
fi

# Validar
./scripts/validate-principles.sh

echo ""
echo "✅ Entorno configurado exitosamente!"
echo ""
echo "📝 Próximos pasos:"
echo "  1. Edita .env con tus credenciales"
echo "  2. Ejecuta: python scripts/agent-cli.py status"
