# Organizador de Rostos

Este projeto utiliza a biblioteca `face_recognition` para identificar rostos em imagens e organizá-los em pastas, atribuindo a cada rosto uma identificação única (ex.: Pessoa_1, Pessoa_2, etc.).

## Configuração

Antes de começar, certifique-se de que você tem Python instalado em sua máquina e que as dependências necessárias estão instaladas. Este projeto requer a instalação da biblioteca `face_recognition` e `Pillow`.

### Instalação das Dependências

```bash
pip install face_recognition Pillow
```

### Uso

Para usar este script, atualize as variáveis diretorio_origem e diretorio_destino no script organizar_rostos.py para corresponder ao seu diretório de imagens de origem e ao diretório de destino desejado, respectivamente.

Execute o script:

```py
python organizar_rostos.py
```

O script identificará rostos nas imagens do diretório de origem e os organizará em subpastas no diretório de destino, cada uma nomeada com uma identificação única para cada rosto detectado.

### Contribuições

Contribuições para este projeto são bem-vindas. Por favor, leia as diretrizes de contribuição antes de submeter uma pull request.

### Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.
