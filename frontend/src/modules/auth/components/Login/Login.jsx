
import { Container, Box, FormControl, Typography, TextField, Button } from '@mui/material';


function Login() {

    const handleSubmit = (event) => {
        console.log(event);
    };
    
    return (
        <>
            <Container
                sx={{
                    width: "70%",
                    height: 'fit-content',
                    display: 'flex',
                    alignItems: 'center',
                    textAlign: 'center',
                    justifyContent: 'center'
                }}
            >
                <Box
                    sx={{
                        width: '100%',
                        height: 'fit-content',
                        border: '1px solid #61D1BB',
                        borderRadius: '25px'
                    }}
                >
                    <Box 
                        sx={{
                            marginTop: '40px',
                            marginBottom: '60px',
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
                    </Box>

                    <FormControl 
                        sx={{
                            width: '60%', 
                        }} 
                    >
                        <TextField 
                            type="text"
                            label='Логин'
                            variant="outlined"
                            sx={{
                                width: '100%',
                                marginBottom: '30px',

                            }}
                        />

                        <TextField 
                            type="password"
                            label='Пароль'
                            variant="outlined"
                            sx={{
                                marginBottom: '50px'
                            }}
                        />
                        
                        <Button
                            onClick={handleSubmit}
                            variant='contained'
                            title='Отправить'
                            sx={{
                                width: '50%',
                            }}
                        >

                        </Button>
                        
                    </FormControl>
                </Box>
            </Container>
        </>
    );
}

export default Login;