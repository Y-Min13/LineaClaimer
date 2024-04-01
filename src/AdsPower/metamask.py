import re
from src.AdsPower.operations import click_element, send_element_keys, check_element_exist
import time


def metamask_import(driver, private, password):
    # Это левый сид для импорта в ММ
    seed = 'almost buddy whip witness warfare frown heart thing confirm supply drink tip'.split()

    # Термсы
    click_element(driver, '//*[@id="onboarding__terms-checkbox"]', 1)

    # Согласие на использование
    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[3]/button', 1)

    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div/div/div/button[1]', 2)

    # Отправка сида
    for i in range(len(seed)):
        send_element_keys(driver, f'//*[@id="import-srp__srp-word-{i}"]', seed[i], 1)

    # Подтверждаем сид фразу
    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button', 2)

    # Ввод пароля 1
    send_element_keys(driver, '//*[@data-testid="create-password-new"]', password, 1)
    # Ввод пароля 2
    send_element_keys(driver, '//*[@data-testid="create-password-confirm"]', password, 3)

    # Ставим галочку
    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input', 3)

    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button', 6)

    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button', 3)
    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button', 3)
    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button', 10)

    click_element(driver, '//*[@id="popover-content"]/div/div/section/div[1]/div/button/span', 4)

    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div[2]/button', 3)

    # Импорт приватника
    #click_element(driver, '//*[@id="app-content"]/div/div[2]/div/button/span[1]/span', 3)
    click_element(driver, '/html/body/div[3]/div[3]/div/section/div[4]/button', 1)
    click_element(driver, '/html/body/div[3]/div[3]/div/section/div[2]/div[2]/button', 1)
    send_element_keys(driver, '//*[@id="private-key-box"]', private, 1)

    # Нажимаем кнопку Импорт
    click_element(driver, '/html/body/div[3]/div[3]/div/section/div[2]/div/div[2]/button[2]', 3)


def metamask_sign(driver, password):
    send_element_keys(driver, '//*[@id="password"]', password, 4)
    click_element(driver, '//*[@id="app-content"]/div/div[2]/div/div/button', 4)


def get_metamask_window(driver, path):
    all_windows = driver.window_handles
    # Ищем вкладку по url
    for i in range(len(all_windows)):
        driver.switch_to.window(driver.window_handles[i])
        pattern = r'chrome-extension://[a-z]{32}/'+path
        url = driver.current_url
        if re.search(pattern, url) is not None:
            return i
    return False


def metamask_check_seed(driver):
    get_metamask_window(driver, 'home.html')
    # Проверяем введена ли сид фраза
    while True:
        if check_element_exist(driver, '//*[@id="onboarding__terms-checkbox"]') is True:
            return -1  # Если приватник не импортирован
        if check_element_exist(driver, '//*[@id="password"]') is True:
            return 1  # Если приватник импортировали
        time.sleep(5)
