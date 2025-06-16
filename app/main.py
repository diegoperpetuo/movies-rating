from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as ratings_router
from app.auth import router as auth_router

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os headers
    expose_headers=["*"]
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(ratings_router, prefix="/api/ratings", tags=["ratings"])
