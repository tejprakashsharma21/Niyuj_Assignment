"""
@author : Tej Prakash Sharma
Class for Logger
"""
import logging


class LoggerHeper:
    @staticmethod
    def log_helper(f_path):
        logging.basicConfig(filename=f_path,
                            format="%(asctime)s:%(created)f:%(levelname)s:%(message)s",
                            level=logging.INFO)
        return logging





