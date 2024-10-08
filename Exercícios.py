"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence 
ou não a sequência.
"""
def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

def is_in_fibonacci(n):
    fib_sequence = fibonacci_sequence(n)
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Defina o número aqui
numero = int(input("Informe um número: "))
print(is_in_fibonacci(numero))

"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

"""
def verificar_letra_a(string):
    # Contar a ocorrência de 'a' e 'A'
    count_a = string.count('a')
    count_A = string.count('A')
    total_count = count_a + count_A
    
    # Verificar se 'a' ou 'A' estão na string
    if total_count > 0:
        return f"A letra 'a' (maiúscula ou minúscula) aparece {total_count} vezes na string."
    else:
        return "A letra 'a' (maiúscula ou minúscula) não aparece na string."

# Defina a string aqui
string = input("Informe uma string: ")
print(verificar_letra_a(string))

"""
3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

"""
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

RESPOSTA: 77

"""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____


"""

RESPOSTA:
a) Lógica: A sequência é formada por números ímpares consecutivos.
Próximo elemento: 9

b) Lógica: Cada número é o dobro do anterior.
Próximo elemento: 128

c) Lógica: A sequência é formada pelos quadrados dos números inteiros (0², 1², 2², 3², 4², 5², 6², …).
Próximo elemento: 49 (7²)

d) Lógica: A sequência é formada pelos quadrados dos números pares (2², 4², 6², 8², …).
Próximo elemento: 100 (10²)

e) Lógica: A sequência é a sequência de Fibonacci, onde cada número é a soma dos dois anteriores.
Próximo elemento: 13 (5 + 8)

f) Lógica: A sequência parece alternar entre adicionar 8 e adicionar 1.
Próximo elemento: 20 (19 + 1)

"""
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar 
e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas 
idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 
"""

Resposta: Ligue o primeiro interruptor por 10 minutos, depois desligue-o e ligue o segundo; a lâmpada acesa é do segundo, a quente e apagada é do primeiro, e a fria 
e apagada é do terceiro. Um fato engraçado... eu vi esse teste em uma serie da netflix
 
