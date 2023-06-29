m = float(input('Digite a medida em metros:\n'))
km = round(m / 1000, 4)
hm = round(m / 100, 3)
dam = round(m / 10, 2)
dm = round(m * 10, 1)
cm = round(m * 100, 1)
mm = round(m * 1000)
print(f'A medida dada em metros é igual a:\n km:{km}\n hm:{hm}\n dam:{dam}\n'
      f' dm:{dm}\n cm:{cm}\n mm:{mm}')
