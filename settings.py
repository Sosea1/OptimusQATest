from pydantic_settings import BaseSettings, SettingsConfigDict


# Класс для трансформации переменных из .env файла
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_nested_delimiter="."
    )

    file_path: str


base_settings = Settings()
