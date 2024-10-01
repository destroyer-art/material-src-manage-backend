from fastapi import APIRouter, Query
from app.services import preferenceService
from app.models.preference import PreferenceModel

from typing import List

preference_api = APIRouter()


@preference_api.get("/")
async def get_preference_info(id: int = Query(default=None, ge=1)):
    result = await preferenceService.get_preference_data(id)
    return result


@preference_api.post("/")
async def get_prefer_match_data(preferences: List[PreferenceModel]):
    for prefer in preferences:
        await preferenceService.insert_data(prefer)
    return {"Status": "All data inserted"}
