from fastapi import APIRouter

from api.services.api_health.schemas import ResponseHealthStatus

router = APIRouter()


@router.get('/health', summary='Check health status of this service API')
async def service_health() -> ResponseHealthStatus:
    """
    **Check the health status of this service API**.\n
    This function is a FastAPI endpoint that handles a GET request to the '/health' route.
    It returns a ResponseHealthStatus object with the status set to "health".\n
    **Returns**:\n
        - ResponseHealthStatus: An object representing the health status of the service API.
    """
    return ResponseHealthStatus(status="health")
