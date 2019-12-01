
from database import conectar_base_datos

if __name__ == "__main__":
    db = conectar_base_datos()
    db_c=db.contrasenha()
    print(db_c.get_by_user_contrasenha('elio'))