from fastapi import APIRouter

from api.api_health.endpoints import router
from api.config import settings

service_router = APIRouter()
service_router.include_router(router, prefix=settings.api.url_prefix, tags=['Public endpoints'])
