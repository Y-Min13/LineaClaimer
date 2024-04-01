import time
from src.AdsPower.operations import (get_last_window, click_quest_button, check_quest_button_exist,
                                     click_element, check_element_exist, find_window_by_url, check_label_exist)
from src.AdsPower.metamask import get_metamask_window


def open_linea_park(driver):
    driver.execute_script("window.open('https://www.google.com/', '_blank')")
    time.sleep(5)
    find_window_by_url(driver, 'https://www.google.com')
    driver.get('https://layer3.xyz/linea-park')
    time.sleep(10)


def check_sign(driver):
    # Проверяем авторизацию в Linea-Park
    while True:
        if check_element_exist(driver, '//*[@id="__next"]/div/div/div[2]/header/div/div[2]/button[1]/span') is True:
            return -1  # Если не авторизованы на сайте
        if check_element_exist(driver, '//*[@id="__next"]/div/div/div[2]/header/div/div[2]/button[1]/div/img') is True:
            return 1  # Если уже авторизованы на сайте
        time.sleep(5)


def log_out(driver):
    click_element(driver, '//*[@id="__next"]/div/div/div[2]/header/div/div[2]/button[1]/div/img', 3)
    click_element(driver, '//*[@id=":r7:"]/div/div[3]', 5)


def sign_in(driver):
    # Нажимаем Sign в LineaPark
    click_element(driver, '//*[@id="__next"]/div/div/div[2]/header/div/div[2]/button[1]', 4)

    # Выбираем метамаск во всплывающем окне
    click_element(driver, '//*[@id="radix-:r6:-content-evm"]/div/button[1]', 5)
    get_last_window(driver)
    time.sleep(3)

    # Кликаем далее
    click_element(driver, '//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]', 5)

    # Кликаем подключиться
    click_element(driver, '//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]', 10)
    get_last_window(driver)

    # Подписываем сообщение
    click_element(driver, '//*[@id="app-content"]/div/div/div/div[4]/footer/button[2]', 10)


def connect_metamask(driver):
    status = get_metamask_window(driver, 'notification.html')
    if status is False:
        return False
    click_element(driver, '//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]', 3)
    click_element(driver, '//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]', 3)
    return True


def check_stop(driver):
    if check_label_exist(driver, 'No matching transactions found') is True:
        return 'Not Found'
    if check_label_exist(driver, 'Completed') is True:
        return 'Completed'
    if check_label_exist(driver, 'Quest completed!') is True:
        return 'Quest completed!'
    if check_label_exist(driver, 'Validation failed') is True:
        return 'Validation failed'
    return None


def check_window(driver):
    while True:
        if check_stop(driver) is not None:
            break
        # Если кнопка на странице Verify
        click_quest_button(driver, 'Verify', 2)
        if check_stop(driver) is not None:
            break
        # Если кнопка на странице Begin
        click_quest_button(driver, 'Begin', 2)
        if check_stop(driver) is not None:
            break
        # Если кнопка на странице Continue
        click_quest_button(driver, 'Continue', 2)
        if check_stop(driver) is not None:
            break


def claim_quest(driver, url):
    window_count1 = len(driver.window_handles)
    driver.get(url)
    time.sleep(10)
    window_count2 = len(driver.window_handles)
    if window_count2 - window_count1 > 0:
        print('Еще один коннект')
        time.sleep(5)
        connect_metamask(driver)

    find_window_by_url(driver, url)

    check_window(driver)
