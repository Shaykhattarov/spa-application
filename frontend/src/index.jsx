import "./assets/styles/app.scss";

import { Provider } from 'react-redux';
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from 'react-router-dom';

import { ThemeProvider, createTheme } from '@mui/material/styles';

import { store } from './utils/store/store';
import App from "./App";


const LightTheme = createTheme({
  palette: {
      primary: {
          main: '#61D1BB',
          contrastText: 'white'
      }
  }
}); 


createRoot(document.getElementById('root')).render(
    <StrictMode>
      <Provider store={store} >
        <BrowserRouter>
            <ThemeProvider theme={LightTheme}>
              <App />
            </ThemeProvider>
        </BrowserRouter>
      </Provider>
    </StrictMode>,
)