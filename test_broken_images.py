from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import unittest

class TestBrokenImages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Используем Chrome WebDriver
        self.driver.get("https://the-internet.herokuapp.com/broken_images")

    def test_broken_images(self):
        driver = self.driver
        images = driver.find_elements(By.TAG_NAME, "img")  # Находим все <img> на странице

        broken_images = []  # Список для битых изображений

        for img in images:
            src = img.get_attribute("src")  # Получаем ссылку на изображение
            if src:
                response = requests.get(src)  # Делаем HTTP-запрос
                if response.status_code != 200:  # Если не 200, значит изображение битое
                    broken_images.append(src)

        # Проверяем, есть ли битые изображения
        self.assertEqual(len(broken_images), 0, f"Битые изображения найдены: {broken_images}")

    def tearDown(self):
        self.driver.quit()  # Закрываем браузер после теста

if __name__ == "__main__":
    unittest.main()
print("Тест завершён!")
