import settings
from src.AdsPower.Profile import Profile


def read_profiles():
    profiles_list = list()
    profiles_data = settings.profiles.read().splitlines()
    index = 1
    for row in profiles_data:
        num = row.split(' ')[0]
        wallet_num = int(num)
        ads_id = row.split(' ')[1]
        key = row.split(' ')[2]
        password = row.split(' ')[3]
        profile = Profile(wallet_num, ads_id, key, password)
        index += 1
        profiles_list.append(profile)
    return profiles_list
