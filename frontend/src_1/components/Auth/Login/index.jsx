import './index.css';

import { Link } from 'react-router-dom';



function Login() {

    return (
        <>
            <div className='login-form-wrapper'>
                <div className='login-form-inner'>
                    <div className='login-form-header'> 
                        Авторизация
                    </div>

                    <form className='login-form'>
                        <input className='' name='login' type="email" placeholder='Логин' />
                        <input className='' name='password' type="password" placeholder='Пароль' />
                        <Link to="/registration" className="registration-link"> Зарегистрироваться </Link>
                        <input className='' id='submit-button' type="submit" value="Отправить" />
                    </form>
                </div>
            </div>
        </>
    );

}

export default Login;