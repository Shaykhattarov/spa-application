
import { Container, Paper, Box, TextField, Typography, Button } from '@mui/material';



function Registration(props) {
    const { navigate, register, errors, loading } = props;

    const handleSubmit = async (event) => {
        event.preventDefault();

        const userData = {

        };
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
                        justifyContent: 'center',
                        marginBottom: '40px'
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
                            Регистрация 
                        </Typography>

                        <Box
                            component='form'
                            onSubmit={handleSubmit}
                            sx={{
                                marginTop: '40px'
                            }}
                        >
                            <TextField 
                                error={!!errors.name}
                                fullWidth={true}
                                type="text"
                                label='Имя'
                                id='name'
                                variant="outlined"
                                sx={{
                                    marginBottom: '30px'
                                }}
                                helperText={errors.name ? `${errors.name.message}`: ''}
                                {...register('name')}
                            />

                            <TextField 
                                error={!!errors.name}
                                fullWidth={true}
                                type="text"
                                label='Фамилия'
                                id='surname'
                                variant="outlined"
                                sx={{
                                    marginBottom: '30px'
                                }}
                                helperText={errors.name ? `${errors.name.message}`: ''}
                                {...register('surname')}
                            />

                            <TextField 
                                error={!!errors.name}
                                fullWidth={true}
                                type="email"
                                label='Логин'
                                id='login'
                                variant="outlined"
                                sx={{
                                    marginBottom: '30px'
                                }}
                                helperText={errors.name ? `${errors.name.message}`: ''}
                                {...register('login')}
                            />

                            <TextField 
                                error={!!errors.name}
                                fullWidth={true}
                                type="password"
                                label='Пароль'
                                variant="outlined"
                                sx={{
                                    marginBottom: '40px'
                                }}
                                helperText={errors.name ? `${errors.name.message}`: ''}
                                {...register('password')}
                            />
                            
                            <Button
                                type="submit"
                                variant='contained'
                                sx={{
                                    width: '70%',
                                    height: '50px',
                                    backgroundColor: '#61D1BB',
                                    alignSelf: 'center',
                                }}
                                onClick={() => setLoading(true)}
                                loading={loading}
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

export default Registration;