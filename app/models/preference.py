from pydantic import BaseModel
from typing import Optional


class PreferenceModel(BaseModel):
    material: Optional[str] = None
    form: Optional[str] = None
    grade: Optional[str] = None
    choice: Optional[str] = None
    min_width: Optional[float] = None
    max_width: Optional[float] = None
    min_thickness: Optional[float] = None
    max_thickness: Optional[float] = None
