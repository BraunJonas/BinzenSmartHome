import logging
from devices.device_communication.event_listener import EventListener

logger = logging.getLogger(__name__)


class EventManager():
    __listeners = []

    @staticmethod
    def subscribe(listener: EventListener, event: str):
        EventManager.__listeners.append([listener, event])
    

    @staticmethod
    def unsubscribe(listener: EventListener, event: str):
        EventManager.__listeners.remove([listener, event])
        

    @staticmethod
    def notify( event: str, additionalInformation: str):
        for l in EventManager.__listeners:
            if l[1] == event:
                l[0].notify(event, additionalInformation)

