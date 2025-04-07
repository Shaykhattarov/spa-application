
import { createSlice } from '@reduxjs/toolkit';


const initialState = {
    user: {
        token: '',
        user: {}
    },
    isLogged: false,
    isLoading: false,
}


export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {

    }
});


