# 配置
install_path = '/home/xlab-app-center'
webui_repo = 'AUTOMATIC1111/stable-diffusion-webui'
rename_repo = 'stable-diffusion-webui'
git_url = 'gitcode.com'
webui_port = 7860

download_tool = 'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M'

webui_args = [
'--xformers',
'--no-hashing',
'--disable-nan-check',
'--enable-insecure-extension-access',
'--disable-console-progressbars', 
'--enable-console-prompts',
'--no-gradio-queue',
'--no-half-vae',
'--opt-sdp-no-mem-attention',
'--opt-split-attention',
]

extensions = [

]

sd_models = [
# '[StabilityAI (SDXL)]SDXL-1.0.safetensors@https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0_0.9vae.safetensors',
# '[StabilityAI]SD-2.1.safetensors@https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.safetensors',
]

lora_models = []

vae_models = [
# '[StabilityAI]vae-ft-mse-840000.safetensors@https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors',
# '[StabilityAI (SDXL)]sdxl-vae.safetensors@https://huggingface.co/stabilityai/sdxl-vae/resolve/main/sdxl_vae.safetensors',
]

ControlNet = False

controlnet_models = [
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_canny_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_lineart_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_openpose_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_scribble_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_softedge_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors',
'https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11u_sd15_tile_fp16.safetensors',
'https://huggingface.co/DionTimmer/controlnet_qrcode-control_v1p_sd15/resolve/main/control_v1p_sd15_qrcode.safetensors',
]

embedding_models = []

hypernetwork_models = []

esrgan_models = [
'https://huggingface.co/FacehugmanIII/4x_foolhardy_Remacri/resolve/main/4x_foolhardy_Remacri.pth',
'https://huggingface.co/konohashinobi4/4xAnimesharp/resolve/main/4x-AnimeSharp.pth',
'https://huggingface.co/lokCX/4x-Ultrasharp/resolve/main/4x-UltraSharp.pth',
]

# WebUI部署
import os
import re

def download_extensions(extensions):
    os.chdir(f'{install_path}/{rename_repo}/extensions')
    for extension in extensions:
        os.system(f'git clone {extension}')

def model_download(models, type_w):
    for model in models:
        download_files(model, type_w)

def download_files(url, source):
    if '@' in url and (not url.startswith('http://') and not url.startswith('https://')):
        parts = url.split('@', 1)
        name = parts[0]
        url = parts[1]
        rename = f"-o '{name}'"
        if 'huggingface.co' in url:
            url = url.replace("huggingface.co", "hf-mirror.com")
    else:
        if ('huggingface.co' or 'hf-mirror.com' or 'huggingface.sukaka.top') in url:
            url = url.replace("huggingface.co", "hf-mirror.com")
            match_name = re.search(r'/([^/?]+)(?:\?download=true)?$', url).group(1)
            if match_name:
                rename = f"-o '{match_name}'"
            else:
                rename = ''
        else:
            rename = ''
    source_dir = f'{install_path}/{rename_repo}/{source}'
    os.makedirs(source_dir, exist_ok=True)
    os.chdir(source_dir)
    os.system(f"{download_tool} '{url}' {rename}")
def run_webui():
    os.chdir(install_path)
    if not os.path.exists(f'{install_path}/{rename_repo}'):
        os.system(f"git clone https://{git_url}/{webui_repo} {install_path}/{rename_repo}")
        if not os.path.exists(f'{install_path}/{rename_repo}'):
            print(f'在克隆 https://{git_url}/{webui_repo} 时出错')
            exit()

    download_extensions(extensions)

    model_download(sd_models, 'models/Stable-diffusion')
    model_download(lora_models, 'models/Lora')
    model_download(vae_models, 'models/VAE')
    if ControlNet:
        model_download(controlnet_models, 'extensions/sd-webui-controlnet/models')
    model_download(hypernetwork_models, 'models/hypernetworks')
    model_download(embedding_models, 'embeddings')
    model_download(esrgan_models, 'models/ESRGAN')
    
    os.chdir(f"{install_path}/{rename_repo}")
    package_envs = [
    {"env": "STABLE_DIFFUSION_REPO", "url": os.environ.get('STABLE_DIFFUSION_REPO', "https://gitcode.net/overbill1683/stablediffusion")},
    {"env": "STABLE_DIFFUSION_XL_REPO", "url": os.environ.get('STABLE_DIFFUSION_XL_REPO', "https://gitcode.net/overbill1683/generative-models")},
    {"env": "K_DIFFUSION_REPO", "url": os.environ.get('K_DIFFUSION_REPO', "https://gitcode.net/overbill1683/k-diffusion")},
    {"env": "CODEFORMER_REPO", "url": os.environ.get('CODEFORMER_REPO', "https://gitcode.net/overbill1683/CodeFormer")},
    {"env": "BLIP_REPO", "url": os.environ.get('BLIP_REPO', "https://gitcode.net/overbill1683/BLIP")},
]
    for i in package_envs:
        os.environ[i["env"]] = i["url"]

    os.chdir(f"{install_path}/{rename_repo}")
    os.system(f"python launch.py {' '.join(webui_args)} --port {webui_port}")

# 启动
import threading

if __name__ == '__main__':
    webui = threading.Thread(target=run_webui)
    
    webui.start()
