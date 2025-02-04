import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

interface ResultDisplayProps {
    sentiment: string;
    confidence: number;
}

const ResultDisplay: React.FC<ResultDisplayProps> = ({ sentiment, confidence }) => {
    return (
      <Card style={{ backgroundColor: '#f0f0f0', padding: '1rem', marginTop: '1rem' }}>
            <CardContent>
                <Typography variant="h6">Sentiment: {sentiment}</Typography>
                <Typography variant="body1">Confidence Score: {confidence.toFixed(2)}</Typography>
            </CardContent>
        </Card>
    );
};

export default ResultDisplay;
