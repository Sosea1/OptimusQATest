import pytest
from utils.command_facade import CommandFacade


@pytest.fixture(scope="session")
def api() -> CommandFacade:
    return CommandFacade()
