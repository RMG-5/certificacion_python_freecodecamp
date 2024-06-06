'''Formateador aritmético'''


def error_handling(problems):
    '''Función para manejar los diferentes tipos de errores'''

    # Si se introducen mas de 5 operaciones devuelve un error
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        x = problem.split()
        # Si el operador es multiplicacion o division devuelve un error
        if x[1] in ('*', '/'):
            return "Error: Operator must be '+' or '-'."
        # Si un operando contiene valores que no son numeros devuelve un error
        if not x[0].isnumeric() or not x[2].isnumeric():
            return 'Error: Numbers must only contain digits.'
        # Si un operando contiene mas de 4 digitos devuelve un error
        if len(x[0]) > 4 or len(x[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    return None


def perform_operations(problems, show_answers=False):
    '''Función para realizar las operaciones'''

    operating_1 = []
    operand_operating_2 = []
    lines = []
    results = []

    for problem in problems:
        x = problem.split()
        # Si el segundo operando es igual o mas largo que el primer operando
        if len(x[2]) >= len(x[0]):
            operating_1.append(x[0].rjust(int(len(x[2]) + 2)))
            operand_operating_2.append(x[1] + ' ' + x[2])
            lines.append('-' * int(len(x[2]) + 2))
            if x[1] == '+':
                results.append(
                    str(int(x[0]) + int(x[2])).rjust(int(len(x[2]) + 2)))
            elif x[1] == '-':
                results.append(
                    str(int(x[0]) - int(x[2])).rjust(int(len(x[2]) + 2)))

        # Si el segundo operando es mas corto que el primer operando
        else:
            operating_1.append(x[0].rjust(int(len(x[0]) + 2)))
            operand_operating_2.append(x[1] + x[2].rjust(int(len(x[0]) + 1)))
            lines.append('-' * int(len(x[0]) + 2))
            if x[1] == '+':
                results.append(
                    str(int(x[0]) + int(x[2])).rjust(int(len(x[0]) + 2)))
            elif x[1] == '-':
                results.append(
                    str(int(x[0]) - int(x[2])).rjust(int(len(x[0]) + 2)))

    # Si show_answers se establece en True devuelve las operaciones con resultado
    if show_answers:
        return '    '.join(operating_1) + '\n' + '    '.join(operand_operating_2) +\
            '\n' + '    '.join(lines) + '\n' + '    '.join(results)
    # Si show_answers se establece en false devuelve las operaciones sin resultado
    if not show_answers:
        return '    '.join(operating_1) + '\n' + '    '.join(operand_operating_2) +\
            '\n' + '    '.join(lines)
    return None


def arithmetic_arranger(problems, show_answers=False):
    '''Función para formatear operaciones aritméticas'''

    # Si se encuentra un error lo devuelve
    if error_handling(problems):
        return error_handling(problems)
    # Si no encuentra ningun error realiza el formateo aritmetico
    if not error_handling(problems):
        return perform_operations(problems, show_answers)
    return None


# ********** ********** ********** ********** ********** ********** ********** #
# Ejemplo de uso #

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print('\n')
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print('\n')
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print('\n')
print(arithmetic_arranger(
    ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print('\n')
print(arithmetic_arranger(["44 + 815", "909 - 2",
      "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print('\n')
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print('\n')
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print('\n')
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print('\n')
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print('\n')
print(arithmetic_arranger(["32 - 698", "1 - 3801",
      "45 + 43", "123 + 49", "988 + 40"], True))

# ********** ********** ********** ********** ********** ********** ********** #
