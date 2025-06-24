from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='src/.env',env_file_encoding='utf-8')
    database_host: str
    database_password: str
    database_port: str
    database_username: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expires_minutes: int


settings = Settings(_env_file='src/.env')
