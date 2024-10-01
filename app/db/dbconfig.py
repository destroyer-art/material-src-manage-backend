from pydantic import Field
from pydantic.v1 import BaseSettings


class DBConfig(BaseSettings):
    DATABASE_USER: str = Field("", env="DATABASE_USER")
    DATABASE_PASSWORD: str = Field("", env="DATABASE_PASSWORD")
    DATABASE_DBNAME: str = Field("", env="DATABASE_DBNAME")
    DATABASE_HOST: str = Field("", env="DATABASE_HOST")
    DATABASE_PORT: int = Field("", env="DATABASE_PORT")

    class Config:
        env_prefix = ""
        # case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = DBConfig()
