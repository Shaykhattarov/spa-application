import PrivateRoute from '../../utils/privateRoute';
import Registration from '../Auth/Registration';
import Login from '../Auth/Login'
import Header from '../Header';
import Home from '../Home/index';

import './App.css';

import { Route, Routes } from 'react-router-dom'; 


function App() {
  return (
    <>
      <Header></Header>

      <Routes>
        <Route element={ <PrivateRoute /> }>
          <Route path="/" element={ <Home/> } />
        </Route>
        
        <Route path="login" element={ <Login/> } />
        <Route path="registration" element={ <Registration/> } />
        
      </Routes>

    </>
  )
}

export default App;
