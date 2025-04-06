import PrivateRoute from "./utils/privateRoute";

import Header from './modules/base/components/Header/Header';
import Login from './modules/auth/components/Login/Login';
import Home from './modules/base/components/Home/Home';

import { Container } from '@mui/material';
import { Routes, Route } from 'react-router-dom';


function App() {
    
    return (
        <>
            <Header></Header>

            <Container sx={{ marginTop: '200px' }} >
                <Routes>
                    <Route element={ <PrivateRoute/> }></Route>

                    <Route path="/" element={ <Home /> } />
                    <Route path="/login" element={ <Login />} />
                </Routes>
            </Container>
        </>
    );
} 

export default App;