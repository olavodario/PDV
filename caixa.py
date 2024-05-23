p = float(input('Qual é o preço do produto? R$ '))
pix = p-(p*5/100)
par = p+(p*5/100)
xpar = par/12

print ('Para pagar o produto selecione a opção')
print ('1 -------- Pix (5%OFF)')
print ('2 -------- Parcelado em 12x (5% JUROS)')

opção = int(input('Digite a opção: '))

if opção == 1:
    print('O valor R${} a vista fica apenas R${}'.format(p,pix))
elif opção == 2:
    print('Você pode pagar em 12x de R${} que da um total de R${}'.format(xpar,par))