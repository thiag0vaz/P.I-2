from flask import Blueprint, request, jsonify
from database import db
from models import Produto

produto_bp = Blueprint("produto_bp", __name__)

# Listar produtos
@produto_bp.route('/api/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([produto.to_dict() for produto in produtos])

# Adicionar produto
@produto_bp.route('/api/produtos', methods=['POST'])
def add_produto():
    data = request.json
    novo_produto = Produto(
        nome=data["nome"],
        descricao=data["descricao"],
        preco=data["preco"],
        quantidade=data["quantidade"]
    )
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify(novo_produto.to_dict()), 201

# Editar produto
@produto_bp.route('/api/produtos/<int:produto_id>', methods=['PUT'])
def update_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404

    data = request.json
    produto.nome = data.get("nome", produto.nome)
    produto.descricao = data.get("descricao", produto.descricao)
    produto.preco = data.get("preco", produto.preco)
    produto.quantidade = data.get("quantidade", produto.quantidade)

    db.session.commit()
    return jsonify(produto.to_dict())

# Deletar produto
@produto_bp.route('/api/produtos/<int:produto_id>', methods=['DELETE'])
def delete_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404

    db.session.delete(produto)
    db.session.commit()
    return '', 204
