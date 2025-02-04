from dotenv import load_dotenv
from fastapi import FastAPI
from api.routes import router
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# Allow frontend to access backend (replace with the actual URL of your React app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Modify as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Backend is running"}


