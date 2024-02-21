import os
import shutil

# Caminhos de origem e destino
origem = 'F:/'
destino = 'D:/bkp_imagens'

# Certifique-se de que a pasta de destino existe
os.makedirs(destino, exist_ok=True)

# Extensões de arquivos de imagem a serem buscadas
extensoes = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

# Percorrer a pasta de origem recursivamente
for pasta, subpastas, arquivos in os.walk(origem):
    for arquivo in arquivos:
        # Verifica se o arquivo tem uma extensão de imagem
        if arquivo.lower().endswith(extensoes):
            caminho_completo = os.path.join(pasta, arquivo)
            destino_arquivo = os.path.join(destino, arquivo)
            
            # Verifica se o arquivo já existe no destino
            if not os.path.exists(destino_arquivo):
                try:
                    # Tenta mover o arquivo
                    shutil.move(caminho_completo, destino_arquivo)
                    print(f"Arquivo {arquivo} movido para {destino}")
                except PermissionError as e:
                    print(f"Erro de permissão ao tentar mover {arquivo}: {e}")
                except Exception as e:
                    print(f"Erro ao tentar mover {arquivo}: {e}")
            else:
                print(f"Arquivo {arquivo} já existe no destino. Não movido.")
