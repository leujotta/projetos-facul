# -*- coding: utf-8 -*-
"""ex menu de compra

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Ay-C6HPuF-1o1dxIIEZ4anaBKOFsd7a

Login
"""

from getpass import getpass

qtde_user = int(input('quantos usuarios?'))
user = []
senha = []

for i in range(qtde_user):
  user.append(input('\ndigite o login de usuario:'))
  senha.append(getpass('digite a senha do usuario:'))

with open('usersenha.txt' , 'w') as arquivo:
 for indice , users in enumerate(user):
  arquivo.write(users + ';' + senha[indice])
  arquivo.write('\n')

login = input('digite seu usuario:')
senha = str(input('digite sua senha:'))
arquivo = open('usersenha.txt' , 'r')

for i in arquivo:
 nova_senha = i.split(';')[1].replace('\n' , '')
 if login != i.split(';')[0]:
  print('usuario invalido!!')
 elif senha != nova_senha:
  print('senha invalida!!')
 else:
  print('bem vindo')
  login = True

"""Produtos

"""

qtde_prod = int(input('quantos produtos?'))
prod = []
preço = []

for i in range(qtde_prod):
  prod.append(input('\ndigite o produto:'))
  preço.append(float(input('digite o preço:')))

with open('prodepreço.txt' , 'w') as arquivo2:
 for indice , prods in enumerate(prod):
  arquivo2.write(prods + ';' + str(preço[indice]))
  arquivo2.write('\n')

"""menu"""

print('-' * 50)
print('Bem-Vindo ao Magazine Cristina')
print('-' * 50)

print('Veja nosso catálogo:')
print('\n')
arquivo2 = open('prodepreço.txt' , 'r')

for indice , a in enumerate(arquivo2):
  produto = a.split(';')[0]
  precin = a.split(';')[1]
  print(indice , produto , 'R$' , precin)
print('-' * 50)
escolha = int(input('Escolha seu produto:'))
print(prod[escolha] , 'R$' , preço[escolha])

if login == True:
  print('-' * 50)
  print('Bem-Vindo ao Magazine Cristina')
  print('-' * 50)

  print('Veja nosso catálogo:')
  print('\n')
  arquivo2 = open('prodepreço.txt' , 'r')

  for indice , a in enumerate(arquivo2):
    produto = a.split(';')[0]
    precin = a.split(';')[1]
    print(indice , produto , 'R$' , precin)
  print('-' * 50)
  escolha = int(input('Escolha seu produto:'))
  print(prod[escolha] , 'R$' , preço[escolha])
else:
  print('usuario nao identificado')

prod_carrinho = []
preço_carrinho = []

while True:
 escolhacarrinho = int(input('Deseja adicionar ao Carrinho? Não(0) Sim(1) '))
 if escolhacarrinho == 1:
  print(prod[escolha] , 'adicionado com sucesso')
  prod_carrinho.append(prod[escolha])
  preço_carrinho.append(preço[escolha])
  break
while True:
   continuar = int(input('Deseja adicionar outro produto ao Carrinho? Não(0) Sim(1) '))
   if continuar == 1 and escolhacarrinho == 1:
    prod2 = int(input('Digite o número do produto:'))
    prod_carrinho.append(prod[prod2])
    preço_carrinho.append(preço[prod2])
    print(prod[prod2] , 'adicionado com sucesso')
   else:
    break

lista_precin = []
fds = 0
print('-' * 50)
print('Carrinho do' , login)
print('-' * 50)
print('\n')
print('Produtos:')
print('\n')
for i in prod_carrinho:
  print(i)
print('\n')
for a in preço_carrinho:
  lista_precin.append(a)
print('\n')
for b in lista_precin:
  fds += b
print('Total: R$' , round(fds , 2))

"""Ultimo Teste"""

print('-' * 50)
print('Bem-Vindo ao Magazine Cristina')
print('-' * 50)
print('Faça o Login:')
print('\n')

login = input('digite seu usuario:')
senha = str(input('digite sua senha:'))
arquivo = open('usersenha.txt' , 'r')

for i in arquivo:
 nova_senha = i.split(';')[1].replace('\n' , '')
 if login != i.split(';')[0]:
  print('usuario invalido!!')
 elif senha != nova_senha:
  print('senha invalida!!')
 else:
  acesso = True

if acesso == True:
  print('-' * 50)
  print('Magazine Cristina')
  print('Bem Vindo!' , login)
  print('-' * 50)

  print('Veja nosso catálogo:')
  print('\n')
  arquivo2 = open('prodepreço.txt' , 'r')

  for indice , a in enumerate(arquivo2):
    produto = a.split(';')[0]
    precin = a.split(';')[1]
    print(indice , produto , 'R$' , precin)
  print('-' * 50)
  escolha = int(input('Escolha seu produto:'))
  print(prod[escolha] , 'R$' , preço[escolha])
  print('\n')

prod_carrinho = []
preço_carrinho = []

while True:
 escolhacarrinho = int(input('Deseja adicionar ao Carrinho? Não(0) Sim(1) '))
 print('\n')
 if escolhacarrinho == 1:
  print(prod[escolha] , 'adicionado com sucesso')
  prod_carrinho.append(prod[escolha])
  preço_carrinho.append(preço[escolha])
  break
while True:
   continuar = int(input('Deseja adicionar outro produto ao Carrinho? Não(0) Sim(1) '))
   print('\n')
   if continuar == 1 and escolhacarrinho == 1:
    prod2 = int(input('Digite o número do produto:'))
    prod_carrinho.append(prod[prod2])
    preço_carrinho.append(preço[prod2])
    print(prod[prod2] , 'adicionado com sucesso')
   else:
    break

lista_precin = []
fds = 0
print('-' * 50)
print('Carrinho do' , login)
print('-' * 50)
print('\n')
print('Produtos:')
print('\n')
for i in prod_carrinho:
  print(i)
print('\n')
for a in preço_carrinho:
  lista_precin.append(a)
print('\n')
for b in lista_precin:
  fds += b
print('Total: R$' , round(fds , 2))