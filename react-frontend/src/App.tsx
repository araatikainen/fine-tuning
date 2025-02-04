import React from 'react';
import { Container, Typography } from '@mui/material';
import SentimentAnalyzer from './components/SentimentAnalyzer';

const App: React.FC = () => {
    return (
        <div className="container">
            <Typography variant="h4" gutterBottom>
                Sentiment Analysis Tool
            </Typography>
            <SentimentAnalyzer />
        </div>
    );
};

export default App;
