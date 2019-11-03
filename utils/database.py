__autor__='zurmad'

# pip install mysql-connector 

try:
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling
    
except Exception as e:
    
    print('Error:',e)
    


configuracion = {'user': 'pc1',
                 'password': 'pc1',
                 'host': '104.198.229.44',
                 'database': 'rest',
                 'raise_on_warnings': True}



class conectar_base_datos:

    _usuarios_tablename='rest.usuarios'
    _usuarios_col0='idUsuarios'
    _usuarios_col1='LoginName'
    _usuarios_col2='PasswordHash'
    _usuarios_col3='FirstName'
    _usuarios_col4='LastName'

    def __init__(self):
        try:
            self.db = mysql.connector.connect(**configuracion)
            self.c = self.db.cursor()
        except Exception as e:
            print(conectar_base_datos.__name__+":",e)
    
    def get_contrasenha_encriptada(self,usuario):
        try:
            query=('SELECT {} FROM {} WHERE({}="{}")'.format(self._usuarios_col2,
                                                             self._usuarios_tablename,
                                                             self._usuarios_col1,
                                                             usuario))
            print (self.get_contrasenha_encriptada.__name__+":",query)
            self.c.execute(query)
            return self.c.fetchall()
        except Exception as e:
            print (self.get_rows.__name__+":",e)
    
    def get_rows(self,search = ""):
        try:
            query=('SELECT {} FROM platos'.format('*'))
            print (self.get_rows.__name__+":",query)
            self.c.execute(query)
            return self.c.fetchall()
        except Exception as e:
            print (self.get_rows.__name__+":",e)

if __name__ == "__main__":
    pass