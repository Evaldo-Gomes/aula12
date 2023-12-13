# Arquivo com código de teste da classe veículo

from veiculo import Veiculo

# Criar um objeto com suas características ("Como construir o objeto)
minhaCaranga = Veiculo('Fiat', '147', 'Amarelo', 0)
# Exibindo a minha caranga
print('\n\t\t\t -- Minha Caranga  --')
print(minhaCaranga)

# Acelerando a minha caranga
for i in range(0, 200):
    minhaCaranga.acelerar()
# Exibindo a minha caranga acelerada
print('\n\t\t\t -- Minha Caranga Acelerada  --')
print(minhaCaranga)

# Freando a minha caranga
for i in range(0, 200):
    minhaCaranga.frear()

# Exibindo a minha caranga freada
print('\n\t\t\t -- Minha Caranga Freada --')
print(minhaCaranga)