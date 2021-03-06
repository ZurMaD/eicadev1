__autor__ = "zurmad"

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
Ult. Modificacion:  01/11/19
Versión:            v0.1.0


Los cambios se modifican en:
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

    # KIVY MD  ----------------------------------------------
    # Barra de navegación
    from kivymd.theming import ThemeManager
    from kivymd.app import MDApp

    # Read and write and other things ----------------------
    import os
    import sys

    # Para archivos de diseño
    from os.path import abspath, dirname, join

    # Conneccion  --------------------------------------------
    import mysql.connector
    from mysql.connector import connection
    from mysql.connector import errorcode
    from mysql.connector import pooling

    # Fechas  ------------------------------------------
    from datetime import date

    # Ploteo de gráficos
    import numpy as np
    import matplotlib.pyplot as plt

    # Abrir enlaces de ayuda  --------------------------------
    # import webbrowser

    print("[  CTRL  ][ LIBRERIAS ]: Se completaron todas correctamente.")

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

"""-------------VARIABLES GLOBALES------------"""


class Ventana_ventas(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.items = [f"Item {i}" for i in range(50)]
        self.cart = []
        self.qty = []
        self.change_info_usuario()

    def change_info_usuario(self):

        info_us = self.ids.info_usuario
        dat = date.today()
        info_us.text = "Controlador     " + dat.strftime("%d/%m/%Y")

    def actualizar_compras(self):
        codigo = self.ids.codigo_producto.text
        contenedor_productos = self.ids.productos

        if self.validacion_codigo():
            detalles = BoxLayout(size_hint_y=None, height=30, pos_hint={"top": 1})
            contenedor_productos.add_widget(detalles)

            code = Label(text=codigo, size_hint_x=0.2, color=(0.06, 0.45, 0.45, 1))
            name = Label(
                text="Product One", size_hint_x=0.3, color=(0.06, 0.45, 0.45, 1)
            )
            qty = Label(text="1", size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            disc = Label(text="0.00", size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            price = Label(text="0.00", size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            total = Label(text="0.00", size_hint_x=0.2, color=(0.06, 0.45, 0.45, 1))
            detalles.add_widget(code)
            detalles.add_widget(name)
            detalles.add_widget(qty)
            detalles.add_widget(disc)
            detalles.add_widget(price)
            detalles.add_widget(total)

            pname = "Product One"
            pprice = 1.00
            pcantidad = str(1)

            self.ids.ultimo_producto_nombre.text = pname
            self.ids.ultimo_producto_precio.text = str(pprice)

            # Actualizar resumen
            resumen_preview = self.ids.resumen
            temp_text = resumen_preview.text
            _temp = temp_text.find("`")

            resumen_venta = "`\n\nTotal\t\t\t\t\t\t\t\t0.00"
            if _temp > 0:
                temp_text = temp_text[:_temp]

            resumen_preview.text = "\n".join(
                [
                    temp_text,
                    pname + "\t\tx" + pcantidad + "\t\t" + str(pprice),
                    resumen_venta,
                ]
            )

    def validacion_codigo(self):
        """
        Esta función valida los códigos
        """
        return True

    def actualizar_compras2(self):
        codigo = self.ids.codigo_producto2.text
        contenedor_productos = self.ids.productos2

        if self.validacion_codigo2():
            detalles = BoxLayout(size_hint_y=None, height=30, pos_hint={"top": 1})
            contenedor_productos.add_widget(detalles)

            code = Label(text=codigo, size_hint_x=0.2, color=(0.06, 0.45, 0.45, 1))
            name = Label(
                text="Product One", size_hint_x=0.3, color=(0.06, 0.45, 0.45, 1)
            )
            qty = Label(text="1", size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            disc = Label(text="0.00", size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            price = Label(text="0.00", size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            total = Label(text="0.00", size_hint_x=0.2, color=(0.06, 0.45, 0.45, 1))
            detalles.add_widget(code)
            detalles.add_widget(name)
            detalles.add_widget(qty)
            detalles.add_widget(disc)
            detalles.add_widget(price)
            detalles.add_widget(total)

            pname = "Product One"
            pprice = 1.00
            pcantidad = str(1)

            self.ids.ultimo_producto_nombre2.text = pname
            self.ids.ultimo_producto_precio2.text = str(pprice)

            # Actualizar resumen
            resumen_preview = self.ids.resumen2
            temp_text = resumen_preview.text
            _temp = temp_text.find("`")

            resumen_venta = "`\n\nTotal\t\t\t\t\t\t\t\t0.00"
            if _temp > 0:
                temp_text = temp_text[:_temp]

            resumen_preview.text = "\n".join(
                [
                    temp_text,
                    pname + "\t\tx" + pcantidad + "\t\t" + str(pprice),
                    resumen_venta,
                ]
            )

    def validacion_codigo2(self):
        """
        Esta función valida los códigos
        """
        return True

    def ayuda(self):
        pass
        # webbrowser.open('http://www.google.com')

    def cerrar_sesion(self):
        print(self.cerrar_sesion.__name__ + ": Inicializado")

        self.parent.parent.current = "ventana_login"

        print(self.cerrar_sesion.__name__ + ": Finalizado")


class controlador(MDApp):
    def __init__(self, **kwargs):
        self.title = "Controlador"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)

    def build(self):
        return Ventana_ventas()


try:
    Builder.load_file("ventanas/controlador/controlador.kv")
except Exception as e:
    print(e)


if __name__ == "__main__":
    aplicacion = controlador()
    aplicacion.run()
