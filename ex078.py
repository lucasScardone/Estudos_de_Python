numbers = []
for c in range(1, 8):
    numbers.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Os números digitados foram: {numbers}.')
print(f'O menor valor digitado foi {min(numbers)} na(s) posição(ões) {numbers.index(min(numbers))+1}')
print(f'O maior valor digitado foi {max(numbers)} na(s) posição(ões) {numbers.index(max(numbers))+1}')
