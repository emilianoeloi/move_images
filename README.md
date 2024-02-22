# Projeto de Transferência de Imagens

Este projeto em Python automatiza a transferência de arquivos de imagem de uma pasta de origem para uma pasta de destino, identificando arquivos pelas suas extensões (como PNG, JPG, GIF, BMP, etc.) de forma recursiva. Foi desenvolvido com a assistência do ChatGPT, utilizando informações e estratégias de programação sugeridas durante nossas conversas. Além disso, foi empregada a pesquisa no Google Gemini para otimizar soluções e abordagens de código.

## Funcionalidades

- **Identificação de Imagens:** O script identifica arquivos de imagem com base em suas extensões.
- **Transferência Recursiva:** Pesquisa e transfere imagens de forma recursiva dentro de diretórios e subdiretórios.
- **Tratamento de Duplicatas:** Renomeia automaticamente arquivos duplicados ao transferi-los, evitando a sobreposição de arquivos.
- **Log de Atividades:** Gera um log de todas as transferências realizadas para facilitar a revisão e auditoria.
- **Configuração Flexível:** Permite ao usuário especificar as extensões de arquivo desejadas e os diretórios de origem e destino através de argumentos de linha de comando.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação utilizada para o desenvolvimento do projeto.
- **ChatGPT:** Fornecido pela OpenAI, foi utilizado para orientações sobre lógica de programação, estruturação de código e resolução de problemas.
- **Google Gemini:** Empregado para pesquisas complementares e validação de estratégias de implementação.

## Pré-requisitos

Para executar este projeto, você precisará de Python instalado em sua máquina. Não são necessárias bibliotecas externas adicionais além das padrão do Python.

## Como Usar

1. Clone o repositório para sua máquina local.
2. Abra o terminal e navegue até o diretório do projeto.
3. Execute o script com os diretórios de origem e destino como argumentos, opcionalmente especificando as extensões de arquivo:

```bash
python src/transferir_imagens.py /caminho/para/origem /caminho/para/destino --extensoes .png .jpg
```

## Contribuindo
Sua contribuição é bem-vinda! Sinta-se à vontade para forkar o projeto, fazer suas alterações e abrir um Pull Request para contribuir com melhorias e novas funcionalidades.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Agradecimentos
Agradecimento especial ao ChatGPT e ao Google Gemini por facilitarem o processo de pesquisa e desenvolvimento deste projeto.


### Notas Adicionais

- **Personalização:** Certifique-se de ajustar o README conforme necessário para refletir qualquer funcionalidade adicional ou alterações específicas que você tenha feito no projeto.
- **Licença:** Inclua um arquivo de licença no seu repositório se ainda não o fez. A licença MIT mencionada é apenas um exemplo.

Este README aprimorado oferece um guia completo para qualquer pessoa interessada em entender e utilizar seu projeto, destacando a metodologia de desenvolvimento e as ferramentas envolvidas.


