palavra = 'paralelepipedo'
letras_digitadas = []
chances = 10
ganhou = False

while ganhou == False:
       
    for letra in palavra:
        if letra.lower() in letras_digitadas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print(f'Você tem {chances} chances!')


    letra_tentativa = input('Digite uma letra: ')
    letras_digitadas.append(letra_tentativa.lower())


    if letra_tentativa.lower() not in palavra.lower():
        chances = chances -1
        
    if chances == 0 or ganhou:
        break

    ganhou = True
    
    for letra in palavra:
        if letra.lower() not in letras_digitadas:
            ganhou = False
        
if ganhou: 
        print(f'Parabéns, você ganhou o jogo! A palavra era: {palavra}')
else:
        print(f'Você perdeu, a palavra era: {palavra}!')