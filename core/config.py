from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "EOI Validation API"
    DB_SERVER: str
    DB_NAME: str = Field(validation_alias="DB_DATABASE")
    DB_USER: str
    DB_PASSWORD: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    LOG_LEVEL: str = "INFO"
    ENV: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
        )


settings = Settings()