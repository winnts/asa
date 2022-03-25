from constants import Constants
from connector import Connector
from datetime import datetime, timedelta
import logger
import traceback

logging = logger.LoggerUtils.get_logging()
logger.LoggerUtils.get_base_logger()
# datetime object containing current date and time
current_time = datetime.now()
# constants contains all query
constants = Constants()


def execute_insert(currency_name, sell_rete, buy_rate):
  records = (currency_name, sell_rete, buy_rate, current_time)
  cursor, connect = Connector.get_connection()
  try:
    logging.info("records:: " + str(records))
    cursor.execute(constants.insert_query, records)
    connect.commit()
    logging.info("commited")
  except Exception as e:
    logging.error(traceback.format_exc())
  finally:
    if connect:
      connect.close()
      logging.info("The mysql connection is closed")


def execute(query):
  cursor, connect = Connector.get_connection()
  try:
    cursor.execute(query)
    logging.info("executed")
    result = cursor.fetchall()
    logging.info(result)
    return result
  except Exception as e:
    logging.error(traceback.format_exc())
  finally:
    if connect:
      connect.close()
      logging.info("The mysql connection is closed")


def execute_select_in_range(start, end):
  cursor, connect = Connector.get_connection()
  try:
    cursor.execute(constants.select_in_date_range, (start, end))
    logging.info("range")
    result = cursor.fetchall()
    logging.info(result)
    return result
  except Exception as e:
    logging.error(traceback.format_exc())
  finally:
    if connect:
      connect.close()
      logging.info("The mysql connection is closed")

# public static void main (String [] args) {}

# execute_insert('EUR', 34.4, 31.4)
# execute(constants.select_all_query)
# execute(constants.select_all_EUR_query)
execute(constants.select_all_USD_query)
# execute_select_in_range(current_time - timedelta(weeks=1), current_time)
