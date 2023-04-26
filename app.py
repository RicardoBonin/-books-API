# Objetivo - CRUD de livros
# URL base - localhost
# Endpoint -
# localhost/livros - GET
# localhost/livros - POST
# localhost/livros/id - GET
# localhost/livros/id - PUT
# localhost/livros/id - DELETE

# Quais recursos - Livros
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [{
    'id': 1,
    'titulos': 'O senhor dos Anéis - A Sociedade do Anel',
    'autor': 'J.R.R Tolkien'
},
    {
    'id': 2,
    'titulos': 'Fooo - A Sociedade do Anel',
    'autor': 'J.R.R Tolkien'
}, {
    'id': 3,
    'titulos': 'Bar - A Sociedade do Anel',
    'autor': 'J.R.R Tolkien'
},]

# Consultar(todos)


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
# Consultar(id)


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Criar


@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Editar


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Excluir
# add


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
