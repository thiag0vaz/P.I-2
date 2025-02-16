import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api/produtos';

export const getProdutos = () => axios.get(API_URL);
export const addProduto = (produto) => axios.post(API_URL, produto);
export const updateProduto = (id, produto) => axios.put(`${API_URL}/${id}`, produto);
export const deleteProduto = (id) => axios.delete(`${API_URL}/${id}`);
