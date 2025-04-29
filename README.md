# 🎨 Generador de Imágenes con FLUX Stable Diffusion

Este repositorio contiene un generador de imágenes basado en el modelo FLUX de Stable Diffusion, enfocado en proporcionar generación de imágenes de alta calidad con diferentes configuraciones de recursos.

## 📋 Requisitos

- 🐍 Python 3.8 o superior
- 🔥 PyTorch 2.6.0 o compatible
- 🖥️ CUDA (recomendado para aceleración GPU)
- 🤗 Cuenta en Hugging Face (para obtener un token de acceso)

## 💻 Instalación

1. Clona este repositorio:
```
git clone https://github.com/tu-usuario/python-stable-diffusion-generator.git
cd python-stable-diffusion-generator
```

2. Crea un entorno virtual e instala las dependencias:
```
python -m venv .venv
# En Windows
.venv\Scripts\activate
# En macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## ⚙️ Configuración

Antes de ejecutar el generador, necesitas un token de acceso de Hugging Face:

1. Regístrate en [Hugging Face](https://huggingface.co/)
2. Ve a tu perfil → Settings → Access Tokens
3. Crea un nuevo token
4. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```
   HUGGINGFACE_TOKEN=tu_token_aqui
   ```
   
> ⚠️ **Importante**: Nunca compartas tu token ni subas el archivo `.env` a repositorios públicos.

## 🚀 Instalación y Configuración de Stable Diffusion

Este proyecto utiliza la librería `diffusers` que proporciona una API unificada para trabajar con modelos de difusión como Stable Diffusion. La biblioteca gestiona automáticamente la descarga e instalación del modelo necesario.

### 🌊 Modelo FLUX

FLUX es una implementación eficiente de Stable Diffusion que ofrece generación de imágenes de alta calidad con menor uso de recursos. El script utiliza específicamente el modelo "FLUX.1-schnell" que equilibra velocidad y calidad.

### 🔄 Primera ejecución

La primera vez que ejecutes cualquiera de los scripts:

1. 📥 Se descargará automáticamente el modelo FLUX desde Hugging Face (aproximadamente 2GB)
2. 💾 El modelo se almacenará en la caché local de Hugging Face (usualmente en `~/.cache/huggingface/`)
3. ⏱️ Este proceso puede tardar algunos minutos dependiendo de tu conexión a internet

### 🖥️ Requisitos de hardware

- **Con GPU (NVIDIA)**: 
  - 🔋 Mínimo: 4GB VRAM (usando script optimizado con funcionales.py)
  - 🔋🔋 Recomendado: 8GB+ VRAM para mejor rendimiento
  - 🛠️ CUDA Toolkit instalado (se instala automáticamente con PyTorch)

- **Sin GPU**: 
  - 💻 Mínimo 16GB de RAM del sistema
  - 🔄 CPU con buena capacidad de procesamiento
  - ⏱️ Ten en cuenta que la generación será significativamente más lenta

## 🔍 Uso

El repositorio contiene dos scripts principales:

### 1. 🚀 GenerarImagenesFlux.py

Script optimizado para un uso general que detecta automáticamente si dispones de GPU:

```
python GenerarImagenesFlux.py
```

### 2. 🧰 funcionales.py (Script con ajustes para VRAM limitada)

Este archivo contiene un script optimizado para equipos con GPU pero VRAM limitada (aproximadamente 5GB):

```
python funcionales.py
```

## 🎛️ Parámetros personalizables

Puedes modificar los siguientes parámetros en los scripts para personalizar la generación:

- 💬 `prompt`: El texto descriptivo para generar la imagen
- 🎯 `guidance_scale`: Controla qué tanto la imagen se adhiere al prompt (0.0 = más libertad creativa)
- 🔄 `num_inference_steps`: Pasos de procesamiento (más pasos = mejor calidad pero más tiempo)
- 📐 `width` y `height`: Dimensiones de la imagen generada
- 🎲 `generator.manual_seed()`: Semilla para reproducibilidad de resultados

## ⚡ Ajustes de rendimiento

- Para equipos con poca VRAM:
  - 🔽 Reduce `num_inference_steps` a valores entre 4-20
  - 🖼️ Utiliza resoluciones más bajas como 512x512
  - 🧩 Habilita `enable_attention_slicing()`
  - 📊 Usa `torch.float16` en lugar de `torch.bfloat16`

- Para equipos sin GPU:
  - 🖥️ El script principal detectará automáticamente la ausencia de GPU y usará CPU
  - ⏱️ Ten en cuenta que la generación en CPU será significativamente más lenta

## 🔧 Solución de problemas

- 🚫 **Error CUDA out of memory**: Reduce la resolución, los pasos de inferencia o utiliza el script optimizado para VRAM limitada.
- 🔌 **Errores de modelo**: Asegúrate de tener el token de Hugging Face correcto y una conexión a internet estable.
- 📉 **Imágenes de baja calidad**: Aumenta el número de pasos de inferencia para mejorar la calidad.

## 📚 Modelos disponibles

El generador utiliza por defecto el modelo "black-forest-labs/FLUX.1-schnell", pero puedes experimentar con otros modelos de Stable Diffusion modificando la línea:

```python
pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", ...)
```

## 📄 Licencia

Consulta el archivo LICENSE para más información sobre los términos de uso de este repositorio. 