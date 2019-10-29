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

version_eica="1.0.0"

# Install python 3.7
# pip install mysql-connector 
# pip install kivy #http://bit.ly/2pZQzYd
# pip install pandas
# pip install numpy
# pip install bcrypt
# pip install tkcalendar
# pip install matplotlib


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
    # Para menubar
    
    # Read and write and other things
    import os
    import sys
    
    # Conneccion
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling
    
    # Encriptación
    import bcrypt
    
    print("LIBRERIAS: Se completaron todas correctamente.")
except Exception as e:
    print("Error:",e)

kivy.require("1.10.1")

"""-------------VARIABLES GLOBALES------------"""


configuracion = {'user': 'pc1',
                 'password': 'pc1',
                 'host': '104.198.229.44',
                 'database': 'rest',
                 'raise_on_warnings': True}


nombre_ventanas = {'Ventana_login',
                   'Ventana_ejemplo',
                   'Ventana_inicio_gerencia',
                   'Ventana_compras_ingresar_compra',
                   'Ventana_inventario_disponibilidad_platos',
                   'Ventana_reportes_inventario_disponibilidad',
                   'Ventana_ventas_hoy_ingresar_venta',
                   'Ventana_ventas_ingresar_venta',
                   'Ventana_ver_clientes',
                   'Ventana_ver_ingredientes',
                   'Ventana_ver_lista_platos',
                   'Ventana_ver_ingredientes_plato',
                   'Ventana_ver_ventas',
                   'Ventana_ver_usuarios',
                   'Ventana_editar_clientes',
                   'Ventana_editar_ingredientes',
                   'Ventana_editar_platos',
                   'Ventana_editar_ventas',
                   'Ventana_editar_usuarios',
                   'Ventana_reportes_por_fecha',
                   'Ventana_reportes_por_venta',
                   'Ventana_reportes_por_plato',
                   'Ventana_ayuda_videos_tutoriales',
                   'Ventana_ayuda_whatsapp',
                   'Ventana_ayuda_version',
                   }


titulo_ventanas = {'Ventana_login':                             'EICA S.A.C. | Iniciar sesión',
                   'Ventana_ejemplo':                           'EICA S.A.C. | Ventana ejemplo',
                   'Ventana_inicio_gerencia':                   'EICA S.A.C. | Página principal: Gerencia',
                   'Ventana_compras_ingresar_compra':       'EICA S.A.C. | Compras: Ingresar compra hoy',
                   'Ventana_inventario_disponibilidad_platos':  'EICA S.A.C. | Inventario: Disponibilidad de platos',
                   'Ventana_reportes_inventario_disponibilidad': 'EICA S.A.C. | Inventario: Disponibilidad de ingredientes',
                   'Ventana_ventas_hoy_ingresar_venta':         'EICA S.A.C. | Ventas: Ingresar venta hoy',
                   'Ventana_ventas_ingresar_venta':             'EICA S.A.C. | Ventas: Ingresar venta',
                   'Ventana_ver_clientes':                      'EICA S.A.C. | Ver: Clientes',
                   'Ventana_ver_ingredientes':                  'EICA S.A.C. | Ver: Ingredientes',
                   'Ventana_ver_lista_platos':                  'EICA S.A.C. | Ver: Lista platos',
                   'Ventana_ver_ingredientes_plato':            'EICA S.A.C. | Ver: Ingredientes de un plato',
                   'Ventana_ver_ventas':                        'EICA S.A.C. | Ver: Ventas',
                   'Ventana_ver_usuarios':                      'EICA S.A.C. | Ver: Usuarios',
                   'Ventana_editar_clientes':                   'EICA S.A.C. | Editar: Clientes',
                   'Ventana_editar_ingredientes':               'EICA S.A.C. | Editar: Ingredientes',
                   'Ventana_editar_platos':                     'EICA S.A.C. | Editar: Platos', 
                   'Ventana_editar_ventas':                     'EICA S.A.C. | Editar: Ventas', 
                   'Ventana_editar_usuarios':                   'EICA S.A.C. | Editar: Usuarios',   
                   'Ventana_reportes_por_fecha':                'EICA S.A.C. | Reportes: Por fecha',
                   'Ventana_reportes_por_venta':                'EICA S.A.C. | Reportes: Por venta',
                   'Ventana_reportes_por_plato':                'EICA S.A.C. | Reportes: Por plato',
                   'Ventana_ayuda_videos_tutoriales':           'EICA S.A.C. | Ayuda: Videos',
                   'Ventana_ayuda_whatsapp':                    'EICA S.A.C. | Ayuda: Whatsapp',
                   'Ventana_ayuda_version':                     'EICA S.A.C. | Ayuda: Notas de la versión',


                   'Popupmsg':                          'EICA S.A.C. | Aviso',
                   'Gestionar_ingredientes':            'EICA S.A.C. | Gestionar ingredientes',
                   }


mensajes_global = {'MSG_0':       'ERROR',
                   'MSG_1':       'Aquí se muestran las acciones realizadas.',
                   'MSG_2':       'Ingrese usuario & contraseña.',
                   'MSG_3':       'Entrando....',
                   'MSG_4':       'Usuario o contraseña incorrecto.',
                   'MSG_5':       'Inicio de sesión satisfactorio.',
                   'MSG_6':       'Usuario y contraseña son obligatorios.',
                   'MSG_7':       'Nombre y precios son requeridos.',
                   'MSG_8':       'Porfavor selecciona una fila.',
                   'MSG_9':       'Se ha actualizado la lista de platos.',
                   'MSG_10':      'Ingrese una cantidad mayor a cero.',
                   'MSG_11':      'Descargando de la base de datos.',
                   'MSG_12':      'Se ha cargado la base de datos.',
                   'MSG_13':      'Error: Vuelva a seleccionar o actualice.',
                   'MSG_14':      'Se ha exportado a EXCEL exitosamente.',
                   'MSG_15':      'Se ha exportado a PDF exitosamente.',
                   'MSG_16':      'Error: Intenta nuevamente.',
                   'MSG_17':      'No se guardó el archivo',
                   'MSG_18':      'Ventana_Login: Inicio sesión correctamente',
                   'MSG_19':      '',
                   'MSG_20':      '',
                   'MSG_21':      '',
                   'MSG_22':      '',
                   'MSG_23':      '',
                   'TABLA_0':     'Saldo negativo',
                   'TABLA_1':     '',
                   }


class conectar_base_datos:

    def __init__(self):
        try:
            self.db = mysql.connector.connect(**configuracion)
            self.c = self.db.cursor()
        except Exception as e:
            print(conectar_base_datos.__name__+":",e)
    
    def get_contrasenha(self,usuario):
        pass
    
    def get_rows(self,search = ""):
        try:
            query=('SELECT {} FROM platos'.format('*'))
            self.c.execute(query)
            return self.c.fetchall()
        except Exception as e:
            print (self.get_rows.__name__+":",e)


class Ventana_Login(GridLayout):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2
        
        self.add_widget(Label(text="Usuario:"))        
        self.usuario=TextInput(multiline=False)
        self.add_widget(self.usuario)
        
        self.add_widget(Label(text="Contraseña:"))        
        self.contrasenha=TextInput(multiline=False)
        self.add_widget(self.contrasenha)
        
        self.add_widget(Label(text="Contraseña:"))

        self.boton_iniciar_sesion=Button(text="Iniciar sesion")
        self.boton_iniciar_sesion.bind(on_press=self.iniciar_sesion)
        self.add_widget(self.boton_iniciar_sesion)
    
    def cambiar_mensaje(self,mensaje):
        self.mensaje.text=mensaje
    
    def iniciar_sesion(self,instance):
        
        usuario=self.usuario.text
        contrasenha=self.contrasenha.text
        
        
        print(self.iniciar_sesion.__name__,': {},{}'.format(usuario,contrasenha))
        info="ga"
        
        aplicacion.info_page.update_info(info)
        #Cambiamos de página
        aplicacion.screen_manager.current="Info"
        Clock.schedule_once(self.conectar,1)
    
    def conectar(self,_):
        
        usuario=self.usuario.text
        contrasenha=self.contrasenha.text
        print("Conectando")
        aplicacion.screen_manager.current="Ventana_inicio_gerencia"
        
        xd=conectar_base_datos()
        ga=xd.get_rows()
        aplicacion.Ventana_inicio_gerencia.actualizar_texto(str(ga[0]))


class Ventana_inicio_gerencia(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.message=Label(
                           font_size=20)
        #self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
    
    def actualizar_texto(self,mensaje):
        self.message.text=mensaje


class Ventana_cargando(GridLayout):
    
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

        
class ControlVentanas (App):
    
    def build(self):
        
        self.title = 'EICA '+version_eica
        
        self.screen_manager=ScreenManager()
        
               
        self.login=Ventana_Login()        
        screen=Screen(name="Connect")
        screen.add_widget(self.login)
        self.screen_manager.add_widget(screen)

        self.info_page=Ventana_cargando()
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


 
if __name__=="__main__":
    aplicacion=ControlVentanas()
    aplicacion.run()
