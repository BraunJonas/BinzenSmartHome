from devices.event_listener import EventListerner


class EventManager():
    __listeners = []

    @staticmethod
    def subscribe(listener: EventListerner, event: str):
        EventManager.__listeners.append([listener, event])
        for l in EventManager.__listeners:
            print(l[1])

    @staticmethod
    def unsubscribe(listener: EventListerner, event: str):
        EventManager.__listeners.remove([listener, event])
        for l in EventManager.__listeners:
            print(l[1])

    @staticmethod
    def notify( event: str, additionalInformation: str):
        for l in EventManager.__listeners:
            if l[1] == event:
                l[0].notify(event, additionalInformation)

