__autor__ = 'zurmad'

version = """
https://trello.com/b/xdE3hSr0/eica
"""


try:
    # KIVY ----------------------------------------------
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
    # Para las tablas
    from kivy.uix.recycleview import RecycleView
    from kivy.uix.recycleview.views import RecycleDataViewBehavior
    from kivy.uix.recycleboxlayout import RecycleBoxLayout
    from kivy.uix.recyclegridlayout import RecycleGridLayout
    from kivy.uix.behaviors import FocusBehavior
    from kivy.uix.recycleview.layout import LayoutSelectionBehavior
    from kivy.properties import ObjectProperty
    from kivy.properties import BooleanProperty

    # KIVY MD  ----------------------------------------------
    # Barra de navegación
    # Para botones interactivos
    from kivy.factory import Factory
    from kivymd.theming import ThemeManager
    from kivymd.app import MDApp
    

    # Read and write and other things ----------------------
    import os
    import sys

    # Conneccion  --------------------------------------------
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling

    # Array -------------------------------------------------
    import numpy as np

    # Para archivos de diseño
    from os.path import abspath, dirname, join

    sys.path.append("./.")
    # Conectar base de datos / Scripts locales
    from utils.database import database_tables as dt
    from utils.database import database_tables_content as dtc
    from utils.database import conectar_base_datos



    # Encriptación  ------------------------------------------
    # import bcrypt

    # Abrir enlaces de ayuda  --------------------------------
    # import webbrowser    # Dont supported on Android

    print("[  ADMIN  ][ LIBRERIAS ]: Se completaron todas correctamente.")

except Exception as e:

    print("Error:", e)


# Install python 3.7
# pip install mysql-connector
# pip install kivy #http://bit.ly/2pZQzYd
# pip install pandas
# pip install numpy
# pip install bcrypt
# pip install tkcalendar
# pip install matplotlib

################################
# New table from http://bit.ly/2tn0Krj

d = dt[9]
u = list(dtc[d].values())

u = ['Cod', 'Plato', 'P.V.', 'P.C.', 'Tipo', 'Img', '', '']

items = ['0', "111", "15", "12", "Sopa", "IMG0", "EDITAR", "BORRAR",
         '1', "222", "14", "12", "Dieta", "IMG1", "EDITAR", "BORRAR",
         '2', "333", "13", "12", "Carnes", "IMG2", "EDITAR", "BORRAR",
         '3', "444", "14", "12", "Otros", "IMG3", "EDITAR", "BORRAR"]

tabla_platos = u+items

################################
class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in tabla_platos]
################################


class Ventana_admin(BoxLayout):
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)

    def tipo_plato_selected(self):

        print(self.tipo_plato_selected.__name__+": Inicializado")

        # Show nombre de platos dependiendo de categoría

        print(self.tipo_plato_selected.__name__+": Finalizado")

    def busqueda_plato(self):
        """
        Esta función busca el plato por nombre
        y muestra en una tabla toda la información
        """
        
        # respuesta = conectar_base_datos().get_all_tipos_de_platos()
        # self.ids.md_tipo_plato.items=respuesta

        print(self.busqueda_plato.__name__+": Inicializado")
        try:
            respuesta = conectar_base_datos().get_by_nombre_platos("no_borrar")
            row1=respuesta[0]
            x=np.asarray(row1)
            y=np.asarray(u)
            contenido=np.concatenate((y,x),axis=None)
            
            self.ids.tabla1.data=[{'text': str(x)} for x in contenido]

            print(respuesta)
        except Exception as e:
            #self.mensaje_login.text = str(e)
            print(self.busqueda_plato.__name__,e)

        print(self.busqueda_plato.__name__+": Finalizado")        

    def cerrar_sesion(self):

        print(self.cerrar_sesion.__name__+": Inicializado")

        self.parent.parent.current = "ventana_login"

        print(self.cerrar_sesion.__name__+": Finalizado")

    def ayuda(self):
        # webbrowser.open('http://www.google.com')
        # Android dont support webbrowser library
        print("Android dont supp webbrowser")
        pass


class admin(MDApp):

    def __init__(self, **kwargs):
        self.title = "Administrador"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)


    def build(self):
        return Ventana_admin()

try:
    Builder.load_file("ventanas/admin/admin.kv")
except Exception as e:
    print(e)


if __name__ == "__main__":
    aplicacion = admin()
    aplicacion.run()
