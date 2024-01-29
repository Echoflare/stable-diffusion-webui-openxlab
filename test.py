import os

os.chdir(f"/home/xlab-app-center")
os.system(f"git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui")
os.chdir(f"/home/xlab-app-center/stable-diffusion-webui")
os.system("python launch.py")