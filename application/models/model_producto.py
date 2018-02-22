import web
import config

db = config.db


def get_all_producto():
    try:
        return db.select('producto')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_producto(id_producto):
    try:
        return db.select('producto', where='id_producto=$id_producto', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_producto(id_producto):
    try:
        return db.delete('producto', where='id_producto=$id_producto', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_producto(nombre,precio):
    try:
        return db.insert('producto',nombre=nombre,
precio=precio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_producto(id_producto,nombre,precio):
    try:
        return db.update('producto',id_producto=id_producto,
nombre=nombre,
precio=precio,
                  where='id_producto=$id_producto',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
