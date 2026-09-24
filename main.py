from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from core.logger import app_logger
#from app.ui_routes import router as ui_router
from core.exceptions import APIException, api_exception_handler, request_validation_exception_handler
from core.logger import app_logger
from core.log_middleware import RequestLoggingMiddleware
    
from api.v1.routes.life_di_group_routes import router as group_router


app = FastAPI(
    title="EOI (Evidence of Insurability) API",
    root_path="/eoi-api",
    docs_url="/docs",
    json_url="/openapi.json",
    version="1.0.0"
)

app.add_middleware(RequestLoggingMiddleware)
app.mount("/static",StaticFiles(directory="app/static"), name="static")
#app.include_router(ui_router)
app.include_router(group_router)
app.add_exception_handler(APIException, api_exception_handler)
app.add_exception_handler(RequestValidationError,request_validation_exception_handler)
app_logger.success("EOI API has started")

@app.get("/healthcheck")
def health():
    return {
        "status": "EOI API is up and running",
    }       