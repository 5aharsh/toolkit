import sys
import hashlib

class Hash:
    BUF_SIZE = 65536

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    def __init__(self, filename):
        self.file = filename

    def md5_hash(self):
        with open(self.file, 'rb') as f:
            while True:
                data = f.read(self.BUF_SIZE)
                if not data:
                    break
                self.md5.update(data)
        return self.md5.hexdigest()

    def sha1_hash(self):
        with open(self.file, 'rb') as f:
            while True:
                data = f.read(self.BUF_SIZE)
                if not data:
                    break
                self.sha1.update(data)
        return self.sha1.hexdigest()
