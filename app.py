# 配置
install_path = '/home/xlab-app-center'
webui_repo = 'AUTOMATIC1111/stable-diffusion-webui'
rename_repo = 'stable-diffusion-webui'
git_url = 'gitcode.com'
webui_port = 7860

download_tool = 'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M'

webui_args = [
'--api',
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
'--ui-settings-file /home/xlab-app-center/config.json',
'--ui-config-file /home/xlab-app-center/ui-config.json',
'--api-auth=Echoflare:Ag34d9ht',
# '--freeze-settings',
]

extensions = [
'https://gitcode.com/zanllp/sd-webui-infinite-image-browsing',
'https://gitcode.com/dtlnor/stable-diffusion-webui-localization-zh_CN', # 汉化
'https://gitcode.com/DominikDoom/a1111-sd-webui-tagcomplete', # 提示词提示器
'https://gitcode.com/Mikubill/sd-webui-controlnet', # ControlNet
]

sd_models = [
'https://civitai-delivery-worker-prod.5ac0637cfd0766c97916cefa3764fbdf.r2.cloudflarestorage.com/model/205600/cuteyukimix.IUBk.safetensors?X-Amz-Expires=86400&response-content-disposition=attachment%3B%20filename%3D%22cuteyukimixAdorable_naiV3style.safetensors%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=e01358d793ad6966166af8b3064953ad/20240131/us-east-1/s3/aws4_request&X-Amz-Date=20240131T042134Z&X-Amz-SignedHeaders=host&X-Amz-Signature=ad39d7d91e7a7034a3e9ef63578f1152bc7eb1abf3bd4664e7eb1503e8951cc4',
'https://civitai-delivery-worker-prod.5ac0637cfd0766c97916cefa3764fbdf.r2.cloudflarestorage.com/205600/model/cocotifacutev20fp16.riW4.safetensors?X-Amz-Expires=86400&response-content-disposition=attachment%3B%20filename%3D%22cocotifacute_v20.safetensors%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=e01358d793ad6966166af8b3064953ad/20240131/us-east-1/s3/aws4_request&X-Amz-Date=20240131T042613Z&X-Amz-SignedHeaders=host&X-Amz-Signature=f92614d96da35601333a39245195c19a43cd76dc22fccc16bac996f9a15799b7',
'https://civitai-delivery-worker-prod.5ac0637cfd0766c97916cefa3764fbdf.r2.cloudflarestorage.com/262917/model/anythingv5PrtRE.7wG5.safetensors?X-Amz-Expires=86400&response-content-disposition=attachment%3B%20filename%3D%22anything_v50.safetensors%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=e01358d793ad6966166af8b3064953ad/20240131/us-east-1/s3/aws4_request&X-Amz-Date=20240131T042919Z&X-Amz-SignedHeaders=host&X-Amz-Signature=72c12590f069b9ba3532d16978c16b1b9fe46f99588ffa22d5cf87957a3d997c',
'https://civitai-delivery-worker-prod.5ac0637cfd0766c97916cefa3764fbdf.r2.cloudflarestorage.com/217656/model/E5A4A9E7A9BAE4B98BE5.nadm.safetensors?X-Amz-Expires=86400&response-content-disposition=attachment%3B%20filename%3D%22Nullstyle_v20.safetensors%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=e01358d793ad6966166af8b3064953ad/20240131/us-east-1/s3/aws4_request&X-Amz-Date=20240131T045415Z&X-Amz-SignedHeaders=host&X-Amz-Signature=0b1deca32bbf723f1be14d84817dd68fce513dc3c7e63165e2d78819f7f4b18a',
]

lora_models = []

vae_models = [
'[StabilityAI]vae-ft-mse-840000.safetensors@https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors',
'[StabilityAI (SDXL)]sdxl-vae.safetensors@https://huggingface.co/stabilityai/sdxl-vae/resolve/main/sdxl_vae.safetensors',
'https://civitai-delivery-worker-prod.5ac0637cfd0766c97916cefa3764fbdf.r2.cloudflarestorage.com/86728/model/anythingV40Vae.aaHA.pt?X-Amz-Expires=86400&response-content-disposition=attachment%3B%20filename%3D%22anything-v4.0.vae.pt%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=e01358d793ad6966166af8b3064953ad/20240131/us-east-1/s3/aws4_request&X-Amz-Date=20240131T042242Z&X-Amz-SignedHeaders=host&X-Amz-Signature=29912b4e14e2f61bf1484bf0632211012ab2e230d3b2021ebd7dd89281d5afdd',
'https://civitai-delivery-worker-prod.5ac0637cfd0766c97916cefa3764fbdf.r2.cloudflarestorage.com/205600/model/animevae.Z2Oo.pt?X-Amz-Expires=86400&response-content-disposition=attachment%3B%20filename%3D%22cocotifacute_v20.pt%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=e01358d793ad6966166af8b3064953ad/20240131/us-east-1/s3/aws4_request&X-Amz-Date=20240131T042702Z&X-Amz-SignedHeaders=host&X-Amz-Signature=2b0a7d0407e140c9491def9b21da99d2978cc5b123339005df1ba77407012b8d',
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
    os.environ["PIP_INDEX_URL"] = "https://mirrors.aliyun.com/pypi/simple/"
    for i in package_envs:
        os.environ[i["env"]] = i["url"]

    os.chdir(f"{install_path}/{rename_repo}")
    os.system(f"python launch.py {' '.join(webui_args)} --port {webui_port}")

# 启动
import threading

if __name__ == '__main__':
    webui = threading.Thread(target=run_webui)
    
    webui.start()
