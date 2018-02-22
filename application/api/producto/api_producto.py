import web
import config
import json


class Api_producto:
    def get(self, id_producto):
        try:
            # http://0.0.0.0:8080/api_producto?user_hash=12345&action=get
            if id_producto is None:
                result = config.model.get_all_producto()
                producto_json = []
                for row in result:
                    tmp = dict(row)
                    producto_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(producto_json)
            else:
                # http://0.0.0.0:8080/api_producto?user_hash=12345&action=get&id_producto=1
                result = config.model.get_producto(int(id_producto))
                producto_json = []
                producto_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(producto_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            producto_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)

# http://0.0.0.0:8080/api_producto?user_hash=12345&action=put&id_producto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,precio):
        try:
            config.model.insert_producto(nombre,precio)
            producto_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_producto?user_hash=12345&action=delete&id_producto=1
    def delete(self, id_producto):
        try:
            config.model.delete_producto(id_producto)
            producto_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_producto?user_hash=12345&action=update&id_producto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_producto, nombre,precio):
        try:
            config.model.edit_producto(id_producto,nombre,precio)
            producto_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            producto_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_producto=None,
            nombre=None,
            precio=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_producto=user_data.id_producto
            nombre=user_data.nombre
            precio=user_data.precio
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_producto)
                elif action == 'put':
                    return self.put(nombre,precio)
                elif action == 'delete':
                    return self.delete(id_producto)
                elif action == 'update':
                    return self.update(id_producto, nombre,precio)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
