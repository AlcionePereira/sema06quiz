print('''                  Teste de  conhecimentos bíblicos:\n
Quem negou Jesus 3 vezes?.

a) Mateus
b) Pedro
c) Judas  ''')


negou = input('R.').upper().strip()

if negou == 'PEDRO' or negou == 'MATEUS' or negou == 'JUDAS':
    print('  \ncontinuando...\n')
    
    
else:
    print('\n      Você não escolheu nehuma das opções acima.\n')

print(''' ' Qual é o primeiro livro da bíblia?
a) Apocalipse
b) Genesis
d) Êxodo ''')


livro = input('R. ').upper().strip()

if livro == 'GENESIS' or livro == 'APOCALIPSE' or livro == 'ÊXODO' or livro == 'GENESIS' or negou != 'PEDRO' :
    print('\nSegura essa ansiedade.\n')

else:
    print('  \n  "Você precisar ler mais a bíblia!" \n')

print(''' Última perguntinha, essa é a mais difícil.
Qual é o nome da esposa de Abraão?\n
a) Sara
b) Noemi
c) Rute ''')

esposa = input('R .').upper().strip()


if esposa == 'SARA' and  livro == 'GENESIS' and negou == 'PEDRO':
    print('Muito bem!')


else:
    print('Tente novamnete.')




    
    

    



















    
    
          
