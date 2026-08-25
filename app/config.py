from pydantic_settings import BaseSettings, SettingsConfigDict

APPLICATION_NAME = "Secure DevSecOps Platform API"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env") 
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

settings = Settings()
