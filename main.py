from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook

linha = '---------------------------------'
# comp = Computador()
# comp.cadastrar()
print(linha)

desk = Desktop()
desk.cadastrar()

desk.modelo = 'Dell'
desk.cor = 'Cinza'
desk.preco = 1000.00
desk.potenciaDaFonte = 12

desk.getinformacoes()

print(linha)

note = Notebook('Dell', 'Prata', 1000.00, 120)
note.cadastrar()

note.modelo = 'Dell'
note.cor = 'Cinza'
note.preco = 2000.00
note.potenciaDaFonte = 120

note.getinformacoes()


print(linha)
