# publish.py
import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ietfgcja:mO2moIbKdiKWUNlcM8Ck7VlzvcYYDvMg@shark.rmq.cloudamqp.com/ietfgcja')
print(url)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
for i in range(0,20):

  channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello CloudAMQP'+str(i)+'!')

print(" [x] Sent 'Hello World!'")
connection.close()

# consume.py
import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ietfgcja:mO2moIbKdiKWUNlcM8Ck7VlzvcYYDvMg@shark.rmq.cloudamqp.com/ietfgcja')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()
