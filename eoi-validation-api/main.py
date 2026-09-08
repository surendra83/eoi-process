from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.logger import app_logger
#from app.ui_routes import router as ui_router

from api.v1.routes.life_di_group_routes import router as group_router


app = FastAPI(
    title="EOI (Evidence of Insurability) API",
    version="1.0.0"
)

app.mount("/static",StaticFiles(directory="app/static"), name="static")
#app.include_router(ui_router)
app.include_router(group_router)
app_logger.success("EOI API has started")

@app.get("/healthcheck")
def health():
    return {
        "status": "EOI API is up and running",
    }       