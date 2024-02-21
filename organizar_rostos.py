import face_recognition
import os
import shutil
from PIL import Image
import numpy as np

# Configuração de diretórios
diretorio_origem = 'caminho/para/diretorio/de/origem'
diretorio_destino = 'caminho/para/diretorio/de/destino'
os.makedirs(diretorio_destino, exist_ok=True)

# Rastreador de identificações únicas
identificacao_unicas = 0

# Percorrer imagens no diretório de origem
for arquivo in os.listdir(diretorio_origem):
    if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        caminho_completo = os.path.join(diretorio_origem, arquivo)
        
        # Carregar imagem
        imagem = face_recognition.load_image_file(caminho_completo)
        
        # Encontrar todos os rostos na imagem usando o modelo CNN
        localizacoes_rostos = face_recognition.face_locations(imagem, model="cnn")

        for rosto in localizacoes_rostos:
            identificacao_unicas += 1
            top, right, bottom, left = rosto
            
            # Cortar o rosto da imagem
            rosto_imagem = imagem[top:bottom, left:right]
            pil_image = Image.fromarray(rosto_imagem)
            
            # Definir o caminho da pasta de destino para este rosto
            pasta_destino_rosto = os.path.join(diretorio_destino, f'Pessoa_{identificacao_unicas}')
            os.makedirs(pasta_destino_rosto, exist_ok=True)
            
            # Salvar a imagem cortada na pasta de destino
            pil_image.save(os.path.join(pasta_destino_rosto, arquivo))

print(f'Processamento concluído. Rostos organizados em {diretorio_destino}.')
