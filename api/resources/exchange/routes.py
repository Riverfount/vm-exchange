from fastapi import APIRouter

from api.config import settings
from api.resources.exchange.endpoints import router

exchange_router = APIRouter()
exchange_router.include_router(router, prefix=settings.api.url_prefix, tags=['Exchange'])
