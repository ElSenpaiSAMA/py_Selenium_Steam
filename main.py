#librerias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

opciones = Options()
opciones.add_experimental_option("detach", True)

crdriver = 'C:\\Users\\mnico\\chromedriver\\chromedriver.exe'

ser = Service(crdriver)

driver = webdriver.Chrome(service=ser, options=opciones)

driver.get('https://store.steampowered.com/?l=spanish')

buscar= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input#store_nav_search_term"))

)
buscar.send_keys("RETURNAL"+ Keys.RETURN)

seleccionar= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.responsive_search_name_combined"))

)
seleccionar.click()

seleccionar= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#ageYear"))
)
edad = Select(seleccionar)
edad.select_by_value("2003")

seleccionar= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#view_product_page_btn"))
)

seleccionar.click()

seleccionar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "game_description_snippet"))
)

info = seleccionar.text

with open('RETURNAL.txt', 'w', encoding='utf-8') as file:
    file.write(info)

driver.quit()

