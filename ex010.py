# Hoje o dólar está em 5.33, o euro está em 5.18 e a libra está em 5.95.
dimdim = float(input('Quanto dinheiro você tem na carteira?'))
dolar = dimdim / 5.33
euro = dimdim / 5.18
libra= dimdim / 5.95
print(f'{dimdim} reais é equivalente a: \n{euro:.2f} euros. \n{dolar:.2f} dólares. \n{libra:.2f} libras.')
