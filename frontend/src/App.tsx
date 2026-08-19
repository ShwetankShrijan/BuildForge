import { useEffect, useState } from "react";

type Case = {
  id: number;
  brand: string;
  model: string;
  form_factor: string;
}; // we do this because tsx doesnt know the data types used below

function App() {
    const [cases, setCases] = useState<Case[]>([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/cases")
            .then(response => response.json())
            .then(data => {
                setCases(data);
            });
    }, []);

    return (
        <div>
            <h1>BuildForge</h1>
            <h3>Price Analyzer and Compatibility Checker</h3>
            {cases.map((pcCase) => (
                <p key={pcCase.id}>
                    {pcCase.brand} {pcCase.model}
                </p>
            ))}
        </div>
    );
}

export default App; 