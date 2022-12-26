class InputFormulaError(Exception):
    ...


class InputNumberError(Exception):
    ...


class InputOperatorError(Exception):
    ...


def interactive_calculator():
    the_end = 0
    while the_end != 'quit':
        user_formula = input("Введите первое произвольное число, оператор (+,-,*,/,**) и второе произвольное число с пробелами между символами: ")
        try:
            number_one, operator, number_two = user_formula.split(" ")
        except ValueError:
            raise InputFormulaError
        try:
            number_one, number_two = int(number_one), int(number_two)
        except ValueError:
            raise InputNumberError
        operators = ("+", "-", "*", "/", "**")
        if operator == '+':
            operation = number_one + number_two
        elif operator == '-':
            operation = number_one - number_two
        elif operator == '*':
            operation = number_one * number_two
        elif operator == '/':
            operation = number_one / number_two
        elif operator == '**':
            operation = number_one ** number_two
        if operator not in operators:
            raise InputOperatorError
        print(operation)
        the_end = input("Введите quit для выхода из калькулятора либо продолжите.")


interactive_calculator()
