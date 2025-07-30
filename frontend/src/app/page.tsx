"use client";

import { useState } from "react";
import api from "@/lib/api";

const currencies = ["USD", "BRL", "EUR", "JPY"];

export default function Home() {
  const [userId, setUserId] = useState("");
  const [from, setFrom] = useState("USD");
  const [to, setTo] = useState("BRL");
  const [amount, setAmount] = useState(1);
  const [result, setResult] = useState<any>(null);
  const [history, setHistory] = useState<any[]>([]);

  const convert = async () => {
    try {
      const { data } = await api.post("/convert", {
        user_id: userId,
        from_currency: from,
        to_currency: to,
        amount: Number(amount),
      });
      setResult(data);
    } catch (err) {
      alert("Erro ao converter");
    }
  };

  const fetchHistory = async () => {
    const { data } = await api.get(`/transactions?user_id=${userId}`);
    setHistory(data);
  };

  return (
    <div className="max-w-xl mx-auto p-6 space-y-6">
      <h1 className="text-2xl font-bold">Conversor de Moedas</h1>

      <div className="space-y-2">
        <input
          type="text"
          placeholder="User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          className="w-full p-2 border rounded"
        />

        <div className="flex gap-2">
          <select value={from} onChange={(e) => setFrom(e.target.value)} className="p-2 border rounded w-full">
            {currencies.map((c) => <option key={c}>{c}</option>)}
          </select>

          <select value={to} onChange={(e) => setTo(e.target.value)} className="p-2 border rounded w-full">
            {currencies.map((c) => <option key={c}>{c}</option>)}
          </select>
        </div>

        <input
          type="number"
          value={amount}
          onChange={(e) => setAmount(parseFloat(e.target.value))}
          className="w-full p-2 border rounded"
        />

        <button onClick={convert} className="w-full bg-blue-500 text-white p-2 rounded">
          Converter
        </button>

        {result && (
          <div className="p-4 border rounded bg-gray-50 mt-2">
            <p><strong>Resultado:</strong> {result.converted_amount.toFixed(2)} {result.to_currency}</p>
            <p><strong>Taxa:</strong> {result.conversion_rate}</p>
          </div>
        )}

        <button onClick={fetchHistory} className="w-full bg-gray-600 text-white p-2 rounded mt-4">
          Ver Histórico
        </button>

        {history.length > 0 && (
          <div className="mt-4 space-y-2">
            <h2 className="text-lg font-semibold">Histórico</h2>
            {history.map((item, index) => (
              <div key={index} className="p-2 border rounded bg-white">
                <p>{item.amount} {item.from_currency} → {item.converted_amount.toFixed(2)} {item.to_currency}</p>
                <p className="text-sm text-gray-500">{new Date(item.timestamp).toLocaleString()}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
