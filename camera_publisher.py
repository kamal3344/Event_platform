""""

this file collected each camera feed and send them to it represented queue through exchange
each thread is going to fetch camera details through main processor or using multiprocessing techniques:

"""
import sys
import logging
import redis
import numpy as np
from platform_configurations import callable_functions
logging.basicConfig(filename='D:\\Event_platform\\logs\\configurations.log',filemode='w',level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
def fetch_camera_details():    # collecting the camera data from the redis server if not inserting the data into redis server
    try:
        response=callable_functions.get_val()
        logging.info(" [camera] details fetch successfully")
        return response
    except Exception as e:
        exc_type, exc_message = sys.exc_info()[0], str(e)
        logging.error(f"Error = {exc_type}")


class Camerapick():
    def __init__(self):
        camera_data=fetch_camera_details()
        print(camera_data)






if __name__ == "__main__":
    args=Camerapick()