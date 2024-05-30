from fastapi import FastAPI

from api.config import settings


def init_openapi(app: FastAPI):
    def custom_openapi():
        # generate openapi by native fastapi function
        if not app.openapi_schema:
            app.openapi_schema = app.native_openapi()

        # remove paths prefix
        existing_paths = list(app.openapi_schema['paths'].keys())
        for existing_path in existing_paths:
            new_path = existing_path.replace(settings.api.url_prefix, '')
            app.openapi_schema['paths'][new_path] = app.openapi_schema['paths'].pop(existing_path)
        return app.openapi_schema

    # reassign fastapi app functions for custom openapi
    app.native_openapi = app.openapi
    app.openapi = custom_openapi
