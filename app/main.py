from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth, products


app = FastAPI(title="Products API")

# Create the database tables when the application starts.
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(products.router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}
