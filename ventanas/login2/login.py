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
    
    # Para botones interactivos
    from kivy.factory import Factory
    from kivymd.theming import ThemeManager
    
    
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

class Ventana_login(BoxLayout):
    
       
    def __init__(self,**kwargs):
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
        

        
class login (App):
    # http://bit.ly/2pOTIKD -- KIVY
    theme_cls=ThemeManager()
    theme_cls.primary_palette='BlueGray'
    
    def build(self):        
        return Ventana_login()


try:
    Builder.load_file("ventanas/login2/login.kv")
except Exception as e:
    print(e)

if __name__=="__main__":    

    aplicacion=login()
    aplicacion.run()