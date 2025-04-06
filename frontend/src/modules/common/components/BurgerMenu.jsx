
import { Box, Tooltip, IconButton } from '@mui/material';
import { Menu } from '@mui/icons-material';



function BurgerMenu() {

    const handleClick = (event) => {
        console.log(event);
    };

    return (
        <>
            <Box sx={{ display: 'flex', alignItems: 'start', textAlign: 'start', marginRight: "20px" }}>
                <Tooltip title="Авторизуйтесь">
                    <IconButton 
                        onClick={handleClick}
                        size="small"
                        sx={{ ml: 2 }}
                    >
                        <Menu 
                            sx={{ 
                                width: "55px", 
                                height: "55px",
                                color: "#61D1BB" 
                            }} 
                        />
                    </IconButton>
                </Tooltip>
            </Box>
        </>
    );
}

export default BurgerMenu;