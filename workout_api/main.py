from fastapi import FastAPI, HTTPException, Request, status
from workout_api.routers import api_router
from sqlalchemy.exc import IntegrityError
import logging

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)

@app.exception_handler(IntegrityError)
async def integrity_exception_handler(request: Request, exc: IntegrityError):
    logging.error(exc)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail='Falha interna, se persistir contatar suporte.'
    )