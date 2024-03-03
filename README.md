# Projeto de Transferência de Imagens com Interface de Visualização Facial

Este projeto em Python não só automatiza a transferência de arquivos de imagem de uma pasta de origem para uma pasta de destino, mas também fornece uma interface web para visualizar informações de reconhecimento facial em imagens identificadas. Utilizando tecnologias como Flask para o backend e HTML/CSS/JavaScript para o frontend, o projeto permite a identificação e exibição de pontos de referência facial e caixas delimitadoras sobre as imagens processadas. Desenvolvido com a orientação do ChatGPT e pesquisas no Google Gemini, este projeto abrange desde a programação backend até o desenvolvimento de interfaces web front-end.

## Funcionalidades Adicionais

- **Interface Web para Visualização Facial:** Uma interface web simples, mas eficaz, que exibe imagens lado a lado, mostrando tanto a imagem de referência quanto a imagem com rostos identificados, incluindo caixas delimitadoras e pontos de referência faciais.
- **Visualização de Dados de Reconhecimento Facial:** Utiliza dados de reconhecimento facial para desenhar caixas delimitadoras e pontos de referência diretamente nas imagens através de um canvas HTML, permitindo uma fácil identificação visual de rostos nas imagens.

## Configuração do Projeto Web

O projeto web é construído sobre o Flask, um microframework web em Python, que serve a interface web e processa imagens para reconhecimento facial:

### Pré-requisitos para o Web

- Flask: Para rodar o servidor web e processar as requisições.
- face_recognition: Para identificar rostos e pontos de referência nas imagens.

### Como Rodar o Projeto Web

1. Certifique-se de ter o Python e o pip instalados.
2. Instale as dependências necessárias com `pip install -r requirements.txt`, que incluirá Flask e face_recognition.
3. Execute o arquivo `app.py` para iniciar o servidor Flask.
4. Acesse a interface web através do navegador em `http://localhost:5000`.

## Como Usar a Interface Web

Após iniciar o servidor Flask, você poderá:

1. Carregar imagens de referência e imagens a serem identificadas na interface web.
2. Visualizar automaticamente os resultados do reconhecimento facial, incluindo caixas delimitadoras e pontos de referência, sobre as imagens.

## Tecnologias Adicionais Utilizadas

- **Flask:** Microframework web utilizado para criar a interface web do projeto.
- **HTML/CSS/JavaScript:** Utilizados para desenvolver a interface do usuário e lógica front-end para a visualização de dados de reconhecimento facial.

## Contribuindo

Estamos abertos a contribuições! Se você tem ideias para melhorar a interface ou expandir as funcionalidades de reconhecimento facial, por favor, contribua através de Pull Requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE.md para detalhes.

## Agradecimentos Especiais

- **OpenAI (ChatGPT):** Por fornecer orientações e insights valiosos para o desenvolvimento do projeto.
- **Google Gemini:** Por oferecer uma plataforma de pesquisa que ajudou a solucionar desafios de implementação.
