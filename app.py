import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '!@#$%¨&*()[],.<>;:~^`\\/?°£¢¬==+-_|'

# EU QUERO PEGAR DIFERENTES FATORES DESSAS LISTAS DE FORMA RANDÔMICA E RETORNAR UMA SENHA...

upper, lower, nums, syms = True, True, True, True

pool = ""
amount = 10

if upper:
    pool += uppercase_letters
if lower:
    pool += lowercase_letters
if nums:
    pool += digits
if syms:
    pool += symbols

size = int(input("Insira o tamanho escolhido da senha: "))

for i in range(amount):
    password = ''.join(random.sample(pool, k=size))
    print(password)