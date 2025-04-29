import os
from diffusers import FluxPipeline
import torch
from huggingface_hub import login
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar límite de VRAM a 5 GB
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:256"  # Ajustar el tamaño del bloque de memoria

# Ingresar el token de Hugging Face
token = os.getenv("HUGGINGFACE_TOKEN")
if not token:
    raise ValueError("No se encontró el token de Hugging Face. Crea un archivo .env con HUGGINGFACE_TOKEN=tu_token")
login(token)

# Cargar el modelo asegurando que está en CUDA
pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-schnell",
    torch_dtype=torch.float16,  # Usar float16 en lugar de bfloat16
    device_map=None  # Evita la distribución automática para forzar a CUDA
)

pipe.to("cuda")  # Mover el modelo a la GPU
pipe.enable_attention_slicing()  # Optimiza VRAM

# Limpiar caché de memoria antes de la inferencia
torch.cuda.empty_cache()

# Generar imagen
prompt = "A cat holding a sign that says hello world"
image = pipe(
    prompt,
    guidance_scale=0.0,
    num_inference_steps=20,  # Reducir pasos de inferencia
    width=512,  # Reducir resolución
    height=512,  # Reducir resolución
    generator=torch.Generator(device="cuda").manual_seed(0)  # Asegura que el generador también usa CUDA
).images[0]

image.save("flux-schnell.png")
print("✅ Imagen generada en GPU con límite de 5GB VRAM.")