from mysql.connector import connect


class Connector:

  @staticmethod
  def get_connection():
    conn = connect(
      host="localhost",
      user="root",
      password="1111",
      database="asa",)
    cursor = conn.cursor()
    print(conn)
    return cursor, conn
