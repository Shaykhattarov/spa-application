import { createAsyncThunk, isRejectedWithValue } from "@reduxjs/toolkit";
import { instance, instanceAuth } from "../../../axios";


export const loginUser = createAsyncThunk(
    'administrators/login/access-token',
    async (data, { rejectWithValue }) => {
        try {
            const user = await instance.post('administrators/login/access-token', data)
            if (
                user.data.status === 400 ||
                user.data.status === 401 ||
                user.data.status === 500
            )
                return
            sessionStorage.setItem('token', user.data.token)
            sessionStorage.setItem('name', user.data.user.firstName)
            return user.data
        } catch (error) {
            if (error.response && error.response.data.message) {
                return rejectWithValue(error.response.data.message)
            } else {
                return rejectWithValue(error.message)
            }
        }
    },
)


export const registerUser = createAsyncThunk(
    'administrators/',
    async (data, { rejectWithValue }) => {
        try {
            const user = await instance.post('administrators/', data)
            sessionStorage.setItem('token', user.data.token)
            sessionStorage.setItem('name', user.data.user.firstName)
            return user.data
        } catch (error) {
            if (error.response && error.response.data.message) {
                return rejectWithValue(error.response.data.message)
            } else {
                return rejectWithValue(error.message)
            }
        }
    },
)