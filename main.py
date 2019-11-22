__autor__='zurmad'

version="""
EICA CONTROL DE INVENTARIO
Descripción: 
Este programa hace control de inventario mediante el reporte
de gastos diarios, también muestra ganancias y reportes
útiles para los gerentes.
Se usa Mysql en la nube, las credenciales están más abajo

Autor:              Pablo Díaz
Github:             github.com/zurmad
Correo:             pablo.diazv@pucp.edu.pe
Ult. Modificacion:  22/11/19
Versión:            1.0.003


Los cambios se modifican en:
https://trello.com/b/xdE3hSr0/eica

"""

version_eica="1.0.003"
# Install python 3.7
# pip install mysql-connector 
# pip install kivy 
# #http://bit.ly/2pZQzYd

# pip install pandas
# pip install numpy
# pip install bcrypt
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
    #import bcrypt
    
    # Local py files
    from login.login import Ventana_login    
    from controlador.controlador import Ventana_ventas
    from admin.admin import Ventana_admin
    from utils.database import conectar_base_datos
    
    print("LIBRERIAS: Se completaron todas correctamente.")

except Exception as e:
    
    print("-Error:",e)

class gestionar_ventanas(BoxLayout):
    
    # Add screens to main
    login_widget=Ventana_login()
    admin_widget=Ventana_admin()
    ventas_widget=Ventana_ventas()    
    
    def __init__(self, **kwargs):        
        super().__init__(**kwargs)

        self.ids.screen_login.add_widget(self.login_widget)
        self.ids.screen_ventas.add_widget(self.admin_widget)
        self.ids.screen_admin.add_widget(self.ventas_widget)        

class main(App):
    theme_cls=ThemeManager()
    def build(self):
        return gestionar_ventanas()

if __name__ == "__main__":
    main().run()