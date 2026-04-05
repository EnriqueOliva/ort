# Configuración del Entorno Conda para Prácticos

Este documento contiene las instrucciones para crear un entorno conda con todas las dependencias necesarias para ejecutar los notebooks de los prácticos de Inteligencia Artificial Generativa.

## Comandos de Instalación

### 1. Crear el entorno conda con Python 3.11

```bash
conda create -n IAGenerativaPracticos python=3.11 -y
```

### 2. Activar el entorno

```bash
conda activate IAGenerativaPracticos
```

### 3. Instalar PyTorch con soporte CUDA para RTX 4070

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia -y
```

### 4. Instalar paquetes científicos básicos

```bash
conda install numpy pandas matplotlib seaborn scipy scikit-learn networkx -c conda-forge -y
```

### 5. Instalar paquetes adicionales con pip

```bash
pip install pgmpy torchinfo tqdm transformers diffusers imageio
```

**Nota importante sobre pgmpy:** Si encuentras un error `ImportError: BayesianNetwork has been deprecated. Please use DiscreteBayesianNetwork instead.`, esto es normal en versiones recientes de pgmpy. El código ya está actualizado para usar `DiscreteBayesianNetwork` en lugar de `BayesianNetwork` deprecado.

### 6. Instalar ipykernel para usar en VS Code

```bash
conda install ipykernel -y
```

### 7. Registrar el entorno como kernel de Jupyter

```bash
python -m ipykernel install --user --name IAGenerativaPracticos --display-name "Python (IAGenerativaPracticos)"
```

### 8. Verificar la instalación de PyTorch con CUDA

```bash
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'CUDA version: {torch.version.cuda}')"
```

## Resumen de Dependencias por Práctico

- **Práctico 1 (Tennis)**: numpy, pandas
- **Práctico 2 (Bayesian Networks)**: pandas, networkx, matplotlib, pgmpy, numpy, seaborn, scikit-learn, scipy
- **Práctico 3 (Hinton)**: torch, torchvision, matplotlib, tqdm
- **Práctico 4 (VAE)**: torch, torchvision, torchinfo, numpy, matplotlib
- **Práctico 5 (GAN)**: torch, torchvision, numpy, matplotlib, tqdm
- **Práctico 6 (Language Models)**: torch, transformers
- **Práctico 7 (Diffusion)**: torch, torchvision, diffusers, transformers, imageio, numpy, matplotlib

## Uso en VS Code

Una vez completados todos los pasos anteriores, puedes usar el entorno en VS Code:

1. Abre un notebook (.ipynb) en VS Code
2. Haz clic en el selector de kernel (esquina superior derecha)
3. Selecciona "Python (IAGenerativaPracticos)"
4. El notebook ahora usará el entorno conda con todas las dependencias instaladas

Si no aparece el kernel, reinicia VS Code después de completar el paso 7.

## Especificaciones del Sistema

- **Sistema Operativo**: Windows 11
- **GPU**: RTX 4070 12GB
- **CPU**: i5-13600k
- **RAM**: 64GB DDR4

## Notas Importantes

- Se usa `pytorch-cuda=12.1` que es compatible con RTX 4070
- Si tienes problemas con CUDA 12.1, puedes cambiar a `pytorch-cuda=11.8`
- Los paquetes de Hugging Face (transformers, diffusers) se instalan mejor con pip
- El comando de verificación al final confirmará que PyTorch detecta correctamente la GPU

## Solución de Problemas

### Si PyTorch no detecta la GPU:

1. Verifica que los drivers de NVIDIA estén actualizados
2. Reinstala PyTorch con una versión CUDA diferente:
   ```bash
   conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
   ```

### Si hay conflictos de dependencias:

Intenta instalar en un entorno limpio eliminando el anterior:
```bash
conda deactivate
conda remove -n IAGenerativaPracticos --all -y
```
Y luego vuelve a seguir los pasos desde el inicio.
