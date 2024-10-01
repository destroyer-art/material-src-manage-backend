import csv
from app.db.schemas import InventorySchema
from app.db.dbconnect import SessionLocal

db = SessionLocal()


def load_inventory_info():
    with open("data/inventory.csv", mode="r") as file:
        column_names = file.readline().strip().split(",")
        print(column_names)
        inventory_data = csv.DictReader(file, fieldnames=column_names)

        records = [
            {
                "product_number": data[column_names[0]],
                "material": data[column_names[1]],
                "form": data[column_names[2]],
                "choice": data[column_names[3]],
                "grade": data[column_names[4]],
                "finish": data[column_names[5]],
                "surface": data[column_names[6]],
                "quantity": int(data[column_names[7]]),
                "weight": float(data[column_names[8]]) if data[column_names[8]] else 0,
                "length": float(data[column_names[9]]) if data[column_names[9]] else 0,
                "width": float(data[column_names[10]]) if data[column_names[10]] else 0,
                "height": (
                    float(data[column_names[11]]) if data[column_names[11]] else 0
                ),
                "thickness": (
                    float(data[column_names[12]]) if data[column_names[12]] else 0
                ),
                "outer_diameter": (
                    float(data[column_names[13]]) if data[column_names[13]] else 0
                ),
                "wall_thickness": (
                    float(data[column_names[14]]) if data[column_names[14]] else 0
                ),
                "web_thickness": (
                    float(data[column_names[15]]) if data[column_names[15]] else 0
                ),
                "flange_thickness": (
                    float(data[column_names[16]]) if data[column_names[16]] else 0
                ),
                "certificates": data[column_names[17]],
                "location": data[column_names[18]],
            }
            for data in inventory_data
        ]

        db.bulk_insert_mappings(InventorySchema, records)
        db.commit()
