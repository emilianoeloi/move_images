#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <filesystem>
#include <ProgressBar.h>

using namespace std;

// Função para verificar se o arquivo é uma imagem
bool isImage(const string& filename) {
  // Lista de extensões de imagem
  vector<string> extensions = { ".png", ".jpg", ".gif", ".bmp" };

  // Converte o nome do arquivo para minúsculo
  string lower_filename = filename;
  transform(lower_filename.begin(), lower_filename.end(), lower_filename.begin(), ::tolower);

  // Verifica se a extensão do arquivo está na lista
  for (const string& extension : extensions) {
    if (lower_filename.find(extension) != string::npos) {
      return true;
    }
  }

  return false;
}

int main() {
  // Pasta de origem
  string source_path = "f:\\*";

  // Pasta de destino
  string destination_path = "d:\\imagens";

  // Conta o número total de arquivos
  size_t total_files = 0;
  for (const auto& entry : filesystem::recursive_directory_iterator(source_path)) {
    if (isImage(entry.path().filename().string())) {
      total_files++;
    }
  }

  // Cria uma barra de progresso
  ProgressBar pb(total_files);

  // Itera pelos arquivos da pasta de origem
  for (const auto& entry : filesystem::recursive_directory_iterator(source_path)) {
    // Obtém o nome do arquivo
    string filename = entry.path().filename().string();

    // Verifica se o arquivo é uma imagem
    if (isImage(filename)) {
      // Concatena o nome do arquivo com o caminho de destino
      string destination_file = destination_path + "\\" + filename;

      // Move o arquivo para a pasta de destino
      try {
        filesystem::rename(entry.path(), destination_file);
      } catch (const filesystem::filesystem_error& e) {
        cout << "Erro ao mover " << filename << ": " << e.what() << endl;
      }

      // Atualiza a barra de progresso
      pb.update();
    }
  }

  // Finaliza a barra de progresso
  pb.done();

  return 0;
}
