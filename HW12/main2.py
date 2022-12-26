class InvalidLogin(Exception):
    ...


class InvalidPassword(Exception):
    ...


class InvalidEmail(Exception):
    ...


class ValidationError(Exception):
    ...


class Validator:

    @staticmethod
    def validation(user_data: tuple) -> bool:
        try:
            Validator.validate_login(user_data[0])
            Validator.validate_password(user_data[1])
            Validator.validate_email(user_data[2])
        except (InvalidLogin, InvalidPassword, InvalidEmail):
            raise ValidationError
        return True
    
    @staticmethod
    def validate_login(login: str) -> bool:
        if len(login) >= 6:
            return True
        else:
            raise InvalidLogin
    
    @staticmethod
    def validate_password(password: str) -> bool:
        special_symbols = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_letters = upper_letters.lower()
        spec_symbol = False
        up_letter = False
        low_letter = False
        for symbol in password:
            if symbol in special_symbols:
                spec_symbol = True
            if symbol in upper_letters:
                up_letter = True
            if symbol in lower_letters:
                low_letter = True
        if spec_symbol == True and up_letter == True and low_letter == True and len(password) >= 8:
            return True
        else:
            raise InvalidPassword

    @staticmethod
    def validate_email(email: str) -> bool:
        if "@" in email and email[-3:] == ".by":
            return True
        else:
            raise InvalidEmail


a = Validator()
print(a.validation(("sgd0sgd0", "dgbdfgDh@bd.b", "!yhfghf@yj.by")))
