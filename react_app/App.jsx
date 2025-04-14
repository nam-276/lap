import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [input, setInput] = useState({});
  const [result, setResult] = useState(null);

  const handleChange = e => setInput({ ...input, [e.target.name]: e.target.value });

  const handleSubmit = async () => {
    const res = await axios.post("http://localhost:8000/predict", input);
    setResult(res.data.churn_prediction ? "CÓ" : "KHÔNG");
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Dự đoán khách hàng rời bỏ</h1>
      <input className="border p-2 w-full mb-2" name="MonthlyCharges" placeholder="Monthly Charges" onChange={handleChange} />
      {/* Thêm input khác tương ứng */}
      <button onClick={handleSubmit} className="bg-blue-500 text-white px-4 py-2">Dự đoán</button>
      {result && <p className="mt-4 text-xl">Khách hàng rời bỏ: <strong>{result}</strong></p>}
    </div>
  );
}

export default App;
