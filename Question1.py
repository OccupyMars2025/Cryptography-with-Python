# plain text is in lower case
# cipher text is in upper case


class AffineCipher:
    """
    encryption and decryption on affine cipher
    """

    def __init__(self):
        self._a, self._b, self._inverse_a = 0, 0, 0
        print('First use findkey() to find the key')

    # find greatest common divisor
    def gcd(self, m, n):
        return m if not n else self.gcd(n, m % n)

    # find the key (a, b)
    def findkey(self):
        m = list(input('Enter two plain text letters in lower case,such as az, bc:'))
        c = list(input('Enter two corresponding cipher text letters in upper case:'))
        for i in (0, 1):
            m[i] = ord(m[i]) - ord('a')
            c[i] = ord(c[i]) - ord('A')

        for a in range(1, 26):
            if self.gcd(26, a) != 1:
                continue
            if (a*(m[0] - m[1])) % 26 == (c[0] - c[1]) % 26:
                b = [0, 0]
                for i in (0, 1):
                    b[i] = (c[i] - a*m[i]) % 26
                if b[0] == b[1]:
                    break

        self._a, self._b = a, b[0]
        for inverse_a in range(1, 26):
            if (inverse_a * a) % 26 == 1:
                break
        self._inverse_a = inverse_a
        print('key = (', a, ',', b[0], ')')
        print('inverse of a =', inverse_a)
        return a, b[0], inverse_a

    def encryption(self):
        plain_text_path = input('Enter plain text path:')
        try:
            f = open(plain_text_path, 'r')
        except IOError:
            print('cannot open', plain_text_path)

        cipher_text_path = input('Enter filepath where encrypted text is to be stored:')
        try:
            out = open(cipher_text_path, 'w')
        except IOError:
            print('cannot write to', cipher_text_path)

        for line in f.readlines():
            for letter in line:
                if letter.islower():
                    cipher_char = chr(ord('A') + (self._a * (ord(letter) - ord('a')) + self._b) % 26)
                    out.write(str(cipher_char))
                else:
                    out.write(str(letter))

    def decryption(self):
        cipher_text_path = input('Enter cipher text path:')
        try:
            f = open(cipher_text_path, 'r')
        except IOError:
            print('cannot open', cipher_text_path)
        plain_text_path = input('Enter filepath where decrypted text is to be stored:')
        try:
            out = open(plain_text_path, 'w')
        except IOError:
            print('cannot open', plain_text_path)

        for line in f.readlines():
            for letter in line:
                if letter.isupper():
                    plain_char = chr(ord('a') + (self._inverse_a * (ord(letter) - ord('A') - self._b)) % 26)
                    out.write(str(plain_char))


if __name__ == "__main__":
    cipher = AffineCipher()
    cipher.findkey()
    cipher.decryption()
    cipher.encryption()

