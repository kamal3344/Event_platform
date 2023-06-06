""""
This file has Multiple functions and each function has there own purpose
they are using for publisher , subscriber , for data base and for rule engine as well

"""
import json
import logging
import redis
import sys
from platform_configurations import config
from platform_configurations.setup_data import Redis_server
logging.basicConfig(filename='D:\\Event_platform\\logs\\configurations.log',filemode='w',level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
Redis_server_obj=Redis_server()

def get_val(): # this function is used to call the camera data from the redis data base
    try:
        redis_connection=redis.Redis(host=config.redis_server["redis_host"],port=config.redis_server["redis_port"],db=config.redis_server["database"])
        Redis_server_obj.insert_data() # inserting data
        retrieved_data=redis_connection.get(config.redis_server["key"])  # fetching data from redis data base

        # deseralize the data
        retrieved_json_data=json.loads(retrieved_data)
        logging.info(" Data Fetch successfully from the redis Database :")
        return retrieved_json_data

    except Exception as e:
        exc_type, exc_message = sys.exc_info()[0], str(e)
        logging.error(f"Error in redis data fetching = {exc_type}")

