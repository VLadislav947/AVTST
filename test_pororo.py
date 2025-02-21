from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class AddRemoveElementsTest(unittest.TestCase):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def setUp(self):
        # Инициализация WebDriver и открытие страницы
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)

    def tearDown(self):
        # Закрытие браузера после каждого теста
        self.driver.quit()

    def test_add_single_element(self):
        # Нахождение кнопки 'Add Element' и клик по ней
        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add Element']")
        add_button.click()
        
        # Проверка, что появилась кнопка 'Delete'
        delete_button = self.driver.find_element(By.CLASS_NAME, "added-manually")
        self.assertTrue(delete_button.is_displayed(), "Кнопка 'Delete' не появилась")

    def test_add_multiple_elements(self):
        # Нахождение кнопки 'Add Element'
        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add Element']")
        
        # Добавляем 5 кнопок 'Delete'
        for _ in range(5):
            add_button.click()
        
        # Проверка, что количество кнопок 'Delete' равно 5
        delete_buttons = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        self.assertEqual(len(delete_buttons), 5, "Количество кнопок 'Delete' неверное")

    def test_remove_single_element(self):
        # Добавляем один элемент
        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add Element']")
        add_button.click()
        
        # Удаляем элемент
        delete_button = self.driver.find_element(By.CLASS_NAME, "added-manually")
        delete_button.click()
        
        # Проверяем, что кнопка 'Delete' исчезла
        delete_buttons = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        self.assertTrue(len(delete_buttons) == 0, "Кнопка 'Delete' не была удалена")

    def test_remove_multiple_elements(self):
        # Добавляем 3 элемента
        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add Element']")
        for _ in range(3):
            add_button.click()
        
        # Удаляем все кнопки 'Delete' одну за другой
        delete_buttons = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        while delete_buttons:
            delete_buttons[0].click()
            delete_buttons = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        
        # Проверяем, что кнопки удалились
        self.assertTrue(len(delete_buttons) == 0, "Остались кнопки 'Delete' после удаления")

if __name__ == "__main__":
    unittest.main()
