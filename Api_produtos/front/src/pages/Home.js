import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from '@mui/material';

const Home = () => (
    <div>
        <h1>Bem-vindo!</h1>
        <Button component={Link} to="/produtos" variant="contained">Ver Produtos</Button>
    </div>
);

export default Home;

