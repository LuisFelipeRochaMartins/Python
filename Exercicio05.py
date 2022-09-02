#Crie um algoritmo que msotre na tela uma contagem regressiva, para estouro de fogo, indo de 10 até 0.#
import time
for k in range (10,-1,-1):
    #flush=True, para que a cada iteração do loop, imprima o valor de 'k' na tela.
    print(k ,' ',end='' ,flush=True)
    time.sleep(1)
