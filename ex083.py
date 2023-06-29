expression = str(input('Digite uma expressão matemática: '))
list_exp = list(expression)
open_p = list_exp.count('(')
close_p = list_exp.count(')')
if open_p == close_p:
    print(f'A expressão está correta')
elif open_p > close_p:
    print(f'A expressão está incorreta, há {open_p - close_p} parêntesis a serem fechados.')
elif close_p > open_p:
    print(f'A expressão está incorreta, há {close_p - open_p} parêntesis fechados em excesso.')
