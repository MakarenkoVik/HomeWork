import re


class Validator:

    @staticmethod
    def validate(user_data: tuple) -> bool:
        return Validator.validate_login(user_data[0]) and Validator.validate_password(user_data[1]) and Validator.validate_email(user_data[2])     
    
    @staticmethod
    def validate_login(login: str) -> bool:
        try:
            result = re.match(r"[a-zA-Z0-9]{6,10}", login)
            return result[0] == login
        except:
            return False
    
    @staticmethod
    def validate_password(password: str) -> bool:
        try:
            expr = r"""^(?=.*[A-Z])(?=.*[a-z])(?=.*[!"#$%&'()*+,-.\/:;<=>?@[\]^_`{|}~])[A-Za-z!"#$%&'()*+,-.\/:;<=>?@[\]^_`{|}~]{8,}$"""
            result = re.match(expr, password)
            return result[0] == password
        except:
            return False

    @staticmethod
    def validate_email(email: str) -> bool:
        try:
            result = re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$", email)
            return result[0] == email
        except:
            return False


a = Validator()
print(a.validate(("user222", "pkddalP|", "some@mail.by")))
