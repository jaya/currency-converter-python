import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import TransactionHistory from './TransactionHistory';
import * as api from '../../../services/conversion';

jest.mock('../../../services/conversion');

const mockTransactions = [
  {
    id: 1,
    user_id: 'test_user',
    from_currency: 'USD',
    to_currency: 'BRL',
    from_value: 100,
    to_value: 520,
    rate: 5.2,
    timestamp: '2023-06-15T12:00:00Z'
  }
];

describe('TransactionHistory', () => {
  it('displays loading state initially', () => {
    (api.getUserTransactions as jest.Mock).mockImplementation(
      () => new Promise(() => {})
    );
    
    render(<TransactionHistory userId="test_user" />);
    expect(screen.getByRole('progressbar')).toBeInTheDocument();
  });

  it('displays transactions after loading', async () => {
    (api.getUserTransactions as jest.Mock).mockResolvedValue(mockTransactions);
    
    render(<TransactionHistory userId="test_user" />);
    
    await waitFor(() => {
      expect(screen.getByText('USD')).toBeInTheDocument();
      expect(screen.getByText('BRL')).toBeInTheDocument();
      expect(screen.getByText('100.00 USD')).toBeInTheDocument();
      expect(screen.getByText('520.00 BRL')).toBeInTheDocument();
    });
  });

  it('displays error message when request fails', async () => {
    (api.getUserTransactions as jest.Mock).mockRejectedValue(
      new Error('Failed to fetch')
    );
    
    render(<TransactionHistory userId="test_user" />);
    
    await waitFor(() => {
      expect(screen.getByText('Failed to load transaction history')).toBeInTheDocument();
    });
  });
});