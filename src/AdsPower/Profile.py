from web3 import Web3
w3 = Web3()


class Profile(object):

    def __init__(self, profile_num, ads_id, key, password):
        self.profile_num = profile_num
        self.ads_id = ads_id
        self.key = key
        self.password = password
        self.address = w3.eth.account.from_key(key).address
