__autor__ = 'zurmad'

version = """
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

version_eica = "1.0.003"
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

    # Local py files
    # VENTANAS
    from ventanas.login2.login import Ventana_login
    from ventanas.controlador.controlador import Ventana_ventas
    from ventanas.admin.admin import Ventana_admin
    from ventanas.chooser.chooser import Ventana_chooser

    print("LIBRERIAS: Se completaron todas correctamente.")

except Exception as e:

    print("-Error:", e)


class gestionar_ventanas(BoxLayout):

    # Add screens to main
    # Add screnss and windows here
    login_widget = Ventana_login()
    ventas_widget = Ventana_ventas()
    admin_widget = Ventana_admin()
    chooser_widget = Ventana_chooser()

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.ids.ventana1.add_widget(self.login_widget)
        self.ids.ventana2.add_widget(self.chooser_widget)
        self.ids.ventana3.add_widget(self.ventas_widget)
        self.ids.ventana4.add_widget(self.admin_widget)


class main(App):

    theme_cls = ThemeManager()  # Using kivymd is necessary
    theme_cls.primary_palette = 'BlueGray'  # same

    def build(self):
        return gestionar_ventanas()


if __name__ == "__main__":
    main().run()
