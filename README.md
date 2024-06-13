# Introdução
 Esta API é uma ferramenta para gerenciar e converter diferentes unidades de medida. Ela utiliza Flask para a criação de rotas e SQLAlchemy para a interação com o banco de dados SQLite.

 # Principais funcionalidades da API:

* Adicionar Unidades: Permite adicionar novas unidades de medida ao sistema, como metros, litros, gramas, entre outras. Basta informar o nome da unidade, seu fator de conversão para uma unidade base e a categoria à qual pertence (por exemplo, comprimento, volume, peso).

* Listar Unidades: Você pode obter uma lista de todas as unidades disponíveis em uma determinada categoria, como todas as unidades de comprimento ou todas as unidades de peso.

* Converter Unidades: Facilita a conversão entre diferentes unidades de uma mesma categoria. Por exemplo, é possível converter horas em minutos ou de gramas para quilogramas, informando a unidade de origem, a unidade de destino e o valor a ser convertido.

# Como utilizar

- Clone o repositório em sua máquina
- Instale as dependências usando: pip install -r requirements.txt
- Inicie o servidor flask: python app.py
- Em uma nova janela do terminal, navegue até o diretório do projeto e execute o cliente: python client.py
 
