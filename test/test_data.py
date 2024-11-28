import platform
import pytest

_platform = platform.system()


class TestData:
    def __init__(self):
        if _platform == "Windows":
            self._class = WindowsTestData()
        elif _platform == "Linux":
            self._class = LinuxTestData()
        else:
            raise SystemError("The platform is not Windows or Linux")

        self.add_params = self._class.add_params
        self.subtract_params = self._class.subtract_params

        self.divide_params = (
            pytest.param(5, None, "Missing arguments"),
            pytest.param(5, 0, "Divide by zero error encountered"),
        )
        self.multiply_params = (
            pytest.param(5, None, "Missing arguments"),
            pytest.param(-1, 6, "-6"),
        )
        self.weather_params = (
            pytest.param(5, None, "Missing arguments"),
            pytest.param("10001", None, "Incorrect input"),
            pytest.param("Mosco", None, "Current weather in Moscow:"),
            pytest.param("g", None, "Incorrect input"),
            pytest.param("London", 123456789098765432, "Incorrect input"),
        )
        self.meaning_params = (
            pytest.param(None, "Missing arguments"),
            pytest.param(1.55, "42"),
            pytest.param(0, "42"),
            pytest.param(100, "42"),
            pytest.param("-0", "Incorrect input"),
        )
        self.encrypt_params = (pytest.param(5, None, "Missing arguments"),)
        self.decrypt_params = (pytest.param(5, None, "Missing arguments"),)
        self.encrypt_decrypt_params = (pytest.param("encrypted", "key", "encrypted"),)


class WindowsTestData(TestData):
    def __init__(self):
        self.add_params = (
            pytest.param(5, None, "Missing arguments"),
            pytest.param(0, 0, "0"),
        )
        self.subtract_params = (pytest.param(5, None, "Missing arguments"),)


class LinuxTestData(TestData):
    def __init__(self):
        self.add_params = (pytest.param(5, None, "Missing arguments"),)
        self.subtract_params = (
            pytest.param(5, None, "Missing arguments"),
            pytest.param(0, 0, "0"),
        )
