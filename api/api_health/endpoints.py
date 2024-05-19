from fastapi import APIRouter

from api.api_health.schemas import ResponseHealthStatus

router = APIRouter()


@router.get('/health', summary='Check health status of this service API')
async def service_health() -> ResponseHealthStatus:
    return ResponseHealthStatus(status="health")
