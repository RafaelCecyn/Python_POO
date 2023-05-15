# Encapsulamento
'''
public -> Métodos e atributos que podem ser acessados dentro e fora da classe
protected -> Métodos e atributos que podem ser acessados somente dentro da classe ou das filhas daquela classe
private -> Métodos e atributos só está disponível dentro da classe
'''

# class BaseDeDados:
#     def __init__(self):
#         self.dados = {}
        
#     def inserir_cliente(self,id,nome):
#         if 'clientes' not in self.dados:
#             self.dados['clientes'] = {id: nome}
#         else:
#             self.dados['clientes'].update({id: nome})
            
#     def lista_clientes(self):
#         for id,nome in self.dados['clientes'].items():
#             print(id,nome)
            
            
#     def apaga_clientes(self,id):
#         del self.dados['clientes'][id]
        

# bd = BaseDeDados()
# bd.inserir_cliente(1,'Otavio')
# bd.inserir_cliente(2,'Miranda')
# bd.inserir_cliente(3,'Rose')
# bd.dados = 'Uma outra coisa' # Crasha a classe
# bd.inserir_cliente(4,'Amanda')


# CONVENSÃO _ -> PROTECTED (AINDA CONSIGO ACESSAR E ALTERAR A CLASSE)


# class BaseDeDados:
#     def __init__(self):
#         self._dados = {}
        
#     def inserir_cliente(self,id,nome):
#         if 'clientes' not in self._dados:
#             self._dados['clientes'] = {id: nome}
#         else:
#             self._dados['clientes'].update({id: nome})
            
#     def lista_clientes(self):
#         for id,nome in self._dados['clientes'].items():
#             print(id,nome)
            
            
#     def apaga_clientes(self,id):
#         del self._dados['clientes'][id]
        

# bd = BaseDeDados()
# bd.inserir_cliente(1,'Otavio')
# bd.inserir_cliente(2,'Miranda')
# bd.inserir_cliente(3,'Rose')
# bd._dados = 'Uma outra coisa' # Crasha a classe
# bd.inserir_cliente(4,'Amanda')

# CONVENSÃO __ -> PRIVATE (AO TENTAR ACESSAR O __dados ELE NÃO DEIXA E CRIA OUTRO ATRIBUTO)



class BaseDeDados:
    def __init__(self):
        self.__dados = {}
        
    @property
    def dados(self):
        return self.__dados
        
    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            
    def lista_clientes(self):
        for id,nome in self.__dados['clientes'].items():
            print(id,nome)
            
            
    def apaga_clientes(self,id):
        del self.__dados['clientes'][id]
        

bd = BaseDeDados()
bd.inserir_cliente(1,'Otavio')
bd.inserir_cliente(2,'Miranda')
bd.inserir_cliente(3,'Rose')
bd.__dados = 'Uma outra coisa' #   CRIA UM NOVO ATRIBUTO E NÃO DEIXA ALTERAR O ORIGINAL
print(bd.__dados) # IMPRIME O NOVO ATRIBUTO
print(bd._BaseDeDados__dados) # ACESSA O ATRIBUTO ORIGINAL
print(bd.dados)