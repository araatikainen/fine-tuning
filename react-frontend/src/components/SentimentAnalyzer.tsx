import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, MenuItem, Select, FormControl, InputLabel } from '@mui/material';
import ResultDisplay from './ResultDisplay';

const SentimentAnalyzer: React.FC = () => {
    const [text, setText] = useState('');
    const [model, setModel] = useState('Custom Model');
    const [result, setResult] = useState<{ sentiment: string; confidence: number } | null>(null);

    const handleAnalyze = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/analyze', { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 
                    text,
                    model,
                })
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            setResult({
                sentiment: data.sentiment, 
                confidence: data.score * 100 // Convert score to percentage
            });
        } catch (error) {
            console.error('Error analyzing sentiment:', error);
        }
    };

    return (
        <div>
            <TextField
                label="Enter text"
                variant="outlined"
                fullWidth
                margin="normal"
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <FormControl fullWidth margin="normal">
                <InputLabel id="model-select-label">Select Model</InputLabel>
                <Select
                    labelId="model-select-label"
                    value={model}
                    label="Select Model"
                    onChange={(e) => setModel(e.target.value as string)}
                >
                    <MenuItem value="custom">Custom Model</MenuItem>
                    <MenuItem value="llama">Llama 3</MenuItem>
                </Select>
            </FormControl>
            <Button variant="contained" color="primary" onClick={handleAnalyze}>
                Analyze Sentiment
            </Button>
            {result && <ResultDisplay sentiment={result.sentiment} confidence={result.confidence} />}
        </div>
    );
};

export default SentimentAnalyzer;
