from fastapi import FastAPI,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import RedirectResponse

from src.v1.routes.pppRoutes import pppRouter


# API_KEYS=["74df26a602f02d84bf50d04634fa12839cd21239d1888a34d19a6da1a4e1e79c"]

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def api_key_auth(api_key: str = Depends(oauth2_scheme)):
#     if api_key not in API_KEYS:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Forbidden"
#         )

app = FastAPI()

app.include_router(pppRouter, prefix="/api/v1/mikrotik",tags=["Mikrotik PPP"])

# @app.get("/",tags=["Documentation"])
# def doc():
#     return RedirectResponse(url="/docs/")

