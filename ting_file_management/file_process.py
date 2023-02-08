from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if any(item['nome_do_arquivo'] == path_file for item in instance.queue):
        print('[!] O arquivo %s já foi processado anteriormente' % path_file)
        return

    lines = txt_importer(path_file)

    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }

    instance.enqueue(data)

    return sys.stdout.write(f"{data}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
