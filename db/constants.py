class Constants:
  show_table_query = "DESCRIBE currency;"
  select_all_query = "SELECT * from currency LIMIT 100;"
  select_lastRow_query = "SELECT * from currency ORDER BY id DESC LIMIT 1;"
  select_all_USD_query = "SELECT * from currency where name = 'USD';"
  select_all_EUR_query = "SELECT * from currency where name = 'EUR';"
  select_in_date_range = "SELECT * FROM currency WHERE date >= %s AND date <= %s;"

  insert_query = "INSERT INTO currency (name, sell, buy, date) VALUES(%s, %s, " \
                 "%s, %s);"
  # insert_query = "INSERT INTO currency (name, sell, buy, date) VALUES('{}',
  # {:.2f}, {:.2f}, '{}')"
  create_currency_table_query = """
  CREATE TABLE currency (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100),
      sell DOUBLE,
      buy DOUBLE,
      date DATE
  )
  """
  drop_table_query = "DROP TABLE currency"