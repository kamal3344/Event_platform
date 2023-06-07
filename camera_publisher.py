""""

this file collected each camera feed and send them to it represented queue through exchange
each thread is going to fetch camera details through main processor or using multiprocessing techniques:

"""
import sys
import logging
import redis
import numpy as np
from collections import defaultdict
from platform_configurations import callable_functions
import multiprocessing
import threading
# logging.basicConfig(filename='D:\\Event_platform\\logs\\configurations.log',filemode='w',level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
from platform_configurations.loggings import setup_logging
logger=setup_logging("camera_publisher")

def fetch_camera_details():    # collecting the camera data from the redis server if not inserting the data into redis server
    try:
        response=callable_functions.get_val()
        logger.info(" [camera] details fetch successfully")
        return response
    except Exception as e:
        exc_type, exc_message = sys.exc_info()[0], str(e)
        logger.error(f"Error = {exc_type}")


class Camerapick():
    def __init__(self):
        self.camera_data=fetch_camera_details()
        # initalize processor and threads for each processor
        self.num_of_processor = 4  # working with 4 processor
        self.feeds_per_processor = len(self.camera_data) // self.num_of_processor
        self.remaining_feeds = len(self.camera_data) % self.num_of_processor

        # for key, value in self.camera_data.items():
        #     kwargs = {
        #         "camera_name": value["camera_name"],
        #         "camera_ip": value["camera_ip"],
        #         "camera_rtsp": value["rtsp"],
        #         "camera_usecase": value["usecase"],
        #         "camera_model": value["model"],
        #         "camera_videopath": value["video_path"]
        #
        #         }
        for i, (key, value) in enumerate(self.camera_data.items()):
            kwargs = {
                "camera_name": value["camera_name"],
                "camera_ip": value["camera_ip"],
                "camera_rtsp": value["rtsp"],
                "camera_usecase": value["usecase"],
                "camera_model": value["model"],
                "camera_videopath": value["video_path"]
            }

            # Calculate the processor index for the current camera
            feeds = self.feeds_per_processor  # feeds -> number of theads for each processor
            if i < self.remaining_feeds:      # remaining_feeds -> managing remaining camera details for each processor
                feeds += 1

            # Pass the camera details to the corresponding processor
            process_camera_feeds(processor_index, kwargs)

            logger.debug(f"camera details {value['camera_name']} : {value['camera_ip']}")

















if __name__ == "__main__":
    args=Camerapick()