from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_de_dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Unidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    unidade_base = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/unidades', methods=['POST'])
def adicionar_unidade():
    dados = request.get_json()
    nova_unidade = Unidade(nome=dados['nome'], unidade_base=dados['unidade_base'],
                           categoria=dados['categoria'])
    db.session.add(nova_unidade)
    db.session.commit()
    return jsonify({'message': 'Unidade adicionada com sucesso!'}), 201


@app.route('/unidades/<categoria>', methods=['GET'])
def obter_unidades(categoria):
    unidades = Unidade.query.filter_by(categoria=categoria).all()
    resultado = [{'id': unidade.id, 'nome': unidade.nome, 'unidade_base': unidade.unidade_base,
                  'categoria': unidade.categoria} for unidade in unidades]
    return jsonify(resultado), 200


@app.route('/converter', methods=['POST'])
def converter_unidades():
    dados = request.get_json()
    valor = dados['valor']
    categoria = dados['categoria']
    de_unidade = dados['de_unidade']
    para_unidade = dados['para_unidade']

    if categoria == 'comprimento':
        if de_unidade == 'metros' and para_unidade == 'centímetros':
            valor_convertido = valor * 100
        elif de_unidade == 'quilômetros' and para_unidade == 'metros':
            valor_convertido = valor * 1000
        else:
            return jsonify({'erro': 'Unidades inválidas para a categoria de comprimento'}), 400
    elif categoria == 'massa':
        if de_unidade == 'quilogramas' and para_unidade == 'gramas':
            valor_convertido = valor * 1000
        else:
            return jsonify({'erro': 'Unidades inválidas para a categoria de massa'}), 400
    elif categoria == 'volume':
        if de_unidade == 'litros' and para_unidade == 'mililitros':
            valor_convertido = valor * 1000
        else:
            return jsonify({'erro': 'Unidades inválidas para a categoria de volume'}), 400
    elif categoria == 'tempo':
        if de_unidade == 'minutos' and para_unidade == 'segundos':
            valor_convertido = valor * 60
        elif de_unidade == 'horas' and para_unidade == 'minutos':
            valor_convertido = valor * 60
        else:
            return jsonify({'erro': 'Unidades inválidas para a categoria de tempo'}), 400
    else:
        return jsonify({'erro': 'Categoria inválida'}), 400

    return jsonify({'valor_convertido': valor_convertido}), 200


@app.route('/unidades/<int:id>', methods=['DELETE'])
def excluir_unidade(id):
    unidade = Unidade.query.get_or_404(id)
    db.session.delete(unidade)
    db.session.commit()
    return jsonify({'message': 'Unidade excluída com sucesso!'})


if __name__ == '__main__':
    app.run(debug=True)
