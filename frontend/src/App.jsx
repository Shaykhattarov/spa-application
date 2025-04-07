import PrivateRoute from "./utils/routers/privateRoute";

import Authentication from "./modules/auth/components";
import Header from './modules/base/components/Header/Header';
import Home from './modules/base/components/Home/Home';

import { Container } from '@mui/material';
import { Routes, Route } from 'react-router-dom';





function App() {
    
    return (
        <>
            <Header></Header>
            <Container sx={{ marginTop: '200px' }} >
                <Routes>
                    <Route path="/" element={ <Home /> } index />
                    <Route element={ <PrivateRoute /> } >
                        <Route path="/login" element={ <Authentication /> } />
                    </Route>

                    <Route path="/registration" element={ <Authentication />} />
                </Routes>
            </Container>
        </>
    );
} 

export default App;