import requests
import settings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_profile(ads_id):
    open_url = f"{settings.ads_url}/api/v1/browser/start?user_id=" + ads_id
    resp = requests.get(open_url).json()
    if resp["code"] != 0:
        print(f'Ошибка в профиле с id {ads_id}')
        print(resp["msg"])
        print("please check ads_id")
    return resp


def close_profile(ads_id):
    close_url = f"{settings.ads_url}/api/v1/browser/stop?user_id=" + ads_id
    resp = requests.get(close_url).json()
    if resp["code"] != 0:
        print(f'Ошибка в профиле с id {ads_id}')
        print(resp["msg"])
        print("please check ads_id")
    return resp


def configure_profile(response_open):
    chrome_driver = response_open["data"]["webdriver"]
    service = Service(executable_path=chrome_driver)
    chrome_options = Options()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_extension('metamask-chrome-11.13.1.crx')
    chrome_options.add_experimental_option("debuggerAddress", response_open["data"]["ws"]["selenium"])
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def get_last_window(driver):
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])


def check_element_exist(driver, xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
        return True
    except NoSuchElementException:
        return False


def click_element(driver, xpath, sleep_time):
    while True:
        if check_element_exist(driver, xpath) is True:
            driver.find_element(by=By.XPATH, value=xpath).click()
            time.sleep(sleep_time)
            return
        else:
            time.sleep(5)


def send_element_keys(driver, xpath, keys, sleep_time):
    while True:
        if check_element_exist(driver, xpath) is True:
            driver.find_element(by=By.XPATH, value=xpath).send_keys(keys)
            time.sleep(sleep_time)
            return
        else:
            time.sleep(5)


def close_all_tabs(driver):
    try:
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            driver.close()
    except:
        pass


def find_window_by_url(driver, url):
    all_windows = driver.window_handles
    # Ищем вкладку по url
    for i in range(len(all_windows)):
        driver.switch_to.window(driver.window_handles[i])
        if url in driver.current_url:
            return i
    return False


def click_quest_button(driver, button_text, sleep_time):
    try:
        #button = driver.find_element(by=By.XPATH, value=xpath)
        #button.click()
        #driver.execute_script("arguments[0].click();", button)
        button = WebDriverWait(driver, sleep_time).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()='{button_text}']")))
        button.click()
        time.sleep(sleep_time)
        return
    except:
        return


def check_quest_button_exist(driver, button_text):
    try:
        driver.find_element(by=By.XPATH, value=f"//p[text()='{button_text}']")
        return True
    except:
        return False


def check_label_exist(driver, text):
    try:
        elem = driver.find_element(by=By.XPATH, value=f"//p[text()='{text}']")
        if 'body text-3xs text-content-primary' == elem.get_attribute("class"):
            return False
        return True
    except:
        return False


def click_continue(driver, sleep_time):
    try:
        # button = driver.find_element(by=By.XPATH, value=xpath)
        # button.click()
        # driver.execute_script("arguments[0].click();", button)
        button = WebDriverWait(driver, sleep_time).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button')))
        button.click()
        return
    except:
        return


def click_quiz_button(driver, xpath, sleep_time):
    try:
        button = WebDriverWait(driver, sleep_time).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        return
    except:
        return


def get_quest_button_by_xpath(driver, xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
        return True
    except:
        return False


def get_h2_by_text(driver, text):
    try:
        driver.find_element(by=By.XPATH, value=f"//h2[text()='{text}']")
        return True
    except:
        return False