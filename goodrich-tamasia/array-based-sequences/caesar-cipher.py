"""Simple Cryptography using a Caesar cipher."""


class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift % 26

    def encrypt(self, text: str) -> str:
        return self._transform(text, self.shift)

    def decrypt(self, text: str) -> str:
        return self._transform(text, -self.shift)

    def _transform(self, text: str, shift: int) -> str:
        result = []
        for char in text:
            if char.isupper():
                base = ord("A")
                result.append(chr((ord(char) - base + shift) % 26 + base))
            elif char.islower():
                base = ord("a")
                result.append(chr((ord(char) - base + shift) % 26 + base))
            else:
                result.append(char)
        return "".join(result)


if __name__ == "__main__":
    cipher = CaesarCipher(3)
    encrypted = cipher.encrypt("Hello, World!")
    print(encrypted)  # Khoor, Zruog!
    print(cipher.decrypt(encrypted))  # Hello, World!
