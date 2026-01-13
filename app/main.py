from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import auth, users, items

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="A FastAPI backend application with modern Python web development features"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)


@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint."""
    return {
        "message": "Welcome to FastAPI Backend",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
