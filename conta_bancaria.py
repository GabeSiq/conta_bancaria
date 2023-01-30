# Class define a "RECEITA". A classe vai receber o nome, pode ser qualquer palavra.
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        # INIT - Em algumas linguaguagens (como java), esta função recebe o nome de construtor. o Python não se enquadra
        # neste caso, porque uma função construtora não é um equivalente exato do método construtor.
        print("Construindo objeto ... {}".format(self))
        # self é a referência que sabe encontrar o objeto construído em memória.
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))
        # DEF puxa saldo e printa saldo e titular, puxando direto da memória utilizando self.

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f"Você sacou {valor}")
        else:
            print(f"O {valor} passou o limite")

    def transfere(self, valor, destino):
        self.saca(valor)
        self.deposita(valor)

    # Esses métodos a seguir são conhecidos como GET, por isso devem iniciar(boas práticas/ nomenclatura padrão) com GET.
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # Assim como temos os GETs, também temos os SETs (boas práticas/nomenclatura padrão) para criar funções de devolver.

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Os metodos que não utilizam o objeto, são objetos estaticos, observe que esta sem o self
    @staticmethod
    def codigo_do_banco():
        return "001"

    @staticmethod
    def todos_codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
