import React from 'react';
import { Container, Box, Typography } from '@mui/material';
import TransactionHistory from '../components/TransactionHistory/TransactionHistory';

const HistoryPage: React.FC = () => {
  // In a real app, this would come from auth context
  const userId = 'current_user';

  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Conversion History
        </Typography>
        <TransactionHistory userId={userId} />
      </Box>
    </Container>
  );
};

export default HistoryPage;