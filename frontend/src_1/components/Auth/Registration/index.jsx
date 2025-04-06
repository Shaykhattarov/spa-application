import './index.css';



function Registration() {

    return (
        <>
            <div className='registration-form-wrapper'>
                <div className='registration-form-inner'>
                    <div className='registration-form-header'> 
                        Регистрация 
                    </div>

                    <form className='registration-form'>
                        <input className='' name='name' type="text" placeholder='Имя' />
                        <input className='' name='surname' type="text" placeholder='Фамилия' />
                        <input className='' name='login' type="email" placeholder='Логин' />
                        <input className='' name='password' type="password" placeholder='Пароль' />
                        <input className='' id='submit-button' type="submit" value="Отправить" />
                    </form>
                </div>
            </div>
        </>
    );

}

export default Registration;