
import { Container, Box, Paper, Typography, TextField, Button, Link } from '@mui/material';


function Login() {

    const handleSubmit = async (event) => {
        console.log(event.target);
    };


    return (
        <>
            <Container
                sx={{
                    width: "70%",
                    height: 'fit-content',
                    textAlign: 'center'
                }}
            >
                <Paper
                    elevation={5}
                    color="primary"
                    sx={{
                        width: '100%',
                        height: 'fit-content',
                        color: '#61D1BB',   
                        border: '1px solid #61D1BB',
                        borderRadius: '25px',
                        display: 'flex',
                        justifyContent: 'center'
                    }}
                >
                    <Box 
                        sx={{
                            width: '60%',
                            marginTop: '40px',
                            marginBottom: '40px'
                        }}
                    >
                        <Typography 
                            sx={{
                                fontSize: '38px',
                                fontWeight: 700,
                                letterSpacing: '1px',
                                textTransform: 'uppercase'
                            }}
                        > 
                            Авторизация 
                        </Typography>

                        <Box
                            component='form'
                            onSubmit={handleSubmit}
                            sx={{
                                marginTop: '40px'
                            }}
                        >
                            <TextField 
                                type="email"
                                label='Логин'
                                id='login'
                                variant="outlined"
                                sx={{
                                    marginBottom: '30px'
                                }}

                                fullWidth
                            />

                            <TextField 
                                type="password"
                                label='Пароль'
                                variant="outlined"
                                sx={{
                                    marginBottom: '15px'
                                }}

                                fullWidth
                            />
                            <Box sx={{ marginBottom: '25px' }}>
                                <Link 
                                    href="/registration"
                                    underline='hover'
                                    color='primary'
                                    sx={{
                                        fontSize: '18px',
                                        fontWeight: 600,
                                        fontFamily: 'Roboto'
                                    }}
                                >
                                    Зарегистрироваться
                                </Link>
                            </Box>
                            
                            <Button
                                type="submit"
                                variant='contained'
                                sx={{
                                    width: '70%',
                                    height: '50px',
                                    backgroundColor: '#61D1BB',
                                    alignSelf: 'center',
                                }}
                            >
                                Отправить
                            </Button>
                        </Box>
                    </Box>
                </Paper>
            </Container>
        </>
    );
}

export default Login;