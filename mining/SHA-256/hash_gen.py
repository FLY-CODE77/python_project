import hashlib

class hash_gen:
    def __init__(self, key):
        self.key = key

    def make_data(self):
        encoded_string =  self.key .encode()
        hexdigest = hashlib.sha256(encoded_string).hexdigest()
        print('result :', hexdigest)
