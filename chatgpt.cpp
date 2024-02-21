#include <iostream>
#include <filesystem>
#include <string>

namespace fs = std::filesystem;

void moverArquivosDeImagem(const fs::path& origem, const fs::path& destino) {
    try {
        // Verifica se a pasta de origem existe
        if (!fs::exists(origem) || !fs::is_directory(origem)) {
            std::cerr << "Pasta de origem não existe ou não é um diretório." << std::endl;
            return;
        }

        // Cria a pasta de destino se ela não existir
        if (!fs::exists(destino)) {
            fs::create_directories(destino);
        }

        // Extensões de arquivo para identificação
        std::string extensoes[] = {".png", ".jpg", ".jpeg", ".gif", ".bmp"};

        // Percorre todos os arquivos na pasta de origem
        for (const auto& arquivo : fs::directory_iterator(origem)) {
            // Verifica se o item atual é um arquivo e se a extensão é uma das desejadas
            if (fs::is_regular_file(arquivo) && std::find(std::begin(extensoes), std::end(extensoes), arquivo.path().extension()) != std::end(extensoes)) {
                // Constrói o caminho de destino com o mesmo nome de arquivo
                auto novoDestino = destino / arquivo.path().filename();
                // Move o arquivo
                fs::rename(arquivo.path(), novoDestino);
                std::cout << "Arquivo movido: " << arquivo.path().filename() << std::endl;
            }
        }
    } catch (const fs::filesystem_error& e) {
        std::cerr << "Erro ao mover arquivos: " << e.what() << std::endl;
    }
}

int main() {
    fs::path pastaOrigem = "F:/";
    fs::path pastaDestino = "D:/bkp_imagens";

    moverArquivosDeImagem(pastaOrigem, pastaDestino);

    return 0;
}
