import os
import shutil

# Caminhos de origem e destino base
origem = 'D:/bkp_imagens'
destino_base = 'D:/bkp_imagens_classificadas'

# Extensões de arquivos de imagem a serem buscadas
extensoes = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

# Percorrer a pasta de origem recursivamente
for pasta, subpastas, arquivos in os.walk(origem):
    for arquivo in arquivos:
        # Verifica se o arquivo tem uma extensão de imagem
        if arquivo.lower().endswith(extensoes):
            caminho_completo = os.path.join(pasta, arquivo)
            
            # Extrai a extensão do arquivo e remove o ponto para nomear a pasta
            extensao = arquivo.lower().split('.')[-1]
            pasta_destino = os.path.join(destino_base, extensao)
            
            # Certifique-se de que a pasta de destino da extensão existe
            os.makedirs(pasta_destino, exist_ok=True)
            
            destino_arquivo = os.path.join(pasta_destino, arquivo)
            
            # Verifica se o arquivo já existe no destino
            if not os.path.exists(destino_arquivo):
                try:
                    # Tenta mover o arquivo
                    shutil.move(caminho_completo, destino_arquivo)
                    print(f"Arquivo {arquivo} movido para {pasta_destino}")
                except PermissionError as e:
                    print(f"Erro de permissão ao tentar mover {arquivo}: {e}")
                except Exception as e:
                    print(f"Erro ao tentar mover {arquivo}: {e}")
            else:
                print(f"Arquivo {arquivo} já existe em {pasta_destino}. Não movido.")
