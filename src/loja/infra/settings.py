from pydantic import BaseModel, BaseSettings
from src import PROJECT_ROOT_PATH

class PaymentSettings(BaseSettings):
    payment_username: str
    payment_password: str
    payment_token: str
    base_url: str


class Settings(BaseModel):
    payment: PaymentSettings


def get_settings(env_file=f"{PROJECT_ROOT_PATH}/.env") -> Settings:
    payment = PaymentSettings(_env_file=env_file)
    return Settings(payment=payment)

GLOBAL_CONFIG = get_settings()

