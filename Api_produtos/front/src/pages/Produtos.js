import React, { useState } from 'react';
import ProdutoForm from '../components/ProdutoForm';
import ProdutoList from '../components/ProdutoList';
import { Container, Typography, Paper, Button, Box } from '@mui/material';

const Produtos = () => {
    const [open, setOpen] = useState(false);

    return (
        <Container maxWidth="md">
            <Paper elevation={3} sx={{ padding: 3, marginTop: 3 }}>
                <Box display="flex" justifyContent="space-between" alignItems="center" marginBottom={2}>
                    <Typography variant="h4">Gerenciamento de Produtos</Typography>
                    <Button variant="contained" color="primary" onClick={() => setOpen(true)}>Novo Produto</Button>
                </Box>
                <ProdutoList />
            </Paper>
            <ProdutoForm open={open} handleClose={() => setOpen(false)} onSuccess={() => window.location.reload()} />
        </Container>
    );
};

export default Produtos;
