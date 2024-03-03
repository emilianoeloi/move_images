import face_recognition
import os
import random
import shutil
from tqdm import tqdm

# Lista de nomes genéricos brasileiros
Nomes_brasileiros = ["Ana Silva", "João Santos", "Maria Oliveira", "Pedro Souza", "Camila Costa", "Lucas Rodrigues", "Julia Almeida", "Mateus Lima", "Larissa Pereira", "Guilherme Gomes"]

def mover_arquivos_com_rostos(origem, destino_base):
  # Certifique-se de que a pasta de destino existe
  os.makedirs(destino_base, exist_ok=True)

  # Extensões de arquivos de imagem a serem buscadas
  extensoes = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

  # Percorrer a pasta de origem recursivamente
  for pasta, subpastas, arquivos in os.walk(origem):
    for arquivo in tqdm(arquivos):
      if arquivo.lower().endswith(extensoes):
        caminho_completo = os.path.join(pasta, arquivo)

        try:
          # Carrega a imagem
          imagem = face_recognition.load_image_file(caminho_completo)

          # Detecta rostos na imagem
          localizacoes_rosto = face_recognition.face_locations(imagem)

          # Se rostos foram detectados, move o arquivo
          if localizacoes_rosto:
            # Reconhece o rosto ou gera um nome genérico
            if reconhecido:
              nome_pessoa = reconhecimento.nome
            else:
              nome_pessoa = random.choice(Nomes_brasileiros)

            # Cria a pasta de destino
            destino_arquivo = os.path.join(destino_base, nome_pessoa)
            os.makedirs(destino_arquivo, exist_ok=True)

            # Move o arquivo
            shutil.move(caminho_completo, os.path.join(destino_arquivo, arquivo))
            tqdm.write(f"Rosto detectado e arquivo {arquivo} movido para {destino_arquivo}")
          else:
            tqdm.write(f"Nenhum rosto detectado em {arquivo}")
        except Exception as e:
          tqdm.write(f"Erro ao processar {arquivo}: {e}")

# Define os caminhos de origem e destino
origem = '/mnt/d/bkp_imagens_classificadas/'
destino_base = '/mnt/d/bkp_imagens_classificadas_pessoas/'

# Chama a função para mover os arquivos
mover_arquivos_com_rostos(origem, destino_base)
