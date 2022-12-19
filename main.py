# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import localtime, strftime
import requests
from threading import Thread
import json
from helper import *

def main():
    driver = setup()
    # jfrog_packets_to_download_nums = []
    # jfrog_simics_packets_to_download_names = []
    try:
        driver.find_element(by=By.PARTIAL_LINK_TEXT, value="").click()
        driver.find_element(by=By.PARTIAL_LINK_TEXT, value="").click()
        # dowload latest "" usually used packages:
        driver.find_elements(by=By.TAG_NAME, value="a")[-1].click()
        web_link_elements = driver.find_elements(by=By.TAG_NAME, value="a")
        for element in web_link_elements:
            element_url =  element.get_attribute("href")
            element_file_name = ret_element_file_name(element_url)
            if check_some_exe_package(element_file_name, 0000) or \
               check_some_exe_package(element_file_name, 0000) or \
               check_some_exe_package(element_file_name, 0000) or \
               element_file_name == "00000":
                print(f"{element_file_name:<45}{'starts download at':<30}{strftime('%H:%M:%S %t %d.%m.%Y', localtime())}")
                Thread(target=download_url, args=(element_url,)).start()
            if(element_file_name == "00000"):
                json_page = requests.get(element_url).json()
                for packet_num in jfrog_packets_to_download_nums :
                    jfrog_simics_packets_to_download_names.append(get_file_name_from_json_page(json_page, packet_num))
        jfrog_url = r"0000000"
        driver.get(jfrog_url)
        for packet_name in jfrog_simics_packets_to_download_names:
            print(f"{packet_name:<45}{'starts download at':<30}{strftime('%H:%M:%S %t %d.%m.%Y', localtime())}")
            Thread(target=download_url, args=(get_jfrog_some_file_url(driver, packet_name),)).start()
    except Exception as e:
        print("Error occured :")
        print(e)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()


