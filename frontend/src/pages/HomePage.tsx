import React from 'react';
import { Container, Box } from '@mui/material';
import CurrencyConverter from '../components/CurrencyConverter/CurrencyConverter';
import TransactionHistory from '../components/TransactionHistory/TransactionHistory';

const HomePage: React.FC = () => {
  // In a real app, this would come from auth context
  const userId = 'current_user';

  return (
    <Container maxWidth="md">
      <Box sx={{ my: 4 }}>
        <CurrencyConverter />
        <TransactionHistory userId={userId} />
      </Box>
    </Container>
  );
};

export default HomePage;