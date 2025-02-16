import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Produtos from './pages/Produtos';
import { ProdutoProvider } from './context/ProdutoContext';

const App = () => (
    <ProdutoProvider>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/produtos" element={<Produtos />} />
            </Routes>
        </BrowserRouter>
    </ProdutoProvider>
);

export default App;
