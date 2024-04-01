import time
import settings
from src.AdsPower.metamask import metamask_import, metamask_sign, metamask_check_seed
from src.AdsPower.linea import sign_in, check_sign, log_out, open_linea_park, claim_quest
from src.AdsPower.operations import open_profile, close_profile, configure_profile, find_window_by_url, close_all_tabs


def claim(profile_list):
    for profile in profile_list:
        driver = None
        try:
            resp = open_profile(profile.ads_id)
            driver = configure_profile(resp)
            time.sleep(5)

            #           Работа с MetaMask
            seed_status = metamask_check_seed(driver)
            if seed_status > 0:
                metamask_sign(driver, profile.password)
            if seed_status < 0:
                metamask_import(driver, profile.key, profile.password)
            time.sleep(4)

            #           Переключаемся на первую вкладку и открываем какой-либо сайт
            find_window_by_url(driver, '127.0.0.1')
            driver.get('https://www.youtube.com/')

            #           Открываем Linea-Park в новой вкладке
            open_linea_park(driver)

            #           Коннект к Layer3
            linea_park_sign = check_sign(driver)
            if linea_park_sign < 0:
                sign_in(driver)
            if linea_park_sign > 0:
                log_out(driver)
                sign_in(driver)

            find_window_by_url(driver, 'https://layer3.xyz/linea-park')

            #       Квесты
            claim_quest(driver, 'https://layer3.xyz/quests/linea-zace')
            claim_quest(driver, 'https://layer3.xyz/quests/linea-alienswap')
            claim_quest(driver, 'https://layer3.xyz/quests/linea-micro3')
            claim_quest(driver, 'https://layer3.xyz/quests/frog-war-404')
            claim_quest(driver, 'https://layer3.xyz/quests/linea-acg')
            claim_quest(driver, 'https://layer3.xyz/quests/lineas-knobs-bilinear')
            claim_quest(driver, 'https://layer3.xyz/quests/imaginairynfts-lineas-artisan-trail')

        except Exception as ex:
            print(f'Ошибка в профиле {profile.profile_num}  |  {ex}')
        try:
            if settings.close_profile_enable == 1:
                close_all_tabs(driver)
                close_profile(profile.ads_id)
        except:
            pass
