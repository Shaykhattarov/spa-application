
import { useLocation, useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup'
import { useSelector, useDispatch } from 'react-redux';

import { LoginSchema, RegistrationSchema } from '../../../utils/yup';


import Login from './Login/Login';
import Registration from './Registration/Registration';


function Authentication(formData) {
    const location = useLocation();
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const loading = useSelector((state) =>  state.auth);

    const handleSubmit = async (data) => {
        e.preventDefault();

        if (location.pathname === '/login') {
            try {
                await dispatch(); // Добавить бизнес-логику авторизации в виде функции
                navigate('/');
            } catch (e) {
                console.log(e);
                return e;
            }
        }

        try {
            const userData = {
                name: data.name,
                surname: data.surname,
                login: data.login,
                password: data.password
            }

            await dispatch(); // Добавить бизнес-логику регистрации в виде функции
            navigate('/');

        } catch (e) {
            console.log(e);
            return e;
        }
    };

    if (location.pathname === '/login') {

        const {
            register,
            formState: { errors },
            handleSubmit,
        } = useForm({ resolver: yupResolver(LoginSchema)});


        return (
            <>
                <Login 
                    navigate={navigate}
                    register={register}
                    errors={errors}
                    loading={loading}
                />
            </>
        );
    }

    if (location.pathname === '/registration')
    {
        const {
            register,
            formState: { errors },
            handleSubmit,
        } = useForm({ resolver: yupResolver(RegistrationSchema)});

        return (
            <>
                <Registration 
                    navigate={navigate}
                    register={register}
                    errors={errors}
                    loading={loading}
                />
            </>
        );
    }
}


export default Authentication;