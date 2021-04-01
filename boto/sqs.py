import boto3

def queue_exists(queue_name):
    sqs = boto3.client('sqs')

    res = sqs.list_queues()
    queues = res.get('QueueUrls')

    return queue_name in queues if queues else False

def list_queues():
    sqs = boto3.client('sqs')

    res = sqs.list_queues()
    print(res)

def create_queue(queue_name):
    sqs = boto3.client('sqs')

    if not queue_exists(queue_name):
        res = sqs.create_queue(
            QueueName=queue_name,
            Attributes={
                'DelaySeconds': '5',
                'MessageRetentionPeriod': '86400'
            }
        )

        print(res)


def get_queue(queue_name):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    return queue

def send_messages(queue):

    res = queue.send_message(MessageBody='world')
    print(res) 

def process_messages(queue):

    for message in queue.receive_messages():
        print(message)

if __name__ == "__main__":
    create_queue('SQS_QUEUE_NAME')
    list_queues()

    queue = get_queue('SQS_QUEUE_NAME')
    print('--------- SEND MESSAGES -------')
    send_messages(queue)
    print('--------- PROCESS MESSAGES -------')
    process_messages(queue)