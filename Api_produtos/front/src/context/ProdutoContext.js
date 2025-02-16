import React, { createContext, useReducer } from 'react';
import { produtoReducer } from '../reducer';

export const ProdutoContext = createContext();

export const ProdutoProvider = ({ children }) => {
    const [state, dispatch] = useReducer(produtoReducer, { produtos: [] });

    return (
        <ProdutoContext.Provider value={{ state, dispatch }}>
            {children}
        </ProdutoContext.Provider>
    );
};
