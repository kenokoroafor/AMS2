import logging 
import azure.functions as func


def main(msg: func.ServiceBusMessage): 
    logging.info(f'********** {msg.get_body().decode('utf-8')} ********')
