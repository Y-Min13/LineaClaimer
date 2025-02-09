import time
from src.AdsPower.operations import (get_last_window, click_quest_button, click_quiz_button, click_continue,
                                     click_element, check_element_exist, find_window_by_url, check_label_exist,
                                     get_h2_by_text, get_quest_button_by_xpath)
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


def check_stop(driver, profile):
    if check_label_exist(driver, 'No matching transactions found') is True:
        return 'No matching transactions found'
    if check_label_exist(driver, f'No token transfers matching the criteria found for {profile.address}.') is True:
        return 'No matching transactions found'
    if check_label_exist(driver, 'Completed') is True:
        return 'Completed'
    if check_label_exist(driver, 'Quest completed!') is True:
        return 'Quest completed!'
    if check_label_exist(driver, 'Validation failed') is True:
        return 'No matching transactions found'
    if check_label_exist(driver, 'Discord account is not linked!') is True:
        return 'No matching transactions found'
    if check_label_exist(driver, 'Could not find membership!') is True:
        return 'No matching transactions found'
    if get_h2_by_text(driver, 'At Linea Park, you can access the referral zone to claim your referral link. Please choose the correct answer(s) where you can share your referral link.') is True and driver.current_url == 'https://layer3.xyz/quests/the-linea-voyage-gaming-and-social-linea-park':
        return 'quiz2'
    if get_quest_button_by_xpath(driver, '//*[@id="radix-:ra:"]/div/div[2]/div[4]/div/div/div/a/button') is True and driver.current_url == 'https://layer3.xyz/quests/metamask-prioritizes-user-security':
        return 'snaps'
    if get_h2_by_text(driver, 'If a game requests your private key or recovery phrase to connect your wallet, would you comply?') is True and driver.current_url == 'https://layer3.xyz/quests/security-learn':
        return 'quiz3'
    if get_h2_by_text(driver, 'At Linea Park, you can access the referral zone to claim your referral link. Please choose the correct answer(s) where you can share your referral link.') is True and driver.current_url == 'https://layer3.xyz/quests/linea-park-entrance':
        return 'quiz1'
    return None


def skip(driver, profile):
    time.sleep(3)
    print('Поиск кнопки Скипа')
    click_continue(driver, 10)
    time.sleep(3)
    click_quest_button(driver, 'Skip', 12)
    time.sleep(3)
    check_stop(driver, profile)
    click_quest_button(driver, 'Skip', 5)
    time.sleep(3)
    click_quest_button(driver, 'Skip', 5)


def check_window(driver, profile):
    while True:
        check = check_stop(driver, profile)
        if check is not None:
            return check
        # Если кнопка на странице Verify
        click_quest_button(driver, 'Verify', 2)
        check = check_stop(driver, profile)
        if check is not None:
            return check
        # Если кнопка на странице Begin
        click_quest_button(driver, 'Begin', 2)
        check = check_stop(driver, profile)
        if check is not None:
            return check
        # Если кнопка на странице Continue
        click_quest_button(driver, 'Continue', 2)
        check = check_stop(driver, profile)
        if check is not None:
            return check


def check_window_quiz(driver, profile):
    while True:
        check = check_stop(driver, profile)
        if check is not None:
            return check
        # Если кнопка на странице Verify
        click_quest_button(driver, 'Verify', 2)
        check = check_stop(driver, profile)
        if check is not None:
            return check
        # Если кнопка на странице Begin
        click_quest_button(driver, 'Begin', 2)
        check = check_stop(driver, profile)
        if check is not None:
            return check
        # Если кнопка на странице Continue
        click_quest_button(driver, 'Continue', 2)
        check = check_stop(driver, profile)
        if check is not None:
            return check
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 2)
        check = check_stop(driver, profile)
        if check is not None:
            return check
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 2)
        check = check_stop(driver, profile)
        if check is not None:
            return check


def claim_quest(driver, profile, url):
    print(f'Квест: {url}')
    window_count1 = len(driver.window_handles)
    driver.get(url)
    time.sleep(10)
    window_count2 = len(driver.window_handles)
    if window_count2 - window_count1 > 0:
        print('Еще один коннект')
        time.sleep(5)
        connect_metamask(driver)

    find_window_by_url(driver, url)

    check = check_window(driver, profile)
    if check == 'Completed':
        print('Квест уже выполнен')
    if check == 'Quest completed!':
        print('Квест успешно выполнен')
    if check == 'No matching transactions found':
        print('Условия не выполнены')
        skip(driver, profile)
    print('Идем дальше')
    time.sleep(6)


def quiz1(driver, profile):
    print(f'Квест: QUIZ 1')
    window_count1 = len(driver.window_handles)
    url = 'https://layer3.xyz/quests/linea-park-entrance'
    driver.get(url)
    time.sleep(10)
    window_count2 = len(driver.window_handles)
    if window_count2 - window_count1 > 0:
        print('Еще один коннект')
        time.sleep(5)
        connect_metamask(driver)

    find_window_by_url(driver, url)

    check = check_window_quiz(driver, profile)
    if check == 'Completed':
        print('Квест уже выполнен')
    if check == 'Quest completed!':
        print('Квест успешно выполнен')
    if check == 'No matching transactions found':
        print('Условия не выполнены')
        skip(driver, profile)
    if check == 'quiz1':
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 4)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 4)
        time.sleep(5)
        click_quiz_button(driver, '//*[@id="7a1d1cc8-d144-4b4d-a3ed-1381da033553"]', 10)
        time.sleep(5)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 4)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 4)
        time.sleep(5)
        check_window_quiz(driver, profile)
    print('Идем дальше')
    time.sleep(6)


def quiz2(driver, profile):
    print(f'Квест: QUIZ 2')
    window_count1 = len(driver.window_handles)
    url = 'https://layer3.xyz/quests/the-linea-voyage-gaming-and-social-linea-park'
    driver.get(url)
    time.sleep(10)
    window_count2 = len(driver.window_handles)
    if window_count2 - window_count1 > 0:
        print('Еще один коннект')
        time.sleep(5)
        connect_metamask(driver)

    find_window_by_url(driver, url)

    check = check_window_quiz(driver, profile)
    if check == 'Completed':
        print('Квест уже выполнен')
    if check == 'Quest completed!':
        print('Квест успешно выполнен')
    if check == 'No matching transactions found':
        print('Условия не выполнены')
        skip(driver, profile)
    if check == 'quiz2':
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="2378d927-79a5-4b54-8ab8-857aa64fb821"]', 10)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="127ddd13-709f-45cf-836d-af17db29801f"]', 10)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        check_window_quiz(driver, profile)
    print('Идем дальше')
    time.sleep(6)


def quiz3(driver, profile):
    print(f'Квест: QUIZ 3')
    window_count1 = len(driver.window_handles)
    url = 'https://layer3.xyz/quests/security-learn'
    driver.get(url)
    time.sleep(10)
    window_count2 = len(driver.window_handles)
    if window_count2 - window_count1 > 0:
        print('Еще один коннект')
        time.sleep(5)
        connect_metamask(driver)

    find_window_by_url(driver, url)

    check = check_window_quiz(driver, profile)
    if check == 'Completed':
        print('Квест уже выполнен')
    if check == 'Quest completed!':
        print('Квест успешно выполнен')
    if check == 'No matching transactions found':
        print('Условия не выполнены')
        skip(driver, profile)
    if check == 'quiz3':
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="a2"]', 10)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        check_window(driver, profile)
    print('Идем дальше')
    time.sleep(6)


def quiz4(driver, profile):
    print(f'Квест: QUIZ 4')
    window_count1 = len(driver.window_handles)
    url = 'https://layer3.xyz/quests/metamask-prioritizes-user-security'
    driver.get(url)
    time.sleep(10)
    window_count2 = len(driver.window_handles)
    if window_count2 - window_count1 > 0:
        print('Еще один коннект')
        time.sleep(5)
        connect_metamask(driver)

    find_window_by_url(driver, url)

    check = check_window_quiz(driver, profile)
    if check == 'Completed':
        print('Квест уже выполнен')
    if check == 'Quest completed!':
        print('Квест успешно выполнен')
    if check == 'No matching transactions found':
        print('Условия не выполнены')
        skip(driver, profile)
    if check == 'snaps':
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[2]/div[4]/div/div/div/a/button', 10)
        time.sleep(3)
        find_window_by_url(driver, url)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="928ef9b8-3289-4300-9208-92558f3342f8"]', 10)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="0d0bb30c-82b1-4124-a67c-407fbd9df13b"]', 10)
        time.sleep(3)
        click_quiz_button(driver, '//*[@id="__next"]/div/div/div[3]/div/div[3]/div/div[2]/button', 5)
        click_quiz_button(driver, '//*[@id="radix-:ra:"]/div/div[3]/div/div/div/button', 5)
        check_window_quiz(driver, profile)
    print('Идем дальше')
    time.sleep(6)
