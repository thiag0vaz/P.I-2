export const produtoReducer = (state, action) => {
    switch (action.type) {
        case 'SET_PRODUTOS':
            return { ...state, produtos: action.payload };
        case 'ADD_PRODUTO':
            return { ...state, produtos: [...state.produtos, action.payload] };
        case 'DELETE_PRODUTO':
            return { ...state, produtos: state.produtos.filter(p => p.id !== action.payload) };
        default:
            return state;
    }
};
