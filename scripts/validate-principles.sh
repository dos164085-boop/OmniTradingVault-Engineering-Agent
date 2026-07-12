#!/bin/bash
set -e

echo "🔍 Validando principios..."

# Verificar Python
if command -v python3 &> /dev/null; then
    echo "✅ Python encontrado: $(python3 --version)"
else
    echo "❌ Python no encontrado"
    exit 1
fi

# Verificar Git
if command -v git &> /dev/null; then
    echo "✅ Git encontrado: $(git --version)"
else
    echo "❌ Git no encontrado"
    exit 1
fi

# Verificar .env
if [ ! -f ".env" ]; then
    echo "⚠️ .env no encontrado, creando..."
    cp .env.example .env
    echo "✅ .env creado. Edítalo con tus credenciales."
fi

# Verificar estructura
echo "📁 Verificando estructura..."
[ -d ".agent" ] && echo "✅ .agent existe" || echo "❌ .agent no existe"
[ -d "scripts" ] && echo "✅ scripts existe" || echo "❌ scripts no existe"

echo "✅ Validación completada"
