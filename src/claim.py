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

            if settings.switch_mm == 1:

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
                time.sleep(2)
                #           Переходим на вкладку Linea-Park
                find_window_by_url(driver, 'https://layer3.xyz/linea-park')
                time.sleep(4)
                open_linea_park(driver)

                # #           Коннект к Layer3
                linea_park_sign = check_sign(driver)
                if linea_park_sign < 0:
                    sign_in(driver)
                if linea_park_sign > 0:
                    log_out(driver)
                    sign_in(driver)
                    

            find_window_by_url(driver, 'https://layer3.xyz')
            #       Квесты
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-zace')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-alienswap')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-micro3')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/frog-war-404')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-acg')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/lineas-knobs-bilinear')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/imaginairynfts-lineas-artisan-trail')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-abyss-world')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-pictograph')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-yooldo')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-dmail')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-gamic-app')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-asmatch')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-bitavatar')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-readon')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-sending-me')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-metasky')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/2048-zypher')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-brototype')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-battlemon')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-play-nouns')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-dexsport')

            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-timeless-wallet')
            claim_quest(driver, profile, 'https://layer3.xyz/quests/linea-satoshi-universe')

            time.sleep(10)
        except Exception as ex:
            print(f'Ошибка в профиле {profile.profile_num}  |  {ex}')
        try:
            if settings.close_profile_enable == 1:
                close_all_tabs(driver)
                close_profile(profile.ads_id)
        except:
            pass
