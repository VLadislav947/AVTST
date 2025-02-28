from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Функция для проверки авторизации через Digest
def test_digest_auth(username, password, expected_success):
    url = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(2)
    
    try:
        success_message = driver.find_element(By.TAG_NAME, "p").text
        if expected_success:
            assert "Congratulations!" in success_message, "Ошибка: Текст подтверждения не найден!"
            print(f"✅ Аутентификация прошла успешно для пользователя: {username}")
        else:
            print(f"❌ ОШИБКА! Неверные учетные данные: {username}")
    except Exception as e:
        if expected_success:
            print(f"❌ ОШИБКА при входе: {e}")
        else:
            print(f"✅ Ожидаемый отказ в доступе для: {username}")
    
    driver.quit()
    print("Тест завершён!\n")

# Тест с правильными учетными данными
test_digest_auth("admin", "admin", expected_success=True)

# Тест с неправильными учетными данными
test_digest_auth("adman", "admin", expected_success=False)
