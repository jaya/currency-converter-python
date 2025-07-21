import React from 'react';
import { Button, AppBar, Toolbar, Typography, Container } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Currency Converter App
          </Typography>
          <Button color="inherit" component={RouterLink} to="/">
            Currency Converter
          </Button>
          <Button color="inherit" component={RouterLink} to="/history">
            History
          </Button>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Header;
