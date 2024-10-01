from fastapi import APIRouter
from app.api.domain.inventory_api import inventory_api as inventory_route
from app.api.domain.preference_api import preference_api as preference_route

api_router = APIRouter()


@api_router.get("/health_check")
def health_check():
    return {"Message": "Server is Running"}


api_router.include_router(inventory_route, prefix="/inventory")
api_router.include_router(preference_route, prefix="/preference")
