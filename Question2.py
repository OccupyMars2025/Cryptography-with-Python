# question 2
import numpy as np


A = [[3, 13, 21, 9], [15, 10, 6, 25], [10, 17, 4, 8], [1, 23, 7, 2]]
inverseA = [[23, 13, 20, 5], [0, 10, 11, 0], [9, 11, 15, 22], [9, 22, 6, 25]]
B = [[1], [21], [8], [17]]


class Polyalphabetic_Substitution_With_Matrix:
    """
    A and inverseA are both entered by the user
    """
    def __init__(self, A, inverseA, B):
        """
        verify that inverseA * A is an identity matrix
        after modulo 26
        :param A:
        :param inverseA:
        :param B:
        """
        A = np.mat(A)
        inverseA = np.mat(inverseA)
        B = np.mat(B)
        print('matrix A :\n', A)
        print('matrix inverseA :\n', inverseA)
        print('matrix B\n', B)
        product = (A * inverseA) % 26
        if (product == np.mat(np.eye(A.shape[0]))).all():
            print('OK, go on')
        else:
            print('Wrong! A * inverseA must be an identity matrix after modulo 26')

        self._A, self._inverseA, self._B = A, inverseA, B
        self._dim = A.shape[0]
        self._number_of_added_chars = 0  # add 'x' at end to help transform

    def preprocess_plain_text(self):
        """
        get only English letters, and transform them all
        to lower case
        """
        filepath1 = input('Enter path of original plain text:')
        try:
            f1 = open(filepath1, 'r')
        except IOError:
            print('cannot open', filepath1)
        filepath2 = input('Enter path of preprocessed plain text:')
        try:
            f2 = open(filepath2, 'w')
        except IOError:
            print('cannot open', filepath2)

        for line in f1.readlines():
            for original_char in line:
                if original_char.isalpha():
                    if original_char.isupper():
                        original_char = original_char.lower()
                    f2.write(str(original_char))

    def encryption(self):
        """
        if the number of chars is not multiple of self._dim,
        then add 'x' at the end
        :return:
        """
        filepath1 = input('Enter path of preprocessed plain text:')
        try:
            f1 = open(filepath1, 'r')
        except IOError:
            print('cannot open', filepath1)
        filepath2 = input('Enter path of encrypted text:')
        try:
            f2 = open(filepath2, 'w')
        except IOError:
            print('cannot open', filepath2)

        M = np.mat([[0] for i in range(self._dim)])
        i = 0
        for line in f1.readlines():
            for plain_char in line:
                if i < self._dim - 1:
                    M[i, 0] = ord(plain_char)
                    i = i + 1
                else:
                    # once M is full, process it immediately
                    # otherwise you may lose the last self._dim chars
                    M[i, 0] = ord(plain_char)
                    M = M - ord('a')
                    C = (self._A * M + self._B) % 26 + ord('A')
                    for j in range(self._dim):
                        cipher_char = chr(C[j, 0])
                        f2.write(str(cipher_char))
                    i = 0

        if i < self._dim:
            self._number_of_added_chars = self._dim - i
            while i < self._dim:
                M[i, 0] = ord('x')
                i = i + 1
            M = M - ord('a')
            C = (self._A * M + self._B) % 26 + ord('A')
            for j in range(self._dim):
                cipher_char = chr(C[j, 0])
                f2.write(str(cipher_char))

    def decryption(self):
        """
        the code is very similar to that of encryption()
        :return:
        """
        filepath1 = input('Enter path of encrypted text:')
        try:
            f1 = open(filepath1, 'r')
        except IOError:
            print('cannot open', filepath1)
        filepath2 = input('Enter path of decrypted text:')
        try:
            f2 = open(filepath2, 'w')
        except IOError:
            print('cannot open', filepath2)

        C = np.mat([[0] for i in range(self._dim)])
        i = 0
        for line in f1.readlines():
            for cipher_char in line:
                if i < self._dim - 1:
                    C[i, 0] = ord(cipher_char)
                    i = i + 1
                else:
                    C[i, 0] = ord(cipher_char)
                    C = C - ord('A')
                    M = (self._inverseA * (C - self._B)) % 26 + ord('a')
                    for j in range(self._dim):
                        plain_char = chr(M[j, 0])
                        f2.write(str(plain_char))
                    i = 0

        if self._number_of_added_chars:
            f2.write('\nremove last {0} chars'.format(self._number_of_added_chars))


cipher = Polyalphabetic_Substitution_With_Matrix(A, inverseA, B)
cipher.preprocess_plain_text()
cipher.encryption()
cipher.decryption()