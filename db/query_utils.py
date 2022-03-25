from constants import Constants
from connector import Connector
from datetime import datetime
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
    connect.close()
  except Exception as e:
    connect.close()
    logging.error(traceback.format_exc())


def execute_select():
  cursor, connect = Connector.get_connection()
  try:
    cursor.execute(constants.select_lastRow_query)
    logging.info("selected")
    result = cursor.fetchone()
    connect.close()
    logging.info(result)
    return result
  except Exception as e:
    connect.close()
    logging.error(traceback.format_exc())


execute_insert('EUR', 34.4, 31.4)
