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

export interface TransactionHistoryProps {
  userId: string;
  className?: string;
}