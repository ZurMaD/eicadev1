__autor__='zurmad'

# Install python 3.7
# pip install mysql-connector 
# pip install kivy 
# #http://bit.ly/2pZQzYd

# pip install pandas
# pip install numpy
# pip install bcrypt
# pip install tkcalendar
# pip install matplotlib

# For navigation bar
# pip3 install kibymd

try:
    #Generales
    import kivy
    from  kivy.app import App
    # Corremos la version de kivy
    kivy.require("1.11.1")  
    # Los labels
    from kivy.uix.label import Label
    # Para el orden de los labels
    from kivy.uix.gridlayout import GridLayout
    # Para los textos
    from kivy.uix.textinput import TextInput
    # Para las entradas de texto
    from kivy.uix.button import Button
    # Para realizar estilos a la pantalla
    from kivy.uix.screenmanager import ScreenManager,Screen 
    # Para el scheduler 
    # http://bit.ly/36vNJL9
    from kivy.clock import Clock 
    # Para poner botones de mas de 2 
    from kivy.uix.boxlayout import BoxLayout
    # Para los archivos .kv
    from kivy.lang.builder import Builder
    # Para las pantallas
    from kivy.uix.widget import Widget 
    # Cambiar tamaños dinamicamente
    from kivy.uix.floatlayout import FloatLayout
    
    # Read and write and other things
    import os
    import sys
    # Para archivos de diseño
    from os.path import abspath,dirname,join
    
    # Conneccion
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling
    
    # Encriptación
    import bcrypt
    
    # Conectar base de datos
    from utils.database import conectar_base_datos
    
    print("LIBRERIAS: Se completaron todas correctamente.")

except Exception as e:
    
    print("Error:",e)



"""-------------VARIABLES GLOBALES------------"""


Builder.load_file("login/login.kv")


#class conectar_base_datos:


class Ventana_login(BoxLayout):
    
       
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def iniciar_sesion(self):
        
        print(self.iniciar_sesion.__name__,': {}'.format("Inicializando"))
        
        # Get the texts
        usuario=self.ids.usuario
        contrasenha=self.ids.contrasenha
        self.mensaje_login=self.ids.mensaje
        
        u=usuario.text
        c=contrasenha.text
        
        
        print(self.iniciar_sesion.__name__,': usuario: {}, contraseña:{}'.format(u,
                                                            c))
        
        ga=Clock.schedule_once(self.conectar,3)
        print(ga)

        print(self.iniciar_sesion.__name__,': {}'.format("Finalizando"))

    def validar_texto(self,u,c):
        val=((u!='')and(c!=''))
        return val
    
    def conectar(self):
        
        usuario=self.ids.usuario
        contrasenha=self.ids.contrasenha
        self.mensaje_login=self.ids.mensaje
        
        u=usuario.text
        c=contrasenha.text
        
        print(self.conectar.__name__+": {}".format("Inicializando")) 
        
        if self.validar_texto(u,c)==True:
            
            self.mensaje_login.text='[color=#00FF00]Cargando...[/color]'
            
            try:
                db=conectar_base_datos()
                respuesta=db.get_contrasenha_encriptada(usuario)
                print(self.conectar.__name__+":",respuesta)
                #aplicacion.Ventana_inicio_gerencia.actualizar_texto("Bienvenido")
                
                verification = self.check_password(contrasenha.encode('utf-8'), eval(respuesta[0][0]))
                
                if verification:
                    #aplicacion.screen_manager.current="Ventana_inicio_gerencia"
                    #Clock.schedule_once(self.siguiente_pagina(),0.5)
                    pass
                else:
                    #aplicacion.screen_manager.current="Ventana_login"
                    print(self.conectar.__name__+":",mensajes_global['MSG_4'])

            except Exception as e:
                self.mensaje_login.text=str(e)
        #print(self.conectar.__name__+":", mensajes_global['MSG_4'])
        #aplicacion.screen_manager.current="Ventana_login"
        else:
            self.mensaje_login.text='[color=#FF0000] Usuario y/o contraseña incorrecto[/color]'
               
        print(self.conectar.__name__+": {}".format("Finalizando")) 

    def siguiente_pagina(self):
        aplicacion.screen_manager.current="Ventana_inicio_gerencia"

    def get_hashed_password(self, plain_text_password):
        """
        Functions:
        get_hashed_password
        check_password
        From http://bit.ly/2YijKB5
        """
        
        """
        Hash a password for the first time
        (Using bcrypt, the salt is saved into the hash itself)
        """
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    def check_password(self, plain_text_password, hashed_password):
        """
        Check hashed password. Using bcrypt, the salt is saved into the hash itself
        """
        return bcrypt.checkpw(plain_text_password, hashed_password)

        
class login (App):
    
    def build(self):
        
        return Ventana_login()


 
if __name__=="__main__":
    

    aplicacion=login()
    aplicacion.run()

