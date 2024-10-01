from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.api.api_route import api_router
from app.db.dbconnect import Base, engine
import app.db.schemas

from app.utils.load_data import load_inventory_info

load_dotenv()


async def lifespan(app: FastAPI):
    print("DB connecting ...")
    Base.metadata.create_all(bind=engine)
    print("Server starting ...")
    load_inventory_info()
    print("Inventory data commited.")
    yield
    print("Server shutting down ...")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
