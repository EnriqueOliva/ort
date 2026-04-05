#!/bin/bash

# Script para configurar el entorno de Modelos de Deep Learning
# Este script instala las dependencias necesarias localmente

echo "============================================"
echo "Setup para Modelos de Deep Learning"
echo "============================================"

# Detectar si estamos en WSL
if grep -qi microsoft /proc/version; then
    echo "Detectado: Ejecutando en WSL"
fi

# Verificar Python
echo -e "\n1. Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "   ✓ $PYTHON_VERSION instalado"
else
    echo "   ✗ Python3 no encontrado. Por favor instala Python 3.8+"
    exit 1
fi

# Opción 1: Intentar crear un venv (si está disponible)
echo -e "\n2. Configurando entorno virtual..."
if python3 -m venv venv 2>/dev/null; then
    echo "   ✓ Entorno virtual creado"
    echo ""
    echo "   Para activar el entorno, ejecuta:"
    echo "   source venv/bin/activate"
    echo ""

    # Activar el entorno y instalar dependencias
    source venv/bin/activate

    # Actualizar pip
    echo "3. Actualizando pip..."
    python3 -m pip install --upgrade pip

    # Instalar dependencias
    echo "4. Instalando dependencias..."
    pip install -r requirements.txt

    echo -e "\n✓ Configuración completa!"
    echo ""
    echo "Para usar el entorno:"
    echo "  1. Activa el entorno: source venv/bin/activate"
    echo "  2. Ejecuta Jupyter: jupyter notebook"
    echo "  3. Abre los notebooks en practicos/"
    echo ""
    echo "Para desactivar el entorno: deactivate"

else
    echo "   ✗ No se pudo crear el entorno virtual"
    echo ""
    echo "Opción alternativa: Instalación local con --user"
    echo ""

    # Opción 2: Instalar con --user
    echo "Instalando paquetes localmente (--user)..."

    # Verificar si pip está disponible
    if ! python3 -m pip --version &> /dev/null; then
        echo "✗ pip no está instalado."
        echo ""
        echo "Por favor, ejecuta uno de estos comandos con sudo:"
        echo "  - sudo apt install python3-pip python3-venv"
        echo "  - o instala Anaconda/Miniconda desde https://docs.conda.io/en/latest/miniconda.html"
        exit 1
    fi

    # Instalar con --user
    python3 -m pip install --user -r requirements.txt

    echo -e "\n✓ Paquetes instalados localmente"
    echo ""
    echo "Para usar los notebooks:"
    echo "  1. Ejecuta: python3 -m jupyter notebook"
    echo "  2. Abre los notebooks en practicos/"
fi

echo ""
echo "============================================"
echo "Para probar la instalación:"
echo "  python3 test_backprop.py"
echo "============================================"