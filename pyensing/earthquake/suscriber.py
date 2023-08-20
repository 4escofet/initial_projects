import json
import asyncio
import logging
from config import client_id, client_secret

from pyensign import nack
from pyensign.ensign import Ensign

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class EarthquakeSubscriber:
    """
    EarthquakeSubscriber subscribes to an Ensign stream that the EarthquakePublisher is
    writing new earthquake reports to at some regular interval.
    """
    async def handle_event(self, event):
        try:
            data = json.loads(event.data)
        except json.JSONDecodeError:
            logging.error("Received invalid JSON in event payload:", event.data)
            await event.nack(nack.UnknownType)
            return

        logging.info("New earthquake report received: %s", data)
        await event.ack()

    async def subscribe(self):
        id = await self.ensign.topic_id(self.topic)
        async for event in self.ensign.subscribe(id):
            try:
                await self.handle_event(event)
            except Exception as e:
                logging.error("An error occurred while processing event: %s", e)

    def __init__(self, topic="earthquakes-json"):
        """
        Initialize the EarthquakeSubscriber, which will allow a data consumer to
        subscribe to the topic that the publisher is writing earthquake reports to

        Parameters
        ----------
        topic : string, default: "earthquakes-json"
            The name of the topic you wish to subscribe to.
        """
        self.topic = topic
        #self.ensign = Ensign()
        self.ensign = Ensign(client_id=client_id, client_secret=client_secret)

    def run(self):
        """
        Run the subscriber forever.
        """
        asyncio.run(self.subscribe())

    async def handle_event(self, event):
        """
        Decode and ack the event.
        """
        try:
            data = json.loads(event.data)
        except json.JSONDecodeError:
            print("Received invalid JSON in event payload:", event.data)
            await event.nack(nack.UnknownType)
            return

        print("New earthquake report received:", data)
        await event.ack()

    async def subscribe(self):
        """
        Subscribe to the earthquake topic and parse the events.
        """
        id = await self.ensign.topic_id(self.topic)
        async for event in self.ensign.subscribe(id):
            await self.handle_event(event)


if __name__ == "__main__":
    subscriber = EarthquakeSubscriber()
    logging.info("EarthquakePublisher is running. Waiting for updates...")
    subscriber.run()