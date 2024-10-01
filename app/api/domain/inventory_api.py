from fastapi import APIRouter, Query

from app.services import inventoryService
from app.models.preference import PreferenceModel

inventory_api = APIRouter()


@inventory_api.get("/count")
async def get_inventory_data_count():
    result = await inventoryService.get_inventory_count()
    return result


@inventory_api.get("/")
async def get_inventory_data(
    page: int = Query(1, ge=1), perpage: int = Query(10, ge=5)
):
    result = await inventoryService.get_inventory_data(page=page, perpage=perpage)
    return result


@inventory_api.post("/match")
async def get_match_data(preference: PreferenceModel):
    result = await inventoryService.get_match_inventory(preference)
    return result
