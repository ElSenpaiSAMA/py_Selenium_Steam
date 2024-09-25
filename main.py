from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

crdriver = 'C:\\Users\\mnico\\chromedriver\\chromedriver.exe'
nom_juego = "Baldur´s Gate 3"
anio = 2003

def configurar_driver(crdriver):
    opciones = Options()
    opciones.add_experimental_option("detach", True)
    ser = Service(crdriver)
    driver = webdriver.Chrome(service=ser, options=opciones)
    return driver

def abrir_pag(driver, url):
    driver.get(url)

def buscar_juego(driver, nombre_juego):
    buscar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#store_nav_search_term"))
    )
    buscar.send_keys(nombre_juego + Keys.RETURN)

def juego(driver):
    seleccionar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.responsive_search_name_combined"))
    )
    seleccionar.click()

def sel_edad(driver, year):
    seleccionar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ageYear"))
    )
    edad = Select(seleccionar)
    edad.select_by_value(str(year))

def pag_producto(driver):
    seleccionar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#view_product_page_btn"))
    )
    seleccionar.click()

def obtener(driver):
    seleccionar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "game_description_snippet"))
    )
    return seleccionar.text

def descripcion(info, filename='juego.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(info)

def ejecutar(nom_juego, crdriver_path, anio):
    driver = configurar_driver(crdriver_path)
    try:
        abrir_pag(driver, 'https://store.steampowered.com/?l=spanish')
        buscar_juego(driver, nom_juego)
        juego(driver)
        sel_edad(driver, anio)
        pag_producto(driver)
        des = obtener(driver)
        descripcion(des)
    finally:
        driver.quit()

ejecutar(nom_juego, crdriver, anio)

