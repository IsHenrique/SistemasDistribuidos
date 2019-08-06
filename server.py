from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from pymongo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps
from bson.objectid import ObjectId


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()
    cliente = MongoClient('localhost', 27017)
    banco = cliente.museu
    collection = banco.items

    class MyFuncs:
        def fossilnovo(self, nome, reino, nomecientifico, periodo, descricao):
            dicionario = {
                "tipo": "2",
                "nome": nome,
                "reino": reino,
                "nomecientifico": nomecientifico,
                "periodo": periodo,
                "descricao": descricao
            }
            x = collection.insert_one(dicionario)
            y = ('Fossil inserido com sucesso. ID do fossil novo:', x.inserted_id)
            return dumps(y)
        def listarfossil(self, nome):
            g = collection.find_one({"nome": nome})
            if g == None:
                return('Fossil não encontrado')
            else: 
                p = ('Fossil encontrado:')
                r = collection.find_one({"nome": nome})
            return (p, dumps(r))
        def deletefossil(self, idfossil):
            h = collection.delete_one({'_id': ObjectId(idfossil)})
            return ('Fossil deletado com sucesso')

    server.register_instance(MyFuncs())
    server.register_multicall_functions()

    # Run the server's main loop
    server.serve_forever()