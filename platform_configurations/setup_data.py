""""
this file used to store each camera details into the redis database


"""

import redis
import logging
from platform_configurations import config
import sys
import json
logging.basicConfig(filename='D:\\Event_platform\\logs\\configurations.log',filemode='w',level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
class Redis_server():
    def __init__(self):
        self.camera_details = {
            "cameras": [
                {
                    "camera_name": "camera1",
                    "camera_ip": "192.168.0.1",
                    "rtsp": "camera1",
                    "usecase": "person_restricted_area",
                    "model": "yolov4",
                    "video_path": ""
                },
                {
                    "camera_name": "camera2",
                    "camera_ip": "192.168.0.1",
                    "rtsp": "camera2",
                    "usecase": "helmate_restricted_area",
                    "model": "yolov5n",
                    "video_path": ""
                },
                {
                    "camera_name": "camera3",
                    "camera_ip": "192.168.0.1",
                    "rtsp": "camera3",
                    "usecase": "danger_zone",
                    "model": "yolov7",
                    "video_path": ""
                },
                {
                    "camera_name": "camera4",
                    "camera_ip": "192.168.0.1",
                    "rtsp": "camera4",
                    "usecase": "jacket",
                    "model": "yolov8n",
                    "video_path": ""
                }
            ]
        }
    def insert_data(self):
        try:
            data=redis.Redis(host=config.redis_server["redis_host"],port=config.redis_server["redis_port"],db=config.redis_server["database"])
            json_data=json.dumps(self.camera_details,indent=4) # seralizing the data to save the database
            data.set(config.redis_server['key'],json_data)
            logging.info(" Data inserted successfully into redis database:")
        except Exception as e:
            exc_type,exc_message=sys.exc_info()[0],str(e)
            logging.error(f"Error in redis data insertion = {exc_type}")





