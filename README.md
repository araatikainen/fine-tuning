# fine-tuning course

This repository contains a Sentiment Analysis Application built with React (Vite), FastAPI, and Docker. The application allows users to analyze sentiment from a given text using different language models.

### Models

llama-3.3-70b-versatile (Groq API)

Fine-tuned DistilBert

[Model](https://huggingface.co/raati/distilbert_imdb_sentiment_analysis)
[Tokenizer](https://huggingface.co/raati/distilbert_imdb_sentiment_analysis_tokenizer)


### Setup & Installation

#### Prerequisites

Ensure you have the following installed:

- Docker & Docker Compose

- Node.js & npm (for local development)

Generate Groq API key from https://console.groq.com/keys
- Add API key to .env

#### Running with Docker

1. Clone the repository:

```bash
git clone https://github.com/your-repo/sentiment-analysis.git
cd sentiment-analysis
```

2. Build and start the application using Docker Compose:
```bash
docker-compose up --build
```
3. Open your browser and visit:

- Frontend: http://localhost:5173

- Backend: http://localhost:8000/docs#/default (Swagger UI for API)


or send directly requests to backend using curl

```bash
POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "This is funnnn", "model": "llama"}'
```


## Task 2 technical

Implementation can be found in 

```bash
backend/api/routes.py 
```
in endpoint /generate.

and 
```bash
backend/services/groq.py
```
in function translate_text().
