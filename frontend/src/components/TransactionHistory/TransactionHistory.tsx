import React, { useEffect, useState } from 'react';
import { 
  Table, 
  TableBody, 
  TableCell, 
  TableContainer, 
  TableHead, 
  TableRow, 
  Paper,
  Typography,
  CircularProgress,
  Box
} from '@mui/material';
import { format } from 'date-fns';
import { getUserTransactions } from '../../../services/conversion';

interface TransactionHistoryProps {
  userId: string;
}

const TransactionHistory: React.FC<TransactionHistoryProps> = ({ userId }) => {
  const [transactions, setTransactions] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchTransactions = async () => {
      try {
        setLoading(true);
        const data = await getUserTransactions(userId);
        setTransactions(data);
      } catch (err) {
        setError('Failed to load transaction history');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchTransactions();
  }, [userId]);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" mt={4}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Typography color="error" mt={2}>
        {error}
      </Typography>
    );
  }

  return (
    <Paper elevation={3} sx={{ p: 3, mt: 4 }}>
      <Typography variant="h6" gutterBottom>
        Conversion History
      </Typography>
      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Date</TableCell>
              <TableCell>From</TableCell>
              <TableCell>To</TableCell>
              <TableCell>Amount</TableCell>
              <TableCell>Converted</TableCell>
              <TableCell>Rate</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {transactions.map((tx) => (
              <TableRow key={tx.id}>
                <TableCell>
                  {format(new Date(tx.timestamp), 'MMM dd, yyyy HH:mm')}
                </TableCell>
                <TableCell>{tx.from_currency}</TableCell>
                <TableCell>{tx.to_currency}</TableCell>
                <TableCell>
                  {tx.from_value.toFixed(2)} {tx.from_currency}
                </TableCell>
                <TableCell>
                  {tx.to_value.toFixed(2)} {tx.to_currency}
                </TableCell>
                <TableCell>{tx.rate.toFixed(6)}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      {transactions.length === 0 && (
        <Typography variant="body2" sx={{ mt: 2 }}>
          No conversion history found
        </Typography>
      )}
    </Paper>
  );
};

export default TransactionHistory;