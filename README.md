# 🎨 Image Generator with FLUX Stable Diffusion

This repository contains an image generator based on the FLUX model of Stable Diffusion, focused on providing high-quality image generation with various resource configurations.

## 📋 Requirements

- 🐍 Python 3.8 or higher
- 🔥 PyTorch 2.6.0 or compatible
- 🖥️ CUDA (recommended for GPU acceleration)
- 🤗 Hugging Face account (to obtain an access token)

## 💻 Installation

1. Clone this repository:
```bash
git clone https://github.com/R4F405/python-stable-diffusion-generator.git
cd python-stable-diffusion-generator
```

2. Create a virtual environment and install the dependencies:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## ⚙️ Configuration

Before running the generator, you need a Hugging Face access token:

1. Sign up at [Hugging Face](https://huggingface.co/)
2. Go to your profile → Settings → Access Tokens
3. Create a new token
4. Create a `.env` file in the project root with the following content:
   ```
   HUGGINGFACE_TOKEN=your_token_here
   ```
   
> ⚠️ **Important**: Never share your token or upload the `.env` file to public repositories.

## 🚀 Stable Diffusion Installation and Setup

This project uses the `diffusers` library, which provides a unified API for working with diffusion models like Stable Diffusion. The library automatically manages the download and installation of the required model.

### 🌊 FLUX Model

FLUX is an efficient implementation of Stable Diffusion that offers high-quality image generation with lower resource usage. The script specifically uses the "FLUX.1-schnell" model, which balances speed and quality.

### 🔄 First Run

The first time you run any of the scripts:

1. 📥 The FLUX model will be automatically downloaded from Hugging Face (approximately 2GB).
2. 💾 The model will be stored in the local Hugging Face cache (usually in `~/.cache/huggingface/`).
3. ⏱️ This process may take a few minutes depending on your internet connection.

### 🖥️ Hardware Requirements

- **With GPU (NVIDIA)**:
  - 🔋 Minimum: 4GB VRAM (using the script optimized with `funcionales.py`)
  - 🔋🔋 Recommended: 8GB+ VRAM for better performance
  - 🛠️ CUDA Toolkit installed (usually installed automatically with PyTorch if a compatible GPU is detected)

- **Without GPU**:
  - 💻 Minimum 16GB of system RAM
  - 🔄 CPU with good processing power
  - ⏱️ Be aware that generation will be significantly slower.

## 🔍 Usage

The repository contains two main scripts:

### 1. 🚀 GenerarImagenesFlux.py

Optimized script for general use that automatically detects if you have a GPU:

```bash
python GenerarImagenesFlux.py
```

### 2. 🧰 funcionales.py (Script with adjustments for limited VRAM)

This file contains a script optimized for systems with a GPU but limited VRAM (around 5GB):

```bash
python funcionales.py
```

## 🎛️ Customizable Parameters

You can modify the following parameters in the scripts to customize the generation:

- 💬 `prompt`: The descriptive text to generate the image.
- 🎯 `guidance_scale`: Controls how much the image adheres to the prompt (0.0 = more creative freedom).
- 🔄 `num_inference_steps`: Processing steps (more steps = better quality but more time).
- 📐 `width` and `height`: Dimensions of the generated image.
- 🎲 `generator.manual_seed()`: Seed for reproducibility of results.

## ⚡ Performance Tuning

- For systems with low VRAM:
  - 🔽 Reduce `num_inference_steps` to values between 4-20.
  - 🖼️ Use lower resolutions like 512x512.
  - 🧩 Enable `enable_attention_slicing()`.
  - 📊 Use `torch.float16` instead of `torch.bfloat16`.

- For systems without GPU:
  - 🖥️ The main script will automatically detect the absence of a GPU and use the CPU.
  - ⏱️ Be aware that CPU generation will be significantly slower.

## 🔧 Troubleshooting

- 🚫 **CUDA out of memory error**: Reduce the resolution, inference steps, or use the script optimized for limited VRAM.
- 🔌 **Model errors**: Ensure you have the correct Hugging Face token and a stable internet connection.
- 📉 **Low-quality images**: Increase the number of inference steps to improve quality.

## 📚 Available Models

The generator uses the "black-forest-labs/FLUX.1-schnell" model by default, but you can experiment with other Stable Diffusion models by modifying the line:

```python
pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", ...)
```

## 📄 License

This project is licensed under the MIT License. Consult the [LICENSE](LICENSE) file for more details.
