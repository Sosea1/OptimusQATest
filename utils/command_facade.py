from steps.command_steps import CommandSteps
from utils.command_client import CommandClient


# Класс для обращения к компонентам системы - CommandClient и CommandSteps
class CommandFacade:
    def __init__(self) -> None:
        self.command_client = CommandClient()
        self.command_steps = CommandSteps(command_client=self.command_client)
