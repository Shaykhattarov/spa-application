
import { Container, Paper, Box, TextField, Link , Typography, Button } from '@mui/material';



function Registration() {
    
    const handleSubmit = (event) => {
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
                                type="text"
                                label='Имя'
                                id='name'
                                variant="outlined"
                                sx={{
                                    marginBottom: '30px'
                                }}

                                fullWidth
                            />

                            <TextField 
                                type="text"
                                label='Фамилия'
                                id='surname'
                                variant="outlined"
                                sx={{
                                    marginBottom: '30px'
                                }}

                                fullWidth
                            />

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
                                    marginBottom: '40px'
                                }}

                                fullWidth
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