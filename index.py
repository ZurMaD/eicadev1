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
Ult. Modificacion:  28/10/19
Versión:            v1.0.0


Los cambios se modifican en:
https://trello.com/b/xdE3hSr0/eica

"""
try:
    #Genrales
    import kivy
    from  kivy.app import App  
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
    
    # Read and write and other things
    import os
    import sys
    
    # Conneccion
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling
    
    
    print("LIBRERIAS: Se completaron todas correctamente.")
except Exception as e:
    print("Error:",e)

kivy.require("1.10.1")

configuracion = {'user': 'pc1',
                 'password': 'pc1',
                 'host': '104.198.229.44',
                 'database': 'rest',
                 'raise_on_warnings': True}


class Login(GridLayout):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2
        
        self.add_widget(Label(text="Usuario:"))
        
        self.usuario=TextInput(multiline=False)
        self.add_widget(self.usuario)
        
        self.add_widget(Label(text="Contraseña:"))
        
        self.contrasenha=TextInput(multiline=False)
        self.add_widget(self.contrasenha)

        self.boton_iniciar_sesion=Button(text="Iniciar sesion")
        self.boton_iniciar_sesion.bind(on_press=self.iniciar_sesion)
        self.add_widget(self.boton_iniciar_sesion)
    
    def iniciar_sesion(self,instance):
        
        usuario=self.usuario.text
        contrasenha=self.contrasenha.text
        
        print(self.iniciar_sesion.__name__,': {},{}'.format(usuario,contrasenha))
        info="ga"
        
        aplicacion.info_page.update_info(info)
        #Cambiamos de página
        aplicacion.screen_manager.current="Info"
        Clock.schedule_once(self.conectar,3)
    
    def conectar(self,_):
        
        usuario=self.usuario.text
        contrasenha=self.contrasenha.text
        print("Conectando")
        aplicacion.screen_manager.current="Ventana_inicio_gerencia"
        
        xd=conectar_base_datos()
        ga=xd.get_rows()
        x=0

class InfoPage(GridLayout):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.cols=1
        
        self.message=Label(halign="center",
                           valign="middle",
                           font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
        
    def update_info(self,message):
        
        self.message.text=message
    
    def update_text_width(self,*_):
        self.message.text_size=(self.message.width*0.9,None)

class Ventana_inicio_gerencia(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        
class ControlVentanas (App):
    
    def build(self):
        
        self.screen_manager=ScreenManager()
        
        self.login=Login()        
        screen=Screen(name="Connect")
        screen.add_widget(self.login)
        self.screen_manager.add_widget(screen)

        self.info_page=InfoPage()
        #Indicamos que la clase info_page es la ventana
        screen=Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        
        self.Ventana_inicio_gerencia=Ventana_inicio_gerencia()
        #Indicamos que la clase info_page es la ventana
        screen=Screen(name="Ventana_inicio_gerencia")
        screen.add_widget(self.Ventana_inicio_gerencia)
        self.screen_manager.add_widget(screen)
    
        return self.screen_manager


class conectar_base_datos:

    def __init__(self):
        try:
            self.db = mysql.connector.connect(**configuracion)
            self.c = self.db.cursor()
        except Exception as e:
            print(conectar_base_datos.__name__+":",e)
            
    def get_rows(self,search = ""):
        try:
            query=('SELECT {} FROM platos'.format('*'))
            self.c.execute(query)
            return self.c.fetchall()
        except Exception as e:
            print (self.get_rows.__name__+":",e)

    
if __name__=="__main__":
    aplicacion=ControlVentanas()
    aplicacion.run()

