from dataclasses import dataclass


class Command:
    # Преобразование аргументов в датаклассе в лист
    def get_args(self) -> list[object]:
        values = [*self.__dict__.values()]
        result = []
        for value in values:
            if value != None:
                result.append(str(value))
        return result


@dataclass
class Add(Command):
    arg1: object = None
    arg2: object = None


@dataclass
class Subtract(Command):
    arg1: object = None
    arg2: object = None


@dataclass
class Multiply(Command):
    arg1: object = None
    arg2: object = None


@dataclass
class Divide(Command):
    arg1: object = None
    arg2: object = None


@dataclass
class Weather(Command):
    arg1: object = None
    arg2: object = None


@dataclass
class Meaning(Command):
    arg1: object = None


@dataclass
class Encrypt(Command):
    arg1: object = None
    arg2: object = None


@dataclass
class Decrypt(Command):
    arg1: object = None
    arg2: object = None
