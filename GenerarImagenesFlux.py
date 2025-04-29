import torch
from diffusers import FluxPipeline
from huggingface_hub import login
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Limpiar memoria
torch.cuda.empty_cache() #Reduce la memoria inactiva o fragmentada en la GPU.
torch.cuda.reset_peak_memory_stats() #Reinicia las estadísticas de uso máximo de memoria, asi permitiendo medir el pico de uso precisamente

# Configurar Hugging Face token
token = os.getenv("HUGGINGFACE_TOKEN")
if not token:
    raise ValueError("No se encontró el token de Hugging Face. Crea un archivo .env con HUGGINGFACE_TOKEN=tu_token")
login(token)

# Determinar dispositivo automáticamente
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Usando dispositivo: {device}")

# Cargar modelo con configuración adecuada según el dispositivo
pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-schnell",
    torch_dtype=torch.bfloat16 if device == "cuda" else torch.float32,  # Ajusta el float, si se le permite usara float32
    low_cpu_mem_usage=True #Optimiza la carga del modelo, en lugar de cargar todo el modelo en CPU y moverlo a GPU, carga el modelo por partes segun sea necesario
).to(device)  # Asignar explícitamente el dispositivo (CPU o GPU)

# Aplicar optimizaciones solo si usamos GPU
if device == "cuda":
    pipe.enable_attention_slicing()  # Divide los cálculos de atención en partes más pequeñas asi reduciendo el consumo de VRAM

# Configurar generador con el dispositivo seleccionado
generator = torch.Generator(device=device).manual_seed(0)

# Generar imagen
prompt = "A cat holding a sign that says hello world"
image = pipe(
    prompt,
    guidance_scale=0.0,  # Cuanto mas alto, la IA mas ceñira al texto, cuanto mas bajo, mas libertad creativa tendra
    num_inference_steps=4, #(Pasos de inferencia) Cuanto menor sea generara imagenes mas rapido pero con menor calidad, cuantos mas mejora la calidad de la imagen pero requiere mas tiempo y recursos
    generator=generator
).images[0]

# Guardar imagen
image.save("flux-schnell.png")
print("Imagen *flux-schnell.png* generada correctamente")