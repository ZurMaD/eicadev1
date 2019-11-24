__autor__ = 'zurmad'

# pip install mysql-connector

try:
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling

except Exception as e:

    print('[ DATABASE.PY ] Error:', e)


datos_database = {'user': 'pc1',
                  'password': 'pc1',
                  'port': '3306',
                  'host': '35.223.65.58',
                  'database': 'restaurante',
                  'raise_on_warnings': True,
                  'ssl_ca': 'certs/server-ca.pem',
                  'ssl_key': 'certs/client-key.pem',
                  'ssl_cert': 'certs/client-cert.pem'
                  }


class conectar_base_datos():

    _usuarios_tablename = 'restaurante.usuarios'
    _usuarios_col0 = 'idUsuarios'
    _usuarios_col1 = 'personas_id_persona'
    _usuarios_col2 = 'usuario'
    _usuarios_col3 = 'contraseña'
    _usuarios_col4 = 'tipo_usuario'

    def __init__(self):
        try:
            self.db = mysql.connector.connect(**datos_database)
            self.c = self.db.cursor()
            print('[ DATABASE.PY ][ Conectar_base_datos ]: Conexión establecida ')
        except Exception as e:
            print(conectar_base_datos.__name__+":", e)

    def get_contrasenha_encriptada(self, usuario):
        try:
            query = ('SELECT {} FROM {} WHERE({}="{}")'.format(self._usuarios_col3,
                                                               self._usuarios_tablename,
                                                               self._usuarios_col2,
                                                               usuario))
            print(self.get_contrasenha_encriptada.__name__+":", query)
            self.c.execute(query)
            return self.c.fetchall()
        except Exception as e:
            print(self.get_contrasenha_encriptada.__name__+":", e)

    def get_rows(self, search=""):
        try:
            query = ('SELECT {} FROM platos'.format('*'))
            print(self.get_rows.__name__+":", query)
            self.c.execute(query)
            return self.c.fetchall()
        except Exception as e:
            print(self.get_rows.__name__+":", e)


if __name__ == "__main__":
    conectar_base_datos()