export interface ConversionRequest {
  user_id: string;
  from_currency: string;
  to_currency: string;
  amount: number;
}

export interface ConversionResult {
  originalAmount: number;
  convertedAmount: number;
  fromCurrency: string;
  toCurrency: string;
  rate: number;
  timestamp?: string;
}