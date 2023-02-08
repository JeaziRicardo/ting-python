from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # Verifica se o arquivo já foi processado anteriormente
    if any(item['nome_do_arquivo'] == path_file for item in instance.queue):
        print('[!] O arquivo %s já foi processado anteriormente' % path_file)
        return

    # Chama a função txt_importer para ler o conteúdo do arquivo
    lines = txt_importer(path_file)

    # Monta o dicionário com os dados do arquivo
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }

    # Adiciona os dados no objeto fila
    instance.enqueue(data)

    # Exibe os dados no stdout
    return sys.stdout.write(f"{data}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
