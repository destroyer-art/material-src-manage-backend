from app.db.dbconnect import SessionLocal
from app.db.schemas import PreferenceSchema
from app.models.preference import PreferenceModel

dbHandler = SessionLocal()


async def get_preference_data(id: None | int):
    if id is None:
        return dbHandler.query(PreferenceSchema).all()
    else:
        return (
            dbHandler.query(PreferenceSchema).filter(PreferenceSchema.id == id).first()
        )


async def insert_data(prefer: PreferenceModel):
    new_preference = PreferenceSchema(
        material=prefer.material,
        form=prefer.form,
        grade=prefer.grade,
        choice=prefer.choice,
        min_width=prefer.min_width,
        max_width=prefer.max_width,
        min_thickness=prefer.min_thickness,
        max_thickness=prefer.max_thickness,
    )
    dbHandler.add(new_preference)
    dbHandler.commit()
