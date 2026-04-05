# Instrucciones de Instalación - Modelos de Deep Learning

## Opción 1: Instalación con permisos de administrador (RECOMENDADO)

Ejecuta estos comandos en tu terminal WSL Ubuntu:

```bash
# 1. Instalar Python y herramientas necesarias
sudo apt update
sudo apt install -y python3-pip python3-venv python3-dev

# 2. Navegar al directorio del curso
cd /home/enrique/2doSemestre/ModelosDeDeepLearning

# 3. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# 4. Actualizar pip
pip install --upgrade pip

# 5. Instalar dependencias
pip install numpy matplotlib jupyter notebook ipykernel scipy pandas

# 6. Probar la instalación
python3 practicos/test_backprop.py
```

## Opción 2: Instalación con Miniconda (ALTERNATIVA)

Si prefieres usar conda:

```bash
# 1. Descargar Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 2. Instalar Miniconda
bash Miniconda3-latest-Linux-x86_64.sh
# Sigue las instrucciones, acepta la licencia y permite que inicialice conda

# 3. Reiniciar terminal o ejecutar:
source ~/.bashrc

# 4. Crear entorno para el curso
conda create -n modelos-dl python=3.12 numpy matplotlib jupyter notebook ipykernel -y

# 5. Activar entorno
conda activate modelos-dl

# 6. Probar la instalación
cd /home/enrique/2doSemestre/ModelosDeDeepLearning
python practicos/test_backprop.py
```

## Para ejecutar los notebooks

Una vez instalado todo:

```bash
# 1. Activar el entorno (si usaste venv)
cd /home/enrique/2doSemestre/ModelosDeDeepLearning
source venv/bin/activate

# O si usaste conda:
conda activate modelos-dl

# 2. Iniciar Jupyter Notebook
jupyter notebook

# 3. En el navegador, abrir:
#    - practicos/MLP_Toy_Example_COMPLETADO.ipynb (con las derivadas implementadas)
#    - practicos/MLP.xlsx (para el ejercicio de Excel)
```

## Verificar la implementación

Para verificar que las derivadas están correctamente implementadas:

```bash
# Con el entorno activado:
python practicos/test_backprop.py
```

Deberías ver que el loss disminuye durante el entrenamiento.

## Archivos para la entrega

Los archivos completados para entregar son:
1. **MLP_Toy_Example_COMPLETADO.ipynb** - Notebook con las 4 derivadas implementadas
2. **MLP.xlsx** - Archivo Excel para optimización manual (debes encontrar los parámetros que minimicen el loss)

## Troubleshooting

Si encuentras errores de permisos:
```bash
# Usa sudo para instalar los paquetes del sistema
sudo apt install python3-pip python3-venv

# O instala localmente sin sudo
python3 -m pip install --user numpy matplotlib jupyter notebook ipykernel
```

Si Jupyter no abre en el navegador:
- En WSL, copia la URL con el token que aparece en la terminal
- Ejemplo: http://localhost:8888/?token=abc123...