class Cipher:

    code = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "CRYPTOABDEFGHIJKLMNQSUVWXZ"))

    def operation(self, code: dict, string: str):
        result = []
        string = string.upper()
        for item in string:
            code_symbol = code.get(item, item)
            result.append(code_symbol)
        return "".join(result)

    def encode(self, string):
      return self.operation(self.code, string)

    def decode(self, string):
      decode_dict = {a:b for b, a in self.code.items()}
      return self.operation(decode_dict, string)
    
        
cipher = Cipher()
print(cipher.encode("Hello world"))
print(cipher.decode("BTGGJ VJMGP"))
