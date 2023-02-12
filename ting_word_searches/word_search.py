def exists_word(word, instance):
    info = []
    for item in instance.queue:
        occs = [{'linha': i + 1}
                for i, line in enumerate(item['linhas_do_arquivo'])
                if word.lower() in line.lower()]
    if len(occs) > 0:
        info.append({
            'palavra': word,
            'arquivo': item['nome_do_arquivo'],
            'ocorrencias': occs
        })
    return info


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
