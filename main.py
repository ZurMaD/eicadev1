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
Correo:             pablo.diazva@pucp.edu.pe
Ult. Modificacion:  20/12/19
Versión:            1.0.004


Los cambios se modifican en:
https://trello.com/b/xdE3hSr0/eica

"""

version_eica = "1.0.004"

try:
    # KIVY ----------------------------------------------
    # Para realizar estilos a la pantalla
    from kivy.uix.screenmanager import ScreenManager, Screen
    # Para poner botones de mas de 2
    from kivy.uix.boxlayout import BoxLayout
    # Para los archivos .kv
    from kivy.lang.builder import Builder
    # Para las pantallas
    from kivy.uix.widget import Widget
    # Factory
    from kivy.factory import Factory

    # KIVY MD  ----------------------------------------------
    # Barra de navegación
    # Para botones interactivos
    
    from kivymd.theming import ThemeManager
    from kivymd.app import MDApp

    # LOCAL FYLES - WINDOWS ----------------------------------
    # Ventanas (Screens)
    from ventanas.login2.login import Ventana_login
    from ventanas.chooser.chooser import Ventana_chooser
    from ventanas.controlador.controlador import Ventana_ventas
    from ventanas.admin.admin import Ventana_admin

    print("[  MAIN  ][ LIBRERIAS ]: Se completaron todas correctamente.")

except Exception as e:

    print("[  MAIN  ][ LIBRERIAS ]:", e)


class Gestionar_ventanas(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        
        # Add screens to main
        widget_login = Ventana_login()
        widget_chooser = Ventana_chooser()
        widget_ventas = Ventana_ventas()
        widget_admin = Ventana_admin()

        # Add screns to windows here
        self.ids.ventana1.add_widget(widget_login)
        self.ids.ventana2.add_widget(widget_chooser)
        self.ids.ventana3.add_widget(widget_ventas)
        self.ids.ventana4.add_widget(widget_admin)


class main(MDApp):

    def __init__(self, **kwargs):
        self.title = "Inicio"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)

    def build(self):
        self.items = [f"Item {i}" for i in range(50)]
        return Gestionar_ventanas()

# NOT NEEDED BUILDER IN THE MAIN FILE
# try:
#     Builder.load_file("main.kv")
# except Exception as e:
#     print(e)

if __name__ == "__main__":
    aplicacion = main()
    aplicacion.run()