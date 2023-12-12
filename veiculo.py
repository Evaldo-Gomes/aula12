#Classe de teste veículo

class Veiculo(object):
    # Método construtor
    def __int__(self, marca, modelo, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade

    # Encapsulamento
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        return self.modelo

    def getModelo(self):
        return self.modelo

    def setCor(self, cor):
        self.cor = cor

    def getCor(self):
        return self.cor

    def setVelocidade(self, velocidade):
        return self.velocidade

    def getVelocidade(self):
        return self.velocidade

    # Retorno de dados da classe: Transforma os dados da classe em uma cadeia de string
    def __str__(self):
        return (
            '\n Marca: ' + str(self.getMarca()) +
            '\n Modelo: ' + str(self.getModelo()) +
            '\n Cor: ' + str(self.getCor()) +
            '\n Velocidade: ' + str(self.getVelocidade() * 'km/h')
        )

