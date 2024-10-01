from app.db.dbconnect import SessionLocal
from app.db.schemas import InventorySchema
from app.models.preference import PreferenceModel
from sqlalchemy import and_

dbHandler = SessionLocal()


async def get_inventory_count():
    return dbHandler.query(InventorySchema).count()


async def get_inventory_data(page: int, perpage: int):
    offset = (page - 1) * perpage
    return (
        dbHandler.query(InventorySchema)
        .order_by(InventorySchema.weight.desc())
        .offset(offset)
        .limit(perpage)
        .all()
    )


async def get_match_inventory(preference: PreferenceModel):
    query = dbHandler.query(InventorySchema)

    filter_conditions = []

    conditions = [
        ("material", InventorySchema.material, "=="),
        ("form", InventorySchema.form, "=="),
        ("grade", InventorySchema.grade, "=="),
        ("choice", InventorySchema.choice, "=="),
        ("min_width", InventorySchema.width, ">="),
        ("max_width", InventorySchema.width, "<="),
        ("min_thickness", InventorySchema.thickness, ">="),
        ("max_thickness", InventorySchema.thickness, "<="),
    ]

    for attr, schema_field, operator in conditions:
        value = getattr(preference, attr)
        if value is not None and value is not '':
            if operator == "==":
                filter_conditions.append(schema_field == value)
            elif operator == ">=":
                filter_conditions.append(schema_field >= value)
            elif operator == "<=":
                filter_conditions.append(schema_field <= value)

    if filter_conditions:
        query = query.filter(and_(*filter_conditions))

    result = query.order_by(InventorySchema.weight.desc()).all()

    return result
