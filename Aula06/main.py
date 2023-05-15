from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = caneta # recebe o objeto inteiro de caneta
escritor.ferramenta.escrever()

del escritor # deleta a instância escritor  
print(caneta.marca)
maquina.escrever()