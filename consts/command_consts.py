from enum import StrEnum

# Enum, содержащий все доступные модули
class CommandsConsts(StrEnum):
    ADD = "--add"
    SUBTRACT = "--subtract"
    DIVIDE = "--divide"
    MULTIPLY = "--multiply"
    WEATHER = "--weather"
    MEANING = "--meaning"
    ENCRYPT = "--encrypt"
    DECRYPT = "--decrypt"
    HELP = "--help"
