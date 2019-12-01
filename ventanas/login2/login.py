__autor__ = 'zurmad'

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
# pip3 install kivymd

try:
    # Generales
    import kivy
    from kivy.app import App
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
    from kivy.uix.screenmanager import ScreenManager, Screen
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

    # Para botones interactivos
    from kivy.factory import Factory
    from kivymd.theming import ThemeManager

    # Read and write and other things
    import os
    import sys
    # Para archivos de diseño
    from os.path import abspath, dirname, join

    # Conneccion
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling

    # Conectar base de datos
    from utils.database import conectar_base_datos

    print("-------------------------------BYCRIPT--------------------")
    # Encriptación
    import bcrypt

    print("LIBRERIAS: Se completaron todas correctamente.")

except Exception as e:

    print("Error:", e)


class Ventana_login(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_password(self, field, button):
        """
        Called when you press the right button in the password field
        for the screen TextFields.

        instance_field: kivy.uix.textinput.TextInput
        instance_button: kivymd.button.MDIconButton

        """

        # Show or hide text of password, set focus field
        # and set icon of right button.
        field.password = not field.password
        field.focus = True
        button.icon = 'eye' if button.icon == 'eye-off' else 'eye-off'

    def iniciar_sesion(self):

        print(self.iniciar_sesion.__name__, ': {}'.format("Inicializando"))

        # Get the texts
        usuario = self.ids.usuario
        contrasenha = self.ids.contrasenha
        self.mensaje_login = self.ids.mensaje

        u = usuario.text
        c = contrasenha.text

        print(self.iniciar_sesion.__name__,
              ': usuario: {}, contraseña:{}'.format(u, c))

        Clock.schedule_once(lambda dt: self.conectar(), 2)

        print(self.iniciar_sesion.__name__, ': {}'.format("Finalizando"))

    def validar_texto(self, u, c):
        val = ((u != '')and(c != ''))
        return val

    def siguiente_pagina(self):
        aplicacion.screen_manager.current = "Ventana_inicio_gerencia"

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

    def conectar(self):
        usuario = self.ids.usuario
        contrasenha = self.ids.contrasenha
        self.mensaje_login = self.ids.mensaje

        u = usuario.text
        c = contrasenha.text

        print(self.conectar.__name__+': {}'.format("Inicializando"))

        if self.validar_texto(u, c) == True:

            self.mensaje_login.text = '[color=#00FF00]Cargando...[/color]'

            try:
                respuesta = conectar_base_datos().get_by_user_contrasenha('elio')
                print(self.conectar.__name__+":", respuesta)
                # aplicacion.Ventana_inicio_gerencia.actualizar_texto("Bienvenido")
                print(c.encode('utf-8'), respuesta[0][0])

                verification = True
                # verification = self.check_password(c.encode('utf-8'), eval(respuesta[0][0]))

                if verification:
                    """
                    Aquí se ha verificado la sesión y se muestra la siguiente ventana
                    """
                    print(self.conectar.__name__+": INICIO DE SESIÓN EXITOSO")

                    self.parent.parent.current = 'ventana_chooser'

                else:

                    print(self.conectar.__name__+": INICIO DE SESIÓN FALLIDO")

            except Exception as e:
                self.mensaje_login.text = str(e)
        #print(self.conectar.__name__+":", mensajes_global['MSG_4'])
        # aplicacion.screen_manager.current="Ventana_login"
        else:
            self.mensaje_login.text = '[color=#FF0000] Usuario y/o contraseña incorrecto[/color]'

        print(self.conectar.__name__+": {}".format("Finalizando"))


class login (App):
    # http://bit.ly/2pOTIKD -- KIVY
    theme_cls = ThemeManager()

    def build(self):
        return Ventana_login()


try:
    Builder.load_file("ventanas/login2/login.kv")
except Exception as e:
    print(e)

if __name__ == "__main__":

    aplicacion = login()
    aplicacion.run()
