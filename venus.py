OxidationX

# Instale as bibliotecas necessárias
!pip install torch torchvision
!pip install git+https://github.com/ultralytics/yolov5.git

# Importe os módulos necessários
import torch
import os

# Defina o diretório raiz do seu ambiente
HOME = "/home/natalia/repo/corrosion"

# Mude para o diretório do YOLOv5
os.chdir(f"{HOME}/yolov5")

# Treine o modelo YOLOv5
!python train.py --img 800 --batch 16 --epochs 25 --data /path/to/your/dataset.yaml --weights yolov5s.pt --project {HOME}/runs/train --name train_results

# Avalie o modelo no conjunto de validação
!python val.py --data /path/to/your/dataset.yaml --weights {HOME}/runs/train/train_results/weights/best.pt --batch 16

# Faça previsões em novas imagens
!python detect.py --weights {HOME}/runs/train/train_results/weights/best.pt --img 800 --conf 0.25 --source /home/natalia/repo/corrosion --save-txt --save-conf

