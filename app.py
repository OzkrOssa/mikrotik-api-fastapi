from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.v1.routes.pppRoutes import pppRouter


app = FastAPI()

app.include_router(pppRouter, prefix="/api/v1/mikrotik",)

@app.get("/")
def home():
    return RedirectResponse(url="/docs/")

