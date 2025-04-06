import { Box, Divider, Avatar, Menu, MenuItem, Tooltip, IconButton, ListItemIcon } from '@mui/material';
import { Settings, PermIdentity, Logout } from '@mui/icons-material';

import { useState } from 'react';



function AccountMenu() {
    const [anchorEl, setAnchorEl] = useState(null);
    const open = Boolean(anchorEl);

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };
    
    return (
        <>
            <Box sx={{ display: 'flex', alignItems: 'start', textAlign: 'start'}}>
                <Tooltip title="Настройки профиля">
                    <IconButton 
                        onClick={handleClick}
                        size="small"
                        sx={{ ml: 2 }}
                        aria-controls={ open ? 'account-menu': undefined }
                        aria-haspopup="true"
                        aria-expanded={ open ? 'true': undefined }
                    >
                        <PermIdentity 
                            sx={{ 
                                width: "55px", 
                                height: "55px",
                                color: "#61D1BB" 
                            }} 
                        />
                    </IconButton>
                </Tooltip>
            </Box>

            <Menu
                anchorEl={anchorEl}
                id="account-menu"
                open={open}
                onClose={handleClose}
                onClick={handleClose}
                slotProps={{
                    paper: {
                        elevation: 0,
                        sx: {
                            overflow: 'visible',
                            filter: 'drop-shadow(0px 2px 8px rgba(97,209,187,0.5))',
                            mt: 1.5, 
                            '& .MuiAvatar-root': {
                                width: 32,
                                height: 32,
                                ml: -1,
                                mr: 1,
                            },
                            '&::before': {
                                content: '""',
                                display: 'block',
                                position: 'absolute',
                                top: 0,
                                right: 14,
                                width: 10,
                                height: 10,
                                bgcolor: 'background.paper',
                                transform: 'translateY(-50%) rotate(45deg)',
                                zIndex: 0,
                            },
                        },
                    },
                }}
                transformOrigin={{ horizontal: 'right', vertical: 'top' }}
                anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
            >
                <MenuItem sx={{ color: "#61D1BB" }} onClick={handleClose}>
                    <Avatar sx={{ backgroundColor: "#61D1BB" }} /> 
                    Мой профиль
                </MenuItem>
                
                <Divider />
                
                <MenuItem sx={{ color: "#61D1BB" }} onClick={handleClose}>
                  <ListItemIcon>
                    <Settings sx={{ color: "#61D1BB" }} fontSize="small" />
                  </ListItemIcon>
                  Настройки
                </MenuItem>
                
                <MenuItem sx={{ color: "#61D1BB" }} onClick={handleClose}>
                  <ListItemIcon>
                    <Logout sx={{ color: "#61D1BB" }} fontSize="small" />
                  </ListItemIcon>
                  Выйти
                </MenuItem>
            </Menu>
        </>
    );
}

export default AccountMenu;