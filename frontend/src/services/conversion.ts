import api from './api';

export interface ConversionRequest {
  user_id: string;
  from_currency: string;
  to_currency: string;
  amount: number;
}

export interface ConversionResponse {
  transaction_id: number;
  user_id: string;
  from_currency: string;
  to_currency: string;
  from_value: number;
  to_value: number;
  rate: number;
  timestamp?: string;
}

export interface Transaction {
  id: number;
  user_id: string;
  from_currency: string;
  to_currency: string;
  from_value: number;
  to_value: number;
  rate: number;
  timestamp: string;
}

export const convertCurrency = async (data: ConversionRequest): Promise<ConversionResponse> => {
  const response = await api.post('/conversion/convert', data);
  return response.data;
};

export const getUserTransactions = async (userId: string): Promise<Transaction[]> => {
  const response = await api.get(`/transactions/?user_id=${userId}`);
  return response.data;
};