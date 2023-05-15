from pessoa import Pessoa

p1 = Pessoa('Luiz',29) # Instanciando a pessoa 1
# p2 = Pessoa() # Instanciando a pessoa 2

# print(p1.nome)

# p1.outro_metodo()

# p1.comer('Maça')
# p1.parar_comer()
# p1.parar_comer()
# p1.comer('Maça')

# p1.comer('Maça')
# p1.falar('POO')
# p1.parar_comer()
# p1.falar('POO')
# p1.comer('alimento')
# p1.parar_falar()
# p1.comer('alimento')

p2 = Pessoa('Joao',32)

p1.falar('POO')
p2.comer('sorvete')
p1.comer('churrasco')

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())