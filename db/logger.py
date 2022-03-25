import logging


class LoggerUtils:

  @staticmethod
  def get_logging():
    return logging

  @staticmethod
  def get_base_logger():
    return logging, logging.basicConfig(filename='example.log',
                                        encoding='utf-8',
                                        format='%(asctime)s %(message)s',
                                        datefmt='%m/%d/%Y %I:%M:%S %p',
                                        level=logging.INFO)
