multa = False
while multa == False:
    velocidade_max = 80
    velocidade = int(input('Qual era a velocidade do carro? '))
    if velocidade <= velocidade_max:
        print('Não houve multa.')
    elif velocidade > velocidade_max and velocidade <= velocidade_max + 10:
        print('Multa leve.')
    elif velocidade >= velocidade_max +11 and velocidade <= velocidade_max + 20:
        print('Multa grave.')
    elif velocidade > velocidade_max + 20:
        print('Multa gravíssima.')
