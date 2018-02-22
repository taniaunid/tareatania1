import web
import config

db = config.db


def get_all_cliente():
    try:
        return db.select('cliente')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_cliente(id_cliente):
    try:
        return db.select('cliente', where='id_cliente=$id_cliente', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_cliente(id_cliente):
    try:
        return db.delete('cliente', where='id_cliente=$id_cliente', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_cliente(nombre,direccion,telefono):
    try:
        return db.insert('cliente',nombre=nombre,
direccion=direccion,
telefono=telefono)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_cliente(id_cliente,nombre,direccion,telefono):
    try:
        return db.update('cliente',id_cliente=id_cliente,
nombre=nombre,
direccion=direccion,
telefono=telefono,
                  where='id_cliente=$id_cliente',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
