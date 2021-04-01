import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info(f'Event: {event}')
    logger.info(f'Context: {context}')
    event['key'] = 'value'
    event['time'] = datetime.now().isoformat()
    return event