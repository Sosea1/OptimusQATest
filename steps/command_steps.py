from consts.command_consts import CommandsConsts
from models.command_models import (
    Add,
    Decrypt,
    Divide,
    Encrypt,
    Help,
    Meaning,
    Multiply,
    Subtract,
    Weather,
)
import allure
from models.response_model import Response
from utils.command_client import CommandClient


class CommandSteps:
    def __init__(self, command_client) -> None:
        self.command_client = command_client

    @allure.step("Сложение")
    def add(self, model: Add) -> Response:
        return self.command_client.run_command(
            command=CommandsConsts.ADD, args=model.get_args()
        )

    @allure.step("Вычитание")
    def subtract(self, model: Subtract) -> Response:
        return self.command_client.run_command(
            command=CommandsConsts.SUBTRACT, args=model.get_args()
        )

    @allure.step("Деление")
    def divide(self, model: Divide) -> Response:
        return self.command_client.run_command(
            command=CommandsConsts.DIVIDE, args=model.get_args()
        )

    @allure.step("Умножение")
    def multiply(self, model: Multiply) -> Response:
        return self.command_client.run_command(
            command=CommandsConsts.MULTIPLY, args=model.get_args()
        )

    @allure.step("Погода")
    def weather(self, model: Weather) -> Response:
        return self.command_client.run_command(
            command=CommandsConsts.WEATHER, args=model.get_args()
        )

    @allure.step("Смысл")
    def meaning(self, model: Meaning) -> Response:
        return self.command_client.run_command(
            command=CommandsConsts.MEANING, args=model.get_args()
        )

    @allure.step("Шифрование")
    def encrypt(self, model: Encrypt) -> Response:
        return self.command_client.run_command(
            command=CommandsConsts.ENCRYPT, args=model.get_args()
        )

    @allure.step("Дешифрование")
    def decrypt(self, model: Decrypt) -> Response:
        return self.command_client.run_command(
            command=CommandsConsts.DECRYPT, args=model.get_args()
        )
