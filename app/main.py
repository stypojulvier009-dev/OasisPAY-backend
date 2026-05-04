from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, etudiants, paiements, admin
from .utils.init_db import init_database

Base.metadata.create_all(bind=engine)

app = FastAPI(title="OasisPAY API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(etudiants.router)
app.include_router(paiements.router)
app.include_router(admin.router)

@app.on_event("startup")
async def startup_event():
    init_database()

@app.get("/")
def root():
    return {"message": "Bienvenue sur OasisPAY API"}

@app.get("/health")
def health():
    return {"status": "ok"}
