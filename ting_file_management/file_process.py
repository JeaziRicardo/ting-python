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

    return print(f'{data}\n')


def remove(instance):
    if not instance.queue:
        print('Não há elementos')
    else:
        path_file = instance.dequeue()
        remove_file = path_file['nome_do_arquivo']
        print(f'Arquivo {remove_file} removido com sucesso')


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        # O único que precisou usar o módulo sys para passar
        print('Posição inválida', file=sys.stderr)
