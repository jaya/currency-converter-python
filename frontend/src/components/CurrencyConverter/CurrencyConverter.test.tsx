import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import CurrencyConverter from './CurrencyConverter';
import * as api from '../../../services/conversion';

jest.mock('../../../services/conversion');

describe('CurrencyConverter', () => {
  it('should convert currency successfully', async () => {
    const mockConvert = api.convertCurrency as jest.Mock;
    mockConvert.mockResolvedValueOnce({
      to_value: 525.32
    });

    render(<CurrencyConverter />);
    
    fireEvent.change(screen.getByLabelText('Amount'), {
      target: { value: '100' }
    });
    
    fireEvent.click(screen.getByText('Convert'));
    
    await waitFor(() => {
      expect(screen.getByText('100 USD = 525.32 BRL')).toBeInTheDocument();
    });
  });
});