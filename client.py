import requests

url_api = 'http://127.0.0.1:5000'


def adicionar_unidade(nome, unidade_base, categoria):
    response = requests.post(f'{url_api}/unidades',
                             json={'nome': nome, 'unidade_base': unidade_base, 'categoria': categoria})
    if response.status_code == 201:
        print('Unidade adicionada com sucesso!')
    else:
        print('Erro ao adicionar unidade:', response.text)


def obter_unidades(categoria):
    response = requests.get(f'{url_api}/unidades/{categoria}')
    if response.status_code == 200:
        print(response.json())
    else:
        print('Erro ao obter unidades:', response.text)


def converter_unidades(valor, de_unidade, para_unidade, categoria):
    response = requests.post(f'{url_api}/converter',
                             json={'valor': valor, 'de_unidade': de_unidade, 'para_unidade': para_unidade,
                                   'categoria': categoria})
    if response.status_code == 200:
        print(response.json())
    else:
        print('Erro ao converter unidades:', response.text)


def excluir_unidade(id):
    response = requests.delete(f'{url_api}/unidades/{id}')
    if response.status_code == 200:
        print('Unidade excluída com sucesso!')
    else:
        print('Erro ao excluir unidade:', response.text)


if __name__ == '__main__':
    # Adicionar unidades
    adicionar_unidade('metros', 1, 'comprimento')
    adicionar_unidade('quilômetros', 1000, 'comprimento')
    adicionar_unidade('centímetros', 0.01, 'comprimento')
    adicionar_unidade('gramas', 1, 'massa')
    adicionar_unidade('quilogramas', 1000, 'massa')
    adicionar_unidade('litros', 1, 'volume')
    adicionar_unidade('mililitros', 0.001, 'volume')
    adicionar_unidade('minutos', 1, 'tempo')
    adicionar_unidade('segundos', 1 / 60, 'tempo')
    adicionar_unidade('horas', 60, 'tempo')

    # Listar unidades das categorias
    obter_unidades('comprimento')
    obter_unidades('massa')
    obter_unidades('volume')
    obter_unidades('tempo')

    # Converter unidades
    converter_unidades(200, 'metros', 'centímetros', 'comprimento')
    converter_unidades(250, 'quilômetros', 'metros', 'comprimento')
    converter_unidades(470, 'quilogramas', 'gramas', 'massa')
    converter_unidades(125, 'litros', 'mililitros', 'volume')
    converter_unidades(380, 'minutos', 'segundos', 'tempo')
    converter_unidades(900, 'horas', 'minutos', 'tempo')

    # Excluir unidades por ID
    #excluir_unidade(1) Descomentar essa linha caso queira utilizar o metodo de exclusão e adicionar o ID da unidade desejada