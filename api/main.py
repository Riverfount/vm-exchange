from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api.api_health.routes import service_router
from api.config import settings
from api.exchange.routes import exchange_router
from api.middlewares.openapi import init_openapi

description = "This API offers a simple way to converte currencies from one base currency to another."


def init_app() -> FastAPI:
    app_ = FastAPI(
        title="VM Exchange API Service",
        description=description,
        version="0.1.0",
        terms_of_service="https://vmdesenvolvimento.com.br/#servicos",
        contact={
            "name": "VM Exchange Developer Team",
            "url": "https://vmdesenvolvimento.com.br/",
            "email": "vicente.marcal@vmdesenvolvimento.com.br",
        },
        servers=[{"url": settings.api.url_prefix}],
        docs_url="/api"
    )
    # init_gzip(app_)
    # init_cors(app_)
    init_openapi(app_)
    return app_


app = init_app()


# redirect home access to docs in /api
@app.get("/", include_in_schema=False)
async def redirect_to_api_docs():
    return RedirectResponse("/api")


app.include_router(service_router)
app.include_router(exchange_router)
