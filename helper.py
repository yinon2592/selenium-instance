from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def setup():
    options = Options()
    options.add_argument("start-maximized")
    # options.add_argument("--headless")
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # if no chrome driver is installed use this (slower performence) :
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    chromedriver_path = r"<path to compitable chrome driver>"
    driver = webdriver.Chrome(service=Service(executable_path=chromedriver_path), options=options)
    driver.implicitly_wait(15) # wait for element till 15 sec
    some_path = r"<some_path>"
    driver.get(some_path)
    return driver
def ret_element_file_name(t_element_url):
    return t_element_url[t_element_url.rfind("/") + 1:]

def click_by_partial_link_text(t_driver, button):
    t_driver.create_web_element(t_driver.find_element(by=By.PARTIAL_LINK_TEXT, value=button).id).click()

def check_some_exe_package(element_file_name, package_num):
    return element_file_name.startswith(f"some start{package_num}")  and element_file_name.endswith(".exe")

def get_jfrog_some_file_url(t_driver, t_element_file_name):
    return t_driver.find_element(By.CSS_SELECTOR, \
    f'a[href="some copitable url link"]').get_attribute("href")

def get_file_name_from_json_page(json_page, package_num):
    # use json web page content as dict
    pass

def download_url(t_element_url):
    file_name = ret_element_file_name(t_element_url)
    r = requests.get(t_element_url)
    with open(file_name, 'wb') as f:
        f.write(r.content)

last_link_text = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "a")))[-1].text
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, last_link_text))).click()

