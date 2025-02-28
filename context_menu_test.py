from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Инициализация драйвера
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://the-internet.herokuapp.com/context_menu")
time.sleep(2)  # Ожидание загрузки страницы

# Найти область с контекстным меню
target_box = driver.find_element(By.ID, "hot-spot")

# Выполнить правый клик
actions = ActionChains(driver)
actions.context_click(target_box).perform()
time.sleep(1)

# Переключиться на alert и проверить текст
alert = driver.switch_to.alert
assert "You selected a context menu" in alert.text, "Ошибка: Текст alert не совпадает!"
print("Контекстное меню успешно вызвано!")

# Закрыть alert
alert.accept()
time.sleep(1)

driver.quit()
print("Тест успешно завершён!")
