def is_fibonacci(num):
    def is_perfect_square(n):
        return int(n**0.5)**2 == n
    
    
    # Um número é Fibonacci se (5*n^2 + 4) ou (5*n^2 - 4) for um quadrado perfeito
    if is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4):
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

num = int(input("Informe um número: "))
print(is_fibonacci(num))


def count_a_in_string(string):
    count = string.lower().count('a')
    return f"A letra 'a' aparece {count} vezes na string."

string = input("Informe uma string: ")
print(count_a_in_string(string))
