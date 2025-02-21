from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Инициализация драйвера
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Запуск в фоновом режиме

driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/challenging_dom")

time.sleep(2)  # Небольшая пауза для загрузки страницы

# Нажатие на кнопку с изменяющимся текстом
button = driver.find_element(By.CSS_SELECTOR, ".button")
button.click()

# Проверка наличия таблицы
try:
    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    print(f"Таблица найдена, количество строк (включая заголовки): {len(rows)}")
except:
    print("Таблица не найдена!")
    driver.quit()
    exit(1)

# Проверка данных в таблице
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    if columns:
        print([col.text for col in columns])  # Вывод данных в консоль
        assert len(columns) == 6, "Ошибка: в таблице должно быть 6 колонок"

print("Тест успешно выполнен!")
driver.quit()