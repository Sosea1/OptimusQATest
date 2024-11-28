from dataclasses import dataclass


# Датакласс для работы с данными, полученными от CommandClient
@dataclass
class Response:
    out: str = None
    err: str = None

    # Очищение вывода от лишних символов
    def clean_out(self) -> str:
        return self.out.replace("\r", "").replace("\n", "")
