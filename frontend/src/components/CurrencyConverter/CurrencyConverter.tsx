import React, { useState } from 'react';
import {
  Box,
  TextField,
  Button,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Typography,
  Paper,
  CircularProgress,
  Alert
} from '@mui/material';
import { convertCurrency } from '../../services/conversion';
//import { ConversionRequest } from '../../types/conversion';

import * as typesConversions from '../../types/conversion';
const ConversionRequest = typesConversions.ConversionRequest;

const CurrencyConverter: React.FC = ({ userId }) => {
  const [fromCurrency, setFromCurrency] = useState('USD');
  const [toCurrency, setToCurrency] = useState('BRL');
  const [amount, setAmount] = useState('');
  const [result, setResult] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const currencies = ['USD', 'BRL', 'EUR', 'JPY'];

  const handleConvert = async () => {
    if (!amount || isNaN(Number(amount))) {
      setError('Please enter a valid amount');
      return;
    }

    if (fromCurrency === toCurrency) {
      setError('Cannot convert between same currencies');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const request: ConversionRequest = {
        user_id: userId,
        from_currency: fromCurrency,
        to_currency: toCurrency,
        amount: parseFloat(amount)
      };

      const response = await convertCurrency(request);
      setResult(response.to_value);
    } catch (err) {
      setError('Failed to convert currency. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Paper elevation={3} sx={{ p: 4, maxWidth: 600, mx: 'auto' }}>
      <Typography variant="h5" gutterBottom>
        Currency Converter
      </Typography>

      {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}

      <Box sx={{ display: 'flex', gap: 2, mb: 2 }}>
        <TextField
          label="Amount"
          variant="outlined"
          type="number"
          fullWidth
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
      </Box>

      <Box sx={{ display: 'flex', gap: 2, mb: 3 }}>
        <FormControl fullWidth>
          <InputLabel>From</InputLabel>
          <Select
            value={fromCurrency}
            label="From"
            onChange={(e) => setFromCurrency(e.target.value as string)}
          >
            {currencies.map((currency) => (
              <MenuItem key={currency} value={currency}>{currency}</MenuItem>
            ))}
          </Select>
        </FormControl>

        <FormControl fullWidth>
          <InputLabel>To</InputLabel>
          <Select
            value={toCurrency}
            label="To"
            onChange={(e) => setToCurrency(e.target.value as string)}
          >
            {currencies.map((currency) => (
              <MenuItem key={currency} value={currency}>{currency}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Box>

      <Button
        variant="contained"
        onClick={handleConvert}
        disabled={loading}
        fullWidth
        size="large"
      >
        {loading ? <CircularProgress size={24} /> : 'Convert'}
      </Button>

      {result !== null && (
        <Box sx={{ mt: 3, textAlign: 'center' }}>
          <Typography variant="h6">
            {amount} {fromCurrency} = {result.toFixed(2)} {toCurrency}
          </Typography>
        </Box>
      )}
    </Paper>
  );
};

export default CurrencyConverter;
