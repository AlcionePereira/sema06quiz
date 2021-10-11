def mantendo_pontuação(score):
    return acertou + 1
print('Esse é um jogo de perguntas e resposta diversificado\n')

    
score = 0
scorea = 1


print('''Qual personagem de desenho animado diz:
"Olá velhinho" ?''')


desenho = str(input('R.').upper().strip())

if desenho == 'PERNALONGA':
    print('Você tem {} ponto\n' .format(scorea))


else:
    print('Você tem {} ponto.\n' .format(score))
    


módulo = input('No Python onde encontramos o módulo math? \nR.')


if módulo == 'biblioteca' and  desenho == 'PERNALONGA':
    print('Você tem 2 pontos.\n')
    



elif módulo == 'biblioteca' and desenho != 'PERNALONGA' or módulo != 'biblioteca' and desenho == 'PERNALONGA': 
    print('você tem {} \n'.format(scorea))

    
    
else:
    print(score)
    

print('Quem é o único que merece toda honra e toda glória? ')

criador = input('R.').upper().strip()


if criador == 'DEUS' and módulo == 'biblioteca' and  desenho == 'PERNALONGA':
    print('       Fim de jogo...\nvocê tem {} pontos.' .format(scorea + 2))
    
    

elif criador == 'DEUS' and módulo == 'biblioteca' and desenho != 'PERNALONGA' or criador == 'DEUS'and desenho == 'PERNALONGA' and módulo != 'biblioteca':
    print('       Fim de jogo.\nVocê tem {} pontos.' .format(scorea+1))

    

elif criador == 'DEUS' and módulo != 'biblioteca' and desenho != 'PERNALONGA'or criador != 'DEUS' and módulo != 'biblioteca' and desenho == 'PERNALONGA' or criador != 'DEUS' and desenho != 'PERNALONGA'and módulo == 'biblioteca':
   print('        Fim de jogo.\nVocê tem {} ponto.' .format(scorea))
    



else:
    print('       Fim de jogo.\n .Você tem {}pontos'.format(score))
    







    


    
    




    
   
    




                      



