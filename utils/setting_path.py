
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

    # Conneccion
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling

    # Read and write and other things
    import os
    import sys

    # Para el path, caso contrario no importa
    # con el path
    from os.path import abspath, dirname, join

    sys.path.append("./.") # 
    # Conectar base de datos
    from utils.database import database_tables as dt
    from utils.database import database_tables_content as dtc

    # Encriptación
    # import bcrypt

    print("[  LOGIN  ][ LIBRERIAS ]: Se completaron todas correctamente.")

except Exception as e:

    print("Error:", e)