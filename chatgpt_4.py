import face_recognition
import os

# Caminho para o diretório com as imagens das pessoas
pessoas_dir = 'D:/bkp_imagens_classificadas/'

# Carregar as imagens e codificar os rostos
codificacoes_conhecidas = []
nomes_conhecidos = []

for nome_imagem in os.listdir(pessoas_dir):
    if nome_imagem.endswith('.jpg') or nome_imagem.endswith('.png'):
        # Carregar a imagem
        caminho_imagem = os.path.join(pessoas_dir, nome_imagem)
        imagem = face_recognition.load_image_file(caminho_imagem)
        
        # Obter a codificação do rosto (assumindo cada imagem contém exatamente 1 rosto)
        codificacao_rosto = face_recognition.face_encodings(imagem)[0]
        
        # Adicionar a codificação e o nome à lista
        codificacoes_conhecidas.append(codificacao_rosto)
        nomes_conhecidos.append(nome_imagem.split('.')[0]) # Usando o nome do arquivo como identificador

# Função para identificar um rosto em uma nova imagem
def identificar_rosto(caminho_imagem_nova):
    # Carregar a imagem desconhecida
    imagem_desconhecida = face_recognition.load_image_file(caminho_imagem_nova)
    
    # Tentar obter a codificação do rosto desconhecido
    codificacoes_desconhecidas = face_recognition.face_encodings(imagem_desconhecida)
    
    for codificacao in codificacoes_desconhecidas:
        # Comparar com os rostos conhecidos
        resultados = face_recognition.compare_faces(codificacoes_conhecidas, codificacao)
        if True in resultados:
            primeiro_match = resultados.index(True)
            nome = nomes_conhecidos[primeiro_match]
            print(f"Rosto identificado como: {nome}")
        else:
            print("Rosto desconhecido.")

# Exemplo de uso
identificar_rosto('D:/bkp_imagens_classificadas_pessoas/desconhecida.jpg')
