
import { Box, Container, Typography } from '@mui/material';
import { LocalShipping, Map, Store } from '@mui/icons-material';

function Home() {

    return (
        <>
            <Box 
                sx={{
                    textAlign: 'center'   
                }}
            >
                <Typography
                    sx={{
                        fontSize: '86px',
                        fontWeight: 800,
                        textTransform: 'uppercase'
                    }}
                > 
                    Учет приема товаров 
                </Typography>
                <Typography
                    sx={{
                        fontSize: '64px',
                        fontWeight: 800,
                        textTransform: 'uppercase'
                    }}
                > 
                    в продуктовом магазине 
                </Typography>                   
            </Box>
            <Box
                sx={{
                    display: 'flex',
                    justifyContent: 'space-around',
                    marginTop: '60px'
                }}
            >
                <LocalShipping sx={{ width: '110px', height: '110px' }} />
                <Map sx={{ width: '110px', height: '110px' }} />
                <Store sx={{ width: '110px', height: '110px' }} />
            </Box>
        </>
    );
}

export default Home;