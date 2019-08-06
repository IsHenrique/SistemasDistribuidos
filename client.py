import xmlrpc.client


s = xmlrpc.client.ServerProxy('http://localhost:8000', allow_none=True)

#Adicionar um novo novo passando o Nome, Reino, Nome Cientifico, Periodo e Descrição
print(s.fossilnovo('Teste', 'Teste', 'Teste', 'Teste', 'Teste'))

#Procurar um fóssil por nome
print(s.listarfossil('Teste'))

#Deletar o fossil passando o ID
print(s.deletefossil())

# Printa todos os metodos existentes no RPC
print(s.system.listMethods())
