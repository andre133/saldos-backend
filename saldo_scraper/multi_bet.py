from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def extrair_saldo_multi(url, login, senha):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(2)
        driver.find_element(By.NAME, "login").send_keys(login)
        driver.find_element(By.NAME, "password").send_keys(senha)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(5)
        saldo_element = driver.find_element(By.CSS_SELECTOR, ".valor-saldo")
        saldo = saldo_element.text
        return saldo
    except Exception as e:
        return f"Erro: {str(e)}"
    finally:
        driver.quit()
