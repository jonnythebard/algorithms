class CaesarCipher:

    def __init__(self, shift):
        self._shift = shift

    def encrypt(self, message):
        return self._transform('enc', message)

    def decrypt(self, secret):
        return self._transform('dec', secret)

    def _transform(self, order, string):
        msg = list(string)

        if order == 'enc':
            secret = ''.join(chr((ord(c) + self._shift) % 26 + ord('A')) for c in msg)
            return secret

        if order == 'dec':
            message = ''.join(chr((ord(c) - self._shift) % 26 + ord('A')) for c in msg)
            return message

if __name__ == '__main__':
    code01 = CaesarCipher(3)
    s = 'HELP ME'
    str01 = code01.encrypt(s)
    print(str01)
    str01 = code01.decrypt(str01)
    print(str01)