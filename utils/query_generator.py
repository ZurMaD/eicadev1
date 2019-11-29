__autor__ = 'zurmad'

# pip install mysql-connector

try:
    import mysql.connector
    from mysql.connector import (connection)
    from mysql.connector import errorcode
    from mysql.connector import pooling

except Exception as e:

    print('[ DATABASE.PY ] Error:', e)




if __name__ == "__main__":
    pass