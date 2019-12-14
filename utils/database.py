__autor__ = 'zurmad'

# pip install mysql-connector

try:
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling

except Exception as e:

    print('[ DATABASE.PY ] Error:', e)


credenciales = {'user': 'pc1',
                'password': 'pc1',
                'port': '3306',
                'host': '35.223.65.58',
                'database': 'restaurante',
                'raise_on_warnings': True,
                'ssl_ca': 'certs/server-ca.pem',
                'ssl_key': 'certs/client-key.pem',
                'ssl_cert': 'certs/client-cert.pem'
                }

"""
Don't change these libraries or their order
No cambiar el orden ni valores del diccionario.
Si desea agregar uno pongalo al final del diccionario.

"""

database_tables = {0: 'restaurante.clientes',
                   1: 'restaurante.compras',
                   2: 'restaurante.control_flujo_caja',
                   3: 'restaurante.empresas',
                   4: 'restaurante.lista_platos_por_ventas',
                   5: 'restaurante.lista_productos_por_compras',
                   6: 'restaurante.lista_productos_por_platos',
                   7: 'restaurante.lista_productos_por_ventas',
                   8: 'restaurante.personas',
                   9: 'restaurante.platos',
                   10: 'restaurante.productos',
                   11: 'restaurante.proveedores',
                   12: 'restaurante.transacciones',
                   13: 'restaurante.usuarios',
                   14: 'restaurante.ventas_bodega',
                   15: 'restaurante.ventas_restaurante',
                   }

database_tables_content = {'restaurante.clientes': {0: 'id_cliente',
                                                    1: 'personas_id_persona',
                                                    2: 'dni_cliente',
                                                    3: 'comentarios_cliente'
                                                    },
                           'restaurante.compras': {0: 'id_compra',
                                                   1: 'transacciones_id_transaccion',
                                                   2: 'comentarios_compras'
                                                   },
                           'restaurante.control_flujo_caja': {0: 'id_control_caja',
                                                              1: 'usuarios_id_usuario',
                                                              2: 'monto_ajuste_caja',
                                                              3: 'fecha_apertura_caja',
                                                              4: 'fecha_cierre_caja',
                                                              5: 'fecha_modificado_caja'
                                                              },
                           'restaurante.empresas': {0: 'id_empresa',
                                                    1: 'ruc_empresa',
                                                    2: 'correo_empresa',
                                                    3: 'celular_empresa',
                                                    4: 'fecha_creado_empresa',
                                                    5: 'fecha_modificado_empresa'
                                                    },
                           'restaurante.lista_platos_por_ventas': {0: 'ventas_restaurante_id_venta_restaurante',
                                                                   1: 'platos_id_plato',
                                                                   2: 'precio_venta_unitario',
                                                                   3: 'cantidad',
                                                                   4: 'descuento'
                                                                   },
                           'restaurante.lista_productos_por_compras': {0: 'compras_id_compra',
                                                                       1: 'productos_id_producto',
                                                                       2: 'precio_compra_unitario',
                                                                       3: 'cantidad',
                                                                       4: 'descuento'
                                                                       },
                           'restaurante.lista_productos_por_platos': {0: 'platos_id_plato',
                                                                      1: 'productos_id_producto',
                                                                      2: 'cantidad_producto_por_plato',
                                                                      3: 'unidad_producto_por_plato'
                                                                      },
                           'restaurante.lista_productos_por_ventas': {0: 'ventas_bodega_id_venta_bodega',
                                                                      1: 'productos_id_producto',
                                                                      2: 'precio_venta_unitario',
                                                                      3: 'cantidad',
                                                                      4: 'descuento'
                                                                      },
                           'restaurante.personas': {0: 'id_persona',
                                                    1: 'nombre_persona',
                                                    2: 'apellidos_persona',
                                                    3: 'correo_persona',
                                                    4: 'celular_persona',
                                                    5: 'fecha_creado_persona',
                                                    6: 'fecha_modificado_persona'
                                                    },
                           'restaurante.platos': {0: 'id_plato',
                                                  1: 'nombre_plato',
                                                  2: 'precio_venta_plato',
                                                  3: 'precio_compra_plato',
                                                  4: 'imagen_plato_FALTA'
                                                  },
                           'restaurante.productos': {0: 'id_producto',
                                                     1: 'proveedores_id_proveedor',
                                                     2: 'codigo_barras_producto',
                                                     3: 'nombre_producto',
                                                     4: 'descripcion_producto',
                                                     5: 'cantidad_envases_producto',
                                                     6: 'cantidad_por_envase_producto',
                                                     7: 'unidad_producto',
                                                     8: 'precio_producto',
                                                     9: 'imagen_producto_FALTA'
                                                     },
                           'restaurante.proveedores': {0: 'id_proveedor',
                                                       1: 'empresas_id_empresa',
                                                       2: 'nombre_clave_proveedores'
                                                       },
                           'restaurante.transacciones': {0: 'id_transaccion',
                                                         1: 'clientes_id_cliente',
                                                         2: 'tipo_flujo_transaccion',
                                                         3: 'monto_transaccion',
                                                         4: 'fecha_creado_transaccion',
                                                         5: 'fecha_modificado_transaccion'
                                                         },
                           'restaurante.usuarios': {0: 'id_usuario',
                                                    1: 'personas_id_persona',
                                                    2: 'usuario',
                                                    3: 'contraseña',
                                                    4: 'tipo_usuario'
                                                    },
                           'restaurante.ventas_bodega': {0: 'id_venta_bodega',
                                                         1: 'transacciones_id_transaccion',
                                                         2: 'comentarios_venta_bodega'
                                                         },
                           'restaurante.ventas_restaurante': {0: 'id_venta_restaurante',
                                                              1: 'transacciones_id_transaccion',
                                                              2: 'comentarios_venta_restaurante'
                                                              },
                           }

# Simplifiyng table names
dt = database_tables
dtc = database_tables_content


class conectar_base_datos():

    def __init__(self, **kwargs):
        try:
            self.db = mysql.connector.connect(**credenciales)
            self.c = self.db.cursor()
            print('[ DATABASE.PY ][ Conectar_base_datos ]: Conexión establecida ')
        except Exception as e:
            print(conectar_base_datos.__name__+":", e)

    def ejecutar_query(self, q):
        try:
            print('[ DATABASE.PY ][ Conectar_base_datos ]: Ejecutando query')
            self.c.execute(q)
            return self.c.fetchall()
        except Exception as e:
            print(conectar_base_datos.__name__+":", e)
            print("Recordatorio: UPDATE retorna None")

        finally:
            self.db.commit()
            self.db.close()
            print('[ DATABASE.PY ][ Conectar_base_datos ]: Cerrando conexión')

    # ----------------- CONTRASEÑA ----------------- #

    def get_by_user_contrasenha(self, username):

        d = dt[13]

        query = ('SELECT {} FROM {} WHERE({}="{}")'.format(dtc[d][3],
                                                           d,
                                                           dtc[d][2],
                                                           username))

        print(self.get_by_user_contrasenha.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- CLIENTES ----------------- #

    def get_all_clientes(self):

        d = dt[0]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_by_user_contrasenha.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_cliente(self, id):

        d = dt[0]

        query = ('SELECT {} FROM {} WHERE {}="{}"'.format('*',
                                                          d,
                                                          dtc[d][0],
                                                          id))

        print(self.get_by_user_contrasenha.__name__+":", query)

        return self.ejecutar_query(query)

    def update_by_id_cliente(self, id, dni_cliente, comentarios_cliente):

        d = dt[0]

        query = ('UPDATE {} SET {}="{}",{}="{}" WHERE ({}="{}")'.format(d,
                                                                        dtc[d][2],
                                                                        dni_cliente,
                                                                        dtc[d][3],
                                                                        comentarios_cliente,
                                                                        dtc[d][0],
                                                                        id))

        print(self.update_by_id_cliente.__name__+":", query)

        return self.ejecutar_query(query)

    def insert_new_cliente(self, personas_id_persona, dni_cliente, comentarios_cliente):
        pass

    # ----------------- COMPRAS ----------------- #

    def get_all_compras(self):

        d = dt[1]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_compras.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_compras(self, id):

        d = dt[1]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id
                                                            ))

        print(self.get_by_id_compras.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- CONTROL FLUJO DE CAJA ----------------- #

    def get_all_control_flujo_caja(self):

        d = dt[2]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_control_flujo_caja.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_control_flujo_caja(self, id):

        d = dt[2]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id))

        print(self.get_by_id_control_flujo_caja.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- EMPRESAS ----------------- #

    def get_all_empresas(self):

        d = dt[3]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_control_flujo_caja.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_empresas(self, id):

        d = dt[3]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id))

        print(self.get_by_id_empresas.__name__+":", query)

        return self.ejecutar_query(query)

    def update_all_by_id_empresas(self, id, nuevoRuc, nuevoCorreoEmpresa, nuevoCelularEmpresa):

        d = dt[3]

        query = ('UPDATE {} SET {}="{}",{}="{}",{}="{}" WHERE ({}="{}")'.format(d,
                                                                                dtc[d][1],
                                                                                nuevoRuc,
                                                                                dtc[d][2],
                                                                                nuevoCorreoEmpresa,
                                                                                dtc[d][3],
                                                                                nuevoCelularEmpresa,
                                                                                dtc[d][0],
                                                                                id
                                                                                ))

        print(self.update_all_by_id_empresas.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- LISTA PLATOS X VENTAS ----------------- #

    def get_all_platos_x_ventas(self):

        d = dt[4]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_platos_x_ventas.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_platos_x_ventas(self, id):

        d = dt[4]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id
                                                            ))

        print(self.get_by_id_platos_x_ventas.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- LISTA PRODUCTOS X COMPRAS ----------------- #

    def get_all_productos_x_compras(self):

        d = dt[5]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_productos_x_compras.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_productos_x_compras(self, id):

        d = dt[5]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id))

        print(self.get_by_id_productos_x_compras.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- LISTA PRODUCTOS X PLATOS ----------------- #

    def get_all_productos_x_platos(self):

        d = dt[6]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_productos_x_platos.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_productos_x_platos(self, id):

        d = dt[6]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id
                                                            ))

        print(self.get_by_id_productos_x_platos.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- LISTA PRODUCTOS X VENTAS ----------------- #

    def get_all_productos_x_ventas(self):

        d = dt[7]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_productos_x_ventas.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_productos_x_ventas(self, id):

        d = dt[7]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id))

        print(self.get_by_id_productos_x_ventas.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- PERSONAS ----------------- #

    def get_all_personas(self):

        d = dt[8]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_personas.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_persona(self, id):

        d = dt[8]

        query = ('SELECT {} FROM {} WHERE {}="{}"'.format('*',
                                                          d,
                                                          dtc[d][0],
                                                          id))

        print(self.get_by_id_persona.__name__+":", query)

        return self.ejecutar_query(query)

    def update_all_by_id_persona(self, id, nuevoNombre, nuevoApellido, nuevoCorreo, nuevoCelular):

        print("CUIDADITO!!!!!!!!!!!!")
        print("DANGEROUS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        d = dt[8]

        query = ('UPDATE {} SET {}="{}",{}="{}",{}="{}",{}="{}" WHERE ({}="{}")'.format(dt,
                                                                                        dtc[d][1],
                                                                                        nuevoNombre,
                                                                                        dtc[d][2],
                                                                                        nuevoApellido,
                                                                                        dtc[d][3],
                                                                                        nuevoCorreo,
                                                                                        dtc[d][4],
                                                                                        nuevoCelular,
                                                                                        dtc[d][0],
                                                                                        id
                                                                                        ))

        print(self.update_by_id_persona.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- PLATOS ----------------- #

    def get_all_platos(self):

        d = dt[9]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_platos.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_platos(self, id):

        d = dt[9]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id))

        print(self.get_by_id_platos.__name__+":", query)

        return self.ejecutar_query(query)

    def update_all_by_id_platos(self, id, nuevoNombre, nuevoPrecioVentaPlato, nuevoPrecioCompraPlato, nuevoImagen):

        d = dt[9]

        query = ('UPDATE {} SET {}="{}",{}="{}",{}="{}",{}="{}" WHERE ({}="{}")'.format(d,
                                                                                        dtc[d][1],
                                                                                        nuevoNombre,
                                                                                        dtc[d][2],
                                                                                        nuevoPrecioVentaPlato,
                                                                                        dtc[d][3],
                                                                                        nuevoPrecioCompraPlato,
                                                                                        dtc[d][4],
                                                                                        nuevoImagen,
                                                                                        dtc[d][0],
                                                                                        id
                                                                                        ))

        print(self.update_all_by_id_platos.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- PRODUCTOS ----------------- #

    def get_all_productos(self):

        d = dt[10]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_productos.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_productos(self, id):

        d = dt[10]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id))

        print(self.get_by_id_productos.__name__+":", query)

        return self.ejecutar_query(query)

    def update_all_by_id_productos(self, nuevoProveedoresIdProveedor, nuevoCodigoBarrasProducto, nuevoNombreProducto, nuevoDescripcionProducto, nuevoCantidadEnvasesProducto, nuevoCantidadPorEnvaseProducto, nuevoUnidadProducto, nuevoPrecioProducto, nuevoImagenProducto):

        d = dt[10]

        query = ('UPDATE {} SET {}="{}",{}="{}",{}="{}",{}="{}",{}="{}",{}="{}",{}="{}",{}="{}",{}="{}" WHERE ({}="{}")'.format(d,
                                                                                                                                dtc[d][1],
                                                                                                                                nuevoProveedoresIdProveedor,
                                                                                                                                dtc[d][2],
                                                                                                                                nuevoCodigoBarrasProducto,
                                                                                                                                dtc[d][3],
                                                                                                                                nuevoNombreProducto,
                                                                                                                                dtc[d][4],
                                                                                                                                nuevoDescripcionProducto,
                                                                                                                                dtc[d][5],
                                                                                                                                nuevoCantidadEnvasesProducto,
                                                                                                                                dtc[d][6],
                                                                                                                                nuevoCantidadPorEnvaseProducto,
                                                                                                                                dtc[d][7],
                                                                                                                                nuevoUnidadProducto,
                                                                                                                                dtc[d][8],
                                                                                                                                nuevoPrecioProducto,
                                                                                                                                dtc[d][9],
                                                                                                                                nuevoImagenProducto,
                                                                                                                                dtc[d][0],
                                                                                                                                id
                                                                                                                                ))

        print(self.update_all_by_id_productos.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- PROVEEDORES ----------------- #

    def get_all_proveedores(self):

        d = dt[11]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_proveedores.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_proveedores(self, id):

        d = dt[11]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id
                                                            ))

        print(self.get_by_id_proveedores.__name__+":", query)

        return self.ejecutar_query(query)

    def update_all_by_id_proveedores(self, id, nuevoEmpresasIdEmpresa, nuevoNombreClaveProveedores):

        d = dt[11]

        query = ('UPDATE {} SET {}="{}",{}="{}" WHERE ({}="{}")'.format(d,
                                                                        dtc[d][1],
                                                                        nuevoEmpresasIdEmpresa,
                                                                        dtc[d][2],
                                                                        nuevoNombreClaveProveedores,
                                                                        dtc[d][0],
                                                                        id
                                                                        ))

        print(self.update_all_by_id_proveedores.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- TRANSACCIONES ----------------- #

    def get_all_transacciones(self):

        d = dt[12]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_transacciones.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_transacciones(self, id):

        d = dt[12]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id))

        print(self.get_by_id_transacciones.__name__+":", query)

        return self.ejecutar_query(query)

    def update_all_by_id_transacciones(self, id, nuevoClientesIdCliente, nuevoTipoFLujoTransaccion, nuevoMontoTransaccion):

        d = dt[12]

        query = ('UPDATE {} SET {}="{}" WHERE ({}="{}")'.format(d,
                                                                dtc[d][1],
                                                                nuevoClientesIdCliente,
                                                                dtc[d][2],
                                                                nuevoTipoFLujoTransaccion,
                                                                dtc[d][3],
                                                                nuevoMontoTransaccion,
                                                                dtc[d][0],
                                                                id,
                                                                ))

        print(self.update_all_by_id_transacciones.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- USUARIOS ----------------- #

    def get_all_usuarios(self):

        return ("Como esperas que te pase toda la lista de usuario, kbron")

    # ----------------- VENTAS BODEGA ----------------- #

    def get_all_ventas_bodega(self):

        d = dt[14]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_ventas_bodega.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_ventas_bodega(self):

        d = dt[14]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id
                                                            ))

        print(self.get_by_id_ventas_bodega.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- VENTAS RESTAURANTE ----------------- #

    def get_all_ventas_restaurante(self):

        d = dt[15]

        query = ('SELECT {} FROM {}'.format('*',
                                            d))

        print(self.get_all_ventas_restaurante.__name__+":", query)

        return self.ejecutar_query(query)

    def get_by_id_ventas_restaurante(self, id):

        d = dt[15]

        query = ('SELECT {} FROM {} WHERE ({}="{}")'.format('*',
                                                            d,
                                                            dtc[d][0],
                                                            id
                                                            ))

        print(self.get_by_id_ventas_restaurante.__name__+":", query)

        return self.ejecutar_query(query)

    # ----------------- PASTE HERE NEW TABLES ----------------- #


if __name__ == "__main__":

    #####################################################
    #                       GOD                         #
    #           Run your query examples here            #
    #    Follow the structure like in the lines below   #
    #####################################################

    # respuesta = conectar_base_datos().get_all_productos()
    # print(respuesta)

    pass
