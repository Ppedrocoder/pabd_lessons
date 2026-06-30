const ProdutoModel = require('../models/ProdutoModel');
const ProdutoController = {
 listar(req, res) {
 const produtos = ProdutoModel.findAll();
 res.json(produtos);
 },
 buscar(req, res) {
 const id = parseInt(req.params.id);
 const produto = ProdutoModel.findById(id);
 if (!produto) return res.status(404).json({ erro: 'Não encontrado' });
 res.json(produto);
 },
 criar(req, res) {
 const novo = ProdutoModel.create(req.body);
 res.status(201).json(novo);
 },
 atualizar(req, res) {
 const id = parseInt(req.params.id);
 const atualizado = ProdutoModel.update(id, req.body);
 if (!atualizado) return res.status(404).json({ erro: 'Não encontrado' });
 res.json(atualizado);
 },
 remover(req, res) {
 const id = parseInt(req.params.id);
 const ok = ProdutoModel.destroy(id);
 if (!ok) return res.status(404).json({ erro: 'Não encontrado' });
 res.status(204).send(); // 204 No Content
 },
};
module.exports = ProdutoController;