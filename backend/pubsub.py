import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
import uuid
from backend.blockchain.block import Block

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-76359316-4891-4c83-bdb9-9fb5b51fe22e'
pnconfig.publish_key = 'pub-c-5dc91eff-2b7b-48eb-b0be-b824034cabf2'
# Generate a random UUID for the client
pnconfig.uuid = str(uuid.uuid4())

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}

class Listener(SubscribeCallback):

    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], { 'foo': 'bar' })

if __name__ == '__main__':
    main()