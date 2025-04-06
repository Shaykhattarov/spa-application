import logotype from '../../../../assets/images/logotype.svg';

import AccountMenu from '../../../common/components/AccountMenu';
import BurgerMenu from '../../../common/components/BurgerMenu';

import { Box } from '@mui/material';
import { Link } from 'react-router-dom';



function Header() {

    const handleClick = (event) => {
        console.log(event);
    };

    return (
        <>
            <header>
                <Box 
                    sx={{
                        width: "85%",
                        height: "100%",
                        display: "flex",
                        justifyContent: 'space-between'
                    }}
                >

                    <Box 
                        sx={{
                            width: 'fit-content',
                            height: '100%',
                            display: 'flex',
                            alignItems: 'center',
                            textAlign: 'center',
                        }}
                    >
                        <Link to="/" >
                            <img width="200px" height="60px" src={logotype} />
                        </Link>

                    </Box>
                    
                    <Box 
                        sx={{
                            width: "fit-content", 
                            display: 'flex', 
                            alignItems: 'center', 
                            textAlign: 'center'
                        }}
                    >
                        <BurgerMenu/>
                        <AccountMenu />
                    </Box>

                </Box>
            </header>
        </>
    );
}


export default Header;