from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Инициализация драйвера с webdriver-manager
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)  # Ожидание загрузки страницы

# Найти все чекбоксы
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# Проверка чекбоксов
for checkbox in checkboxes:
    initial_state = checkbox.is_selected()
    print(f"Чекбокс {'уже отмечен' if initial_state else 'не отмечен'}")
    
    # Кликнуть чекбокс (изменить его состояние)
    checkbox.click()
    time.sleep(1)
    
    # Проверить, изменилось ли состояние
    new_state = checkbox.is_selected()
    assert new_state != initial_state, "Ошибка: Чекбокс не изменил состояние"
    print(f"Чекбокс теперь {'отмечен' if new_state else 'не отмечен'}")

driver.quit()
print("Тест успешно завершён!")