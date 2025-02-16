import React, { useState, useContext, useEffect } from 'react';
import { ProdutoContext } from '../context/ProdutoContext';
import { getProdutos, deleteProduto } from '../api';
import ProdutoEdit from './ProdutoEdit';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, IconButton } from '@mui/material';
import { Edit, Delete } from '@mui/icons-material';

const ProdutoList = () => {
    const { state, dispatch } = useContext(ProdutoContext);
    const [produtoSelecionado, setProdutoSelecionado] = useState(null);
    const [openEdit, setOpenEdit] = useState(false);

    useEffect(() => {
        getProdutos().then(response => {
            dispatch({ type: 'SET_PRODUTOS', payload: response.data });
        });
    }, [dispatch]);

    const handleDelete = async (id) => {
        await deleteProduto(id);
        dispatch({ type: 'DELETE_PRODUTO', payload: id });
    };

    const handleEdit = (produto) => {
        setProdutoSelecionado(produto);
        setOpenEdit(true);
    };

    return (
        <TableContainer component={Paper}>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell><strong>Nome</strong></TableCell>
                        <TableCell><strong>Descrição</strong></TableCell>
                        <TableCell><strong>Preço</strong></TableCell>
                        <TableCell><strong>Quantidade</strong></TableCell>
                        <TableCell align="center"><strong>Ações</strong></TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {state.produtos.map(produto => (
                        <TableRow key={produto.id}>
                            <TableCell>{produto.nome}</TableCell>
                            <TableCell>{produto.descricao}</TableCell>
                            <TableCell>R$ {produto.preco.toFixed(2)}</TableCell>
                            <TableCell>{produto.quantidade}</TableCell>
                            <TableCell align="center">
                                <IconButton color="primary" onClick={() => handleEdit(produto)}><Edit /></IconButton>
                                <IconButton color="secondary" onClick={() => handleDelete(produto.id)}><Delete /></IconButton>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            {produtoSelecionado && (
                <ProdutoEdit
                    open={openEdit}
                    handleClose={() => setOpenEdit(false)}
                    produto={produtoSelecionado}
                    onSuccess={() => window.location.reload()}
                />
            )}
        </TableContainer>
    );
};

export default ProdutoList;
