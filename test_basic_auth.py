from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class BasicAuthTest(unittest.TestCase):
    # Ссылка на страницу с базовой авторизацией
    URL = "https://the-internet.herokuapp.com/basic_auth"

    def setUp(self):
        """
        Настройка: запуск браузера перед каждым тестом.
        """
        # Указываем путь к браузеру (например, Chrome)
        self.driver = webdriver.Chrome()

    def tearDown(self):
        """
        Закрытие браузера после выполнения теста.
        """
        self.driver.quit()

    def test_basic_auth_success(self):
        """
        Тест: Проверка успешной авторизации с правильными данными.
        """
        # Данные для успешной авторизации
        username = "admin"
        password = "admin"
        
        # Формируем URL с данными для авторизации
        auth_url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        
        # Открываем страницу с авторизацией
        self.driver.get(auth_url)

        # Ждем пару секунд, чтобы страница успела загрузиться
        time.sleep(2)
        
        # Получаем текст на странице, чтобы проверить успешную авторизацию
        success_text = self.driver.find_element(By.TAG_NAME, "p").text
        
        # Проверка, что появился текст об успешной авторизации
        self.assertIn("Congratulations", success_text, "Авторизация не прошла успешно.")

    def test_basic_auth_fail(self):
        """
        Тест: Проверка неудачной авторизации с неверными данными.
        """
        # Данные для неудачной авторизации
        username = "admAn"  # Неверный логин
        password = "admin"  # Правильный пароль
        
        # Формируем URL с неверным логином
        auth_url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        
        # Открываем страницу с авторизацией
        self.driver.get(auth_url)

        # Ждем пару секунд, чтобы страница успела загрузиться
        time.sleep(2)
        
        # Проверяем, что текст ошибки авторизации присутствует
        # В данном случае, просто проверим, что страница не содержит текста о успешной авторизации
        error_text = self.driver.find_element(By.TAG_NAME, "body").text
        
        self.assertNotIn("Congratulations", error_text, "Неудачная авторизация прошла успешно.")

if __name__ == "__main__":
    # Запуск всех тестов
    unittest.main()
