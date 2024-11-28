import pytest
import allure
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
from models.response_model import Response
from test.test_data import TestData
from pytest_check import check


@pytest.mark.command
class TestCommands:
    @allure.title("Проверка модуля Add")
    @pytest.mark.add
    @pytest.mark.parametrize("arg1, arg2, expected_out", TestData().add_params)
    def test_add_command(self, api, arg1, arg2, expected_out):
        with allure.step(
            f"Проверка с аргументами {arg1} и {arg2}. Ожидаемый результат: {expected_out}"
        ):
            with check:

                response = api.command_steps.add(Add(arg1=arg1, arg2=arg2))
                assert response.clean_out() == expected_out

    @allure.title("Проверка модуля Subtract")
    @pytest.mark.subtract
    @pytest.mark.parametrize("arg1, arg2, expected_out", TestData().subtract_params)
    def test_subtract_command(self, api, arg1, arg2, expected_out):
        with allure.step(
            f"Проверка с аргументами {arg1} и {arg2}. Ожидаемый результат: {expected_out}"
        ):
            with check:

                response = api.command_steps.subtract(Subtract(arg1=arg1, arg2=arg2))
                assert response.clean_out() == expected_out

    @allure.title("Проверка модуля Divide")
    @pytest.mark.divide
    @pytest.mark.parametrize("arg1, arg2, expected_out", TestData().divide_params)
    def test_divide_command(self, api, arg1, arg2, expected_out):
        with allure.step(
            f"Проверка с аргументами {arg1} и {arg2}. Ожидаемый результат: {expected_out}"
        ):
            with check:

                response = api.command_steps.divide(Divide(arg1=arg1, arg2=arg2))
                assert response.clean_out() == expected_out

    @allure.title("Проверка модуля Multiply")
    @pytest.mark.multiply
    @pytest.mark.parametrize("arg1, arg2, expected_out", TestData().multiply_params)
    def test_multiply_command(self, api, arg1, arg2, expected_out):
        with allure.step(
            f"Проверка с аргументами {arg1} и {arg2}. Ожидаемый результат: {expected_out}"
        ):
            with check:

                response = api.command_steps.multiply(Multiply(arg1=arg1, arg2=arg2))
                assert response.clean_out() == expected_out

    @allure.title("Проверка модуля Weather")
    @pytest.mark.weather
    @pytest.mark.parametrize("arg1, arg2, expected_out", TestData().weather_params)
    def test_weather_command(self, api, arg1, arg2, expected_out):
        with allure.step(
            f"Проверка с аргументами {arg1} и {arg2}. Ожидаемый результат: {expected_out}"
        ):
            with check:

                response = api.command_steps.weather(Weather(arg1=arg1, arg2=arg2))
                assert response.clean_out().startswith(expected_out)

    @allure.title("Проверка модуля Meaning")
    @pytest.mark.meaning
    @pytest.mark.parametrize("arg1, expected_out", TestData().meaning_params)
    def test_meaning_command(self, api, arg1, expected_out):
        with allure.step(
            f"Проверка с аргументом {arg1}. Ожидаемый результат: {expected_out}"
        ):
            with check:

                response = api.command_steps.meaning(Meaning(arg1=arg1))
                assert response.clean_out() == expected_out

    @allure.title("Проверка модуля Encrypt")
    @pytest.mark.encrypt
    @pytest.mark.parametrize("arg1, arg2, expected_out", TestData().encrypt_params)
    def test_encrypt_command(self, api, arg1, arg2, expected_out):
        with allure.step(
            f"Проверка с аргументами {arg1} и {arg2}. Ожидаемый результат: {expected_out}"
        ):
            with check:
                response = api.command_steps.encrypt(Encrypt(arg1=arg1, arg2=arg2))
                assert response.clean_out() == expected_out

    @allure.title("Проверка модуля Decrypt")
    @pytest.mark.decrypt
    @pytest.mark.parametrize("arg1, arg2, expected_out", TestData().decrypt_params)
    def test_decrypt_command(self, api, arg1, arg2, expected_out):
        with allure.step(
            f"Проверка с аргументами {arg1} и {arg2}. Ожидаемый результат: {expected_out}"
        ):
            with check:

                response = api.command_steps.decrypt(Decrypt(arg1=arg1, arg2=arg2))
                assert response.clean_out() == expected_out

    @allure.title("Проверка работы вместе модуля Encrypt с Decrypt")
    @pytest.mark.encrypt
    @pytest.mark.decrypt
    @pytest.mark.parametrize(
        "arg1, key, expected_out", TestData().encrypt_decrypt_params
    )
    def test_enctypt_decrypt_command(self, api, arg1, key, expected_out):
        with allure.step(
            f"Проверка с аргументами {arg1} и {key}. Ожидаемый результат: {expected_out}"
        ):
            with check:

                response_encrypt = api.command_steps.encrypt(
                    Decrypt(arg1=arg1, arg2=key)
                )
                response_decrypt = api.command_steps.decrypt(
                    Decrypt(arg1=response_encrypt.clean_out(), arg2=key)
                )
                assert response_decrypt.clean_out() == expected_out

    # проверить загрузку RAM не получилось

    # @allure.title("Проверка ОЗУ в модуле Meaning")
    # @pytest.mark.meaning
    # @pytest.mark.parametrize(
    #     "arg1, expected_out", TestData().meaning_params_ram
    # )
    # def test_meaning_ram_command(
    #     self,
    #     api,
    #     arg1,
    #     expected_out
    # ):
    #     with allure.step(f"Проверка с аргументом {arg1}. Ожидаемый результат: {expected_out}"):
    #         with check:

    #             mythread = MeaningClass(api.command_steps.meaning, Meaning(arg1=arg1))
    #             mythread.start()
    #             start_memory_info = psutil.virtual_memory()
    #             file = open("debug.txt","a")
    #             file.write('\n')
    #             file.write('до = '+str(round(start_memory_info.used / (1024 * 1024))))
    #             max_memory = start_memory_info
    #             # response = api.command_steps.meaning(Meaning(arg1=arg1))
    #             while(1):
    #                 memory_info = psutil.virtual_memory()
    #                 if memory_info > max_memory:
    #                     max_memory = memory_info
    #                 file.write('\n')
    #                 file.write(str(mythread.isShutdown()))
    #                 if mythread.isShutdown():
    #                     assert mythread.results.clean_out() == expected_out
    #                     file.write('\n')
    #                     file.write('после = '+str(round(memory_info.used / (1024 * 1024))))
    #                     file.close()
    #                     break
