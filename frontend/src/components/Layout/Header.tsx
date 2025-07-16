import React from 'react';
import { AppBar, Toolbar, Typography, Container } from '@mui/material';

const Header: React.FC = () => {
  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Currency Converter
          </Typography>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Header;