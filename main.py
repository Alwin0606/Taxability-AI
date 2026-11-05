
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.tax import router as tax_router
from app.api.invoice import router as invoice_router
from app.api.classification import router as classification_router
from app.api.history import router as history_router
from app.api.gstr1 import router as gstr1_router

app = FastAPI(
    title="Taxability AI",
    description="AI-powered Indian Tax Analysis Platform",
    version="1.0.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(tax_router)
app.include_router(invoice_router)
app.include_router(classification_router)
app.include_router(history_router)
app.include_router(gstr1_router)


@app.get("/")
def root():
    return {
        "project": "Taxability AI",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "service": "Taxability AI Backend",
    }
