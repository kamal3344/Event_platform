""""
this files provides the complete configuration details of RabbitMQ for publisher part
subscriber part , Rule engine and event consumer part of the application
"""

camera_publisher = {

    "rabbitmq_host":"localhost",
    "rabbitmq_port":15672,
    "rabbitmq_exchange":"publisher",
    "rabbitmq_routingkey":'',
    "rabbitmq_queue":''
}

redis_server = {

    "redis_host":"localhost",
    "redis_port":6379,
    "database":0,
    "key":"event"
}
