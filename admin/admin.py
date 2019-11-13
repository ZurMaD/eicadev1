__autor__='zurmad'

version="""
https://trello.com/b/xdE3hSr0/eica
"""
try:
    # KIVY ----------------------------------------------
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
    from kivy.clock import Clock
    # Para poner botones de mas de 2 
    from kivy.uix.boxlayout import BoxLayout
    # Para los archivos .kv
    from kivy.lang.builder import Builder
    # Para las pantallas
    from kivy.uix.widget import Widget 
    # Cambiar tamaños dinamicamente
    from kivy.uix.floatlayout import FloatLayout
    
    ## KIVY MD  ----------------------------------------------
    # Barra de navegación
    from kivymd.theming import ThemeManager    
    
    # Read and write and other things ----------------------
    import os
    import sys
    # Para archivos de diseño
    from os.path import abspath,dirname,join
    
    # Conneccion  --------------------------------------------
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling
    
    # Encriptación  ------------------------------------------
    import bcrypt
    
    # Abrir enlaces de ayuda  --------------------------------
    import webbrowser    
    
    print("LIBRERIAS: Se completaron todas correctamente.")

except Exception as e:
    
    print("Error:",e)


# Install python 3.7
# pip install mysql-connector 
# pip install kivy #http://bit.ly/2pZQzYd
# pip install pandas
# pip install numpy
# pip install bcrypt
# pip install tkcalendar
# pip install matplotlib


class Ventana_admin(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
       
    
    def cerrar_sesion(self):
        print (self.cerrar_sesion.__name__+": Inicializado")
        
        self.parent.parent.current="screen_login"        
        
        print (self.cerrar_sesion.__name__+": Finalizado")
    
    def ayuda(self):
        webbrowser.open('http://www.google.com')

class admin(App):
    # NavBar
    theme_cls=ThemeManager()
    #http://bit.ly/2PzQAga
    # logos http://bit.ly/36sSPaT
    
    def build(self):        
        return Ventana_admin()



try:
    Builder.load_file("admin/admin.kv")
except Exception as e:
    print(e)
    
    
if __name__ == "__main__":
    aplicacion=admin()
    aplicacion.run()
