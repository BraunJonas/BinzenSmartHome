from devices.WaterEventListener import WaterEventListerner


class WaterEventManager():
    listeners = []

    @staticmethod
    def subscribe(listener: WaterEventListerner):
        WaterEventManager.listeners.append(listener)

    @staticmethod
    def unsubscribe(listener: WaterEventListerner):
        WaterEventManager.listeners.remove(listener)

    @staticmethod
    def notify( enoughWater):
        for l in WaterEventManager.listeners:
            l.notify(enoughWater)

