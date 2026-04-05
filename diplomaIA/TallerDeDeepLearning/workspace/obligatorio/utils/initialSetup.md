  # 1. Crear nuevo conda environment
  conda env create -f C:\Users\Enrique\Documents\2doSemestre\TallerDeDeepLearning\workspace\obligatorio\environment.yml -n TallerDeIAObligatorio

  # 2. Activar el environment
  conda activate TallerDeIAObligatorio

  # 3. Instalar dependencias adicionales necesarias
  conda install -c conda-forge albumentations opencv pillow

  # 4. Verificar instalación de PyTorch con CUDA (para tu RTX 4070)
  python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA disponible: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else     
  \"N/A\"}')"

  # 5. Configurar Kaggle API (para descargar dataset y subir predicciones)
  # Descargar kaggle.json desde https://www.kaggle.com/settings/account
  # y copiarlo a C:\Users\Enrique\.kaggle\kaggle.json