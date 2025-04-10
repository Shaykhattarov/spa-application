import axios from 'axios';

const token = sessionStorage.getItem('token');

export const instance = axios.create({
    baseURL: `${process.env.VITE_BACKEND_API_URL}`,
    timeout: 1000,
    headers: {}
});

export const instanceAuth = axios.create({
    baseURL: `${process.env.VITE_BACKEND_API_URL}`,
    timeout: 1000,
    headers: {
        Authorization: `Bearer ${token}`
    }
});