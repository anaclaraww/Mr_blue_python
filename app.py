# Importando bibliotecas
from ultralytics.utils.plotting import Annotator
from ultralytics import YOLO


def CriandoModel():
    #Criano=do modelo, com pré treinamento do YOLOv8, versão nano
    model = YOLO('yolov8n')

    #Informando origem da imagem
    source = 'https://img.freepik.com/fotos-premium/garrafas-plasticas-de-agua-na-praia-de-areia_501761-2050.jpg'

    #Criando lista
    lista_teste = []

    #Testando modelo com a imagem source e salvando resultado na pasta runs
    detections = model.predict(source=source, show=True,conf=0.5,save=True)

    #Adicionando o resultado da analise a lista
    lista_teste.append(detections)

    #Exibindo lista
    print("detections:",detections)

    for r in detections:
        print(r.boxes.data)

    for r in detections:
        print(r.boxes.conf)
    
CriandoModel()

import os
from PIL import Image

def exibir_imagens(diretorio):
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith((".jpg", ".jpeg", ".png")):
            caminho_imagem = os.path.join(diretorio, arquivo)
            try:
                imagem = Image.open(caminho_imagem)
                imagem.show()
            except Exception as e:
                print(f"Erro ao abrir imagem: {e}")

exibir_imagens("runs/detect/predict")
