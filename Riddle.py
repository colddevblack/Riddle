# Autor: Fabio de Campos Bordin - Dezembro 2015

# -*- coding: utf-8 -*-
from random import randint
print ('WELCOME')
sorteado = randint(1, 100)
bet = 0
while bet != sorteado:
    bet = int(input ('Your number bet 1-100: '))
    if bet == sorteado:
        print ('YOU WIN! Congratulations')
    else:
        if bet > sorteado:
            print ('HIGH')
        else:
            print ('LOW')
print ('GAME OVER!')
