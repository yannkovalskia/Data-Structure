def prioritas(operator):
    if operator in ('+', '-'):
        return 1
    if operator in ('*', '/', '%'):
        return 2
    if operator == '^':
        return 3
    return 0


def infix_to_postfix(ekspresi):
    tumpukan = []
    hasil = ""

    for simbol in ekspresi:
        if simbol.isalnum():
            hasil += simbol
        elif simbol == '(':
            tumpukan.append(simbol)
        elif simbol == ')':
            while tumpukan and tumpukan[-1] != '(':
                hasil += tumpukan.pop()
            tumpukan.pop()
        else:
            while tumpukan and prioritas(tumpukan[-1]) >= prioritas(simbol):
                hasil += tumpukan.pop()
            tumpukan.append(simbol)

    while tumpukan:
        hasil += tumpukan.pop()

    return hasil


def infix_to_prefix(ekspresi):
    ekspresi = ekspresi[::-1]
    ekspresi = ekspresi.replace('(', 'temp')
    ekspresi = ekspresi.replace(')', '(')
    ekspresi = ekspresi.replace('temp', ')')

    hasil_postfix = infix_to_postfix(ekspresi)
    prefix = hasil_postfix[::-1]
    return prefix


def hitung_postfix(ekspresi):
    stack = []

    for simbol in ekspresi:
        if simbol.isdigit():
            stack.append(int(simbol))
        else:
            b = stack.pop()
            a = stack.pop()
            if simbol == '+':
                hasil = a + b
            elif simbol == '-':
                hasil = a - b
            elif simbol == '*':
                hasil = a * b
            elif simbol == '/':
                hasil = a / b
            elif simbol == '%':
                hasil = a % b
            elif simbol == '^':
                hasil = a ** b
            else:
                return "[ERROR] Operator tidak dikenali!"
            stack.append(hasil)
    return stack.pop()


def hitung_prefix(ekspresi):
    stack = []

    for simbol in ekspresi:
        if simbol.isdigit():
            stack.append(int(simbol))
        else:
            b = stack.pop()
            a = stack.pop()
            if simbol == '+':
                hasil = a + b
            elif simbol == '-':
                hasil = a - b
            elif simbol == '*':
                hasil = a * b
            elif simbol == '/':
                hasil = a / b
            elif simbol == '%':
                hasil = a % b
            elif simbol == '^':
                hasil = a ** b
            else:
                return "[ERROR] Operator tidak dikenali!"
            stack.append(hasil)
    return stack.pop()
ekspresi = "(5+3)*4"
print("Infix   :", ekspresi)
print("Postfix :", infix_to_postfix(ekspresi))
b = infix_to_postfix(ekspresi)
print(f"Hasil postfix = {hitung_postfix(b)}")
print("\nInfix   :", ekspresi)
print("Prefix  :", infix_to_prefix(ekspresi))
a = infix_to_prefix(ekspresi)
print(f"Hasil prefix = {hitung_prefix(b)}")