import web
import config
import json


class Api_cliente:
    def get(self, id_cliente):
        try:
            # http://0.0.0.0:8080/api_cliente?user_hash=12345&action=get
            if id_cliente is None:
                result = config.model.get_all_cliente()
                cliente_json = []
                for row in result:
                    tmp = dict(row)
                    cliente_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(cliente_json)
            else:
                # http://0.0.0.0:8080/api_cliente?user_hash=12345&action=get&id_cliente=1
                result = config.model.get_cliente(int(id_cliente))
                cliente_json = []
                cliente_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(cliente_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            cliente_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(cliente_json)

# http://0.0.0.0:8080/api_cliente?user_hash=12345&action=put&id_cliente=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,direccion,telefono):
        try:
            config.model.insert_cliente(nombre,direccion,telefono)
            cliente_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(cliente_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_cliente?user_hash=12345&action=delete&id_cliente=1
    def delete(self, id_cliente):
        try:
            config.model.delete_cliente(id_cliente)
            cliente_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(cliente_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_cliente?user_hash=12345&action=update&id_cliente=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_cliente, nombre,direccion,telefono):
        try:
            config.model.edit_cliente(id_cliente,nombre,direccion,telefono)
            cliente_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(cliente_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            cliente_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(cliente_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_cliente=None,
            nombre=None,
            direccion=None,
            telefono=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_cliente=user_data.id_cliente
            nombre=user_data.nombre
            direccion=user_data.direccion
            telefono=user_data.telefono
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_cliente)
                elif action == 'put':
                    return self.put(nombre,direccion,telefono)
                elif action == 'delete':
                    return self.delete(id_cliente)
                elif action == 'update':
                    return self.update(id_cliente, nombre,direccion,telefono)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
