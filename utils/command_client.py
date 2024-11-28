import subprocess
from models.response_model import Response
from settings import base_settings


# Класс для выполнения консольных команд
class CommandClient:
    def __init__(self):
        pass

    def run_command(
        self,
        file_exe=base_settings.file_path,
        command: str = None,
        args: list[str] = None,
    ):
        p = subprocess.Popen(
            [file_exe, command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        file = open("debug.txt", "w")
        out, err = p.communicate()
        file.write(str(out))

        # Исправление проблем с кодировкой при выводе
        try:
            out = out.decode("utf-8")
            err = err.decode("utf-8")
        except:
            out = out.decode("iso-8859-1")
            err = err.decode("iso-8859-1")
        return Response(out=out, err=err)
