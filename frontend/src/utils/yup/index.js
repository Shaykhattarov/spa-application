import * as yup from 'yup';
import { AppErrors } from '../errors';


export const LoginSchema = yup.object().shape({
    login: yup.string()
        .email(AppErrors.InvalidEmail)
        .required(AppErrors.RequiredField),
    password: yup.string()
        .min(6, AppErrors.minPasswordLength)
        .required(AppErrors.RequiredField)
        .matches(/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[a-zA-Z!#$%&? "])[a-zA-Z0-9!@#$%&?]{6,20}$/, AppErrors.InvalidPassword)
});


export const RegistrationSchema = yup.object().shape({
    name: yup.string()
        .min(2, AppErrors.minStringLength)
        .required(AppErrors.RequiredField),
    surname: yup.string()
        .min(2, AppErrors.minStringLength)
        .required(AppErrors.RequiredField),
    login: yup.string()
        .email(AppErrors.InvalidEmail)
        .required(AppErrors.RequiredField),
    password: yup.string()
        .min(6, AppErrors.minPasswordLength)
        .required(AppErrors.RequiredField)
        .matches(/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[a-zA-Z!#$%&? "])[a-zA-Z0-9!@#$%&?]{6,20}$/, AppErrors.InvalidPassword)
});