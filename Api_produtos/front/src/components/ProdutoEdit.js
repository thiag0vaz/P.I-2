import React, { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { updateProduto } from '../api';
import { Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';

const schema = z.object({
    nome: z.string().min(3, 'Nome deve ter pelo menos 3 caracteres'),
    descricao: z.string().min(5, 'Descrição muito curta'),
    preco: z.coerce.number().positive('Preço deve ser positivo'),
    quantidade: z.coerce.number().int().nonnegative('Quantidade deve ser um número inteiro positivo'),
});

const ProdutoEdit = ({ open, handleClose, produto, onSuccess }) => {
    const { register, handleSubmit, formState: { errors }, setValue } = useForm({
        resolver: zodResolver(schema),
    });

    useEffect(() => {
        if (produto) {
            setValue('nome', produto.nome);
            setValue('descricao', produto.descricao);
            setValue('preco', produto.preco);
            setValue('quantidade', produto.quantidade);
        }
    }, [produto, setValue]);

    const onSubmit = async (data) => {
        await updateProduto(produto.id, data);
        onSuccess();
        handleClose();
    };

    return (
        <Dialog open={open} onClose={handleClose}>
            <DialogTitle>Editar Produto</DialogTitle>
            <DialogContent>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <TextField fullWidth label="Nome" {...register('nome')} error={!!errors.nome} helperText={errors.nome?.message} margin="normal" />
                    <TextField fullWidth label="Descrição" {...register('descricao')} error={!!errors.descricao} helperText={errors.descricao?.message} margin="normal" />
                    <TextField fullWidth label="Preço" type="number" {...register('preco')} error={!!errors.preco} helperText={errors.preco?.message} margin="normal" />
                    <TextField fullWidth label="Quantidade" type="number" {...register('quantidade')} error={!!errors.quantidade} helperText={errors.quantidade?.message} margin="normal" />
                    <DialogActions>
                        <Button onClick={handleClose} color="secondary">Cancelar</Button>
                        <Button type="submit" variant="contained" color="primary">Salvar</Button>
                    </DialogActions>
                </form>
            </DialogContent>
        </Dialog>
    );
};

export default ProdutoEdit;
