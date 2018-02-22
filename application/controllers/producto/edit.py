import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_producto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_producto) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/producto') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_producto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_producto) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/producto') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
        
    

    @staticmethod
    def GET_EDIT(id_producto, **k):
        message = None # Error message
        id_producto = config.check_secure_val(str(id_producto)) # HMAC id_producto validate
        result = config.model.get_producto(int(id_producto)) # search for the id_producto
        result.id_producto = config.make_secure_val(str(result.id_producto)) # apply HMAC for id_producto
        return config.render.edit(result, message) # render producto edit.html

    @staticmethod
    def POST_EDIT(id_producto, **k):
        form = config.web.input()  # get form data
        form['id_producto'] = config.check_secure_val(str(form['id_producto'])) # HMAC id_producto validate
        # edit user with new data
        result = config.model.edit_producto(
            form['id_producto'],form['nombre'],form['precio'],
        )
        if result == None: # Error on udpate data
            id_producto = config.check_secure_val(str(id_producto)) # validate HMAC id_producto
            result = config.model.get_producto(int(id_producto)) # search for id_producto data
            result.id_producto = config.make_secure_val(str(result.id_producto)) # apply HMAC to id_producto
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/producto') # render producto index.html
