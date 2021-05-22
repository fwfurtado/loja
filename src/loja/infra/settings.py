from pydantic import BaseModel, BaseSettings, PostgresDsn
from src import PROJECT_ROOT_PATH


class PaymentSettings(BaseSettings):
    payment_username: str
    payment_password: str
    payment_token: str
    base_url: str


class DatabaseSettings(BaseSettings):
    database_host: str
    database_port: int
    database_user: str
    database_password: str
    database_name: str

    @property
    def dsn(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            host=self.database_host,
            port=str(self.database_port),
            user=self.database_user,
            password=self.database_password,
            path="/" + self.database_name,
        )


class Settings(BaseModel):
    payment: PaymentSettings
    database_settings: DatabaseSettings


def get_settings(env_file=f"{PROJECT_ROOT_PATH}/.env") -> Settings:
    payment = PaymentSettings(_env_file=env_file)
    db = DatabaseSettings(_env_file=env_file)
    return Settings(payment=payment, database_settings=db)


GLOBAL_CONFIG = get_settings()
