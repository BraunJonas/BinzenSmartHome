import customtkinter
from devices.multimedia_devices import AudioDevice
from devices.cooling_device import CoolingDevice
from devices.garage_door import GarageDoor
from devices.heating_device import HeatingDevice
from devices.lights import Light, IntensityLight
from rooms.room import Room
from devices.multimedia_devices import AudioDevice, Tv
from devices.window import Window
from devices.door import Door
from devices.device import Device


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("Smart Home Controller")
        self.geometry(f"{1200}x{600}")

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=0)

        # Rooms
        self.roomList = []
        self.roomListNames = []
        self.roomsFrame = customtkinter.CTkScrollableFrame(self, label_text="Rooms")
        self.roomsFrame.grid(
            row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", columnspan=2
        )
        self.roomsFrame.grid_columnconfigure(0, weight=1)
        self.addRoomButton = customtkinter.CTkButton(
            master=self.roomsFrame,
            text="add Room",
            command=self.addRoom,
        )
        self.addRoomButton.grid(row=0, column=0, padx=20, pady=0)

        # Devices
        self.deviceList = []
        self.devicesFrame = customtkinter.CTkScrollableFrame(self, label_text="Devices")
        self.devicesFrame.grid(
            row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", columnspan=2
        )
        self.devicesFrame.grid_columnconfigure(0, weight=1)

        self.optionRoom = customtkinter.CTkOptionMenu(
            master=self.devicesFrame, values=self.roomList
        )
        self.optionRoom.set("select room")
        self.optionRoom.grid(row=0, column=0, padx=10, pady=0)

        self.optionDeviceType = customtkinter.CTkOptionMenu(
            master=self.devicesFrame,
            values=[
                "Audio Device",
                "Cooling Device",
                "Door",
                "Garage Door",
                "Heating Device",
                "Light",
                "dimmable Light",
                "TV",
                "Window",
            ],
        )
        self.optionDeviceType.set("select device type")
        self.optionDeviceType.grid(row=0, column=1, padx=10, pady=0)

        self.addDeviceButton = customtkinter.CTkButton(
            master=self.devicesFrame,
            text="add Device",
            command=self.addDevice,
        )

        self.addDeviceButton.grid(row=0, column=2, padx=10, pady=0)

        # Temperature controls
        self.temperature_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Temperature Control", width=300
        )
        self.temperature_frame.grid(
            row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.temperature_frame.grid_columnconfigure(0, weight=1)
        self.temperature_sliders = []

        # Multimedia
        self.multimedia_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Multimedia", width=200
        )
        self.multimedia_frame.grid(
            row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.multimedia_frame.grid_columnconfigure(0, weight=1)
        self.multimedia_switches = []

        # doors
        self.doors_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Doors and Windows", width=300
        )
        self.doors_frame.grid(
            row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.doors_frame.grid_columnconfigure(0, weight=1)
        self.doors_switches = []

        # lights
        self.lights_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Lights", width=200
        )
        self.lights_frame.grid(
            row=1, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.lights_frame.grid_columnconfigure(0, weight=1)
        self.lights_controls = []

    def Nightmode(self, room: Room):
        devices = room.getDevices()
        for device in devices:
            device.activateNightMode()

    def switch_event(self, device: Device):
        if isinstance(device, Tv):
            if device.isRunning():
                device.setRunning(False)
            else:
                device.setRunning(True)
                device.playVideo()
        elif isinstance(device, AudioDevice):
            if device.isRunning():
                device.setRunning(False)
            else:
                device.setRunning(True)
                device.playAudio()

        elif isinstance(device, Light):
            if device.isRunning():
                device.setRunning(False)
            else:
                device.setRunning(True)
        elif (
            isinstance(device, Door)
            or isinstance(device, GarageDoor)
            or isinstance(device, Window)
        ):
            if device.isOpen():
                device.setOpen(False)
            else:
                device.setOpen(True)

    def slider_event(self, value, device: Device, label):
        if isinstance(device, CoolingDevice) or isinstance(device, HeatingDevice):
            label.configure(text=int(value))
            device.setTemperature(int(value))
        elif isinstance(device, IntensityLight):
            device.setIntensity(int(value))

    def addRoom(self):
        dialog = customtkinter.CTkInputDialog(text="Enter room name", title="add Room")
        newRoom = Room(dialog.get_input())
        roomLabel = customtkinter.CTkLabel(
            master=self.roomsFrame, text=newRoom.getName()
        )
        roomLabel.grid(row=len(self.roomList) + 2, column=0, padx=10, pady=(0, 10))
        nightmodeButton = customtkinter.CTkButton(
            master=self.roomsFrame,
            text="Nightmode",
            command=lambda: self.Nightmode(newRoom),
        )
        nightmodeButton.grid(
            row=len(self.roomList) + 2, column=1, padx=10, pady=(0, 10)
        )
        self.roomList.append(newRoom)
        self.roomListNames.append(newRoom.getName())
        self.optionRoom.configure(values=self.roomListNames)

    def addTemperatureControl(self, device: Device):
        index = len(self.temperature_sliders) + 1

        label = customtkinter.CTkLabel(
            master=self.temperature_frame, text=device.getName()
        )
        label.grid(row=index, column=0, padx=10, pady=(0, 10))

        label = customtkinter.CTkLabel(self.temperature_frame, text=15)
        label.grid(row=index, column=2, padx=10, pady=(0, 20))

        slider = customtkinter.CTkSlider(
            master=self.temperature_frame,
            from_=0,
            to=30,
            command=lambda value: self.slider_event(value, device, label),
        )
        slider.grid(row=index, column=1, padx=10, pady=(0, 20))
        self.temperature_sliders.append(slider)

    def addDoor(self, device: Device):
        switch = customtkinter.CTkSwitch(
            master=self.doors_frame,
            text=device.getName(),
            command=lambda: self.switch_event(device),
            onvalue="on",
            offvalue="off",
        )
        switch.grid(row=len(self.doors_switches) + 1, column=0, padx=10, pady=(0, 20))
        self.doors_switches.append(switch)

        if isinstance(device, Door):
            lockButton = customtkinter.CTkButton(
                master=self.doors_frame,
                text="lock door",
                command=lambda: device.lock(),
                width=50,
            )
            lockButton.grid(
                row=len(self.doors_switches), column=1, padx=10, pady=(0, 20)
            )
            unlockButton = customtkinter.CTkButton(
                master=self.doors_frame,
                text="unlock door",
                command=lambda: device.unlock(),
                width=50,
            )
            unlockButton.grid(
                row=len(self.doors_switches), column=2, padx=10, pady=(0, 20)
            )
        elif isinstance(device, Window):
            closeBlindsButton = customtkinter.CTkButton(
                master=self.doors_frame,
                text="close blinds",
                command=lambda: device.closeBlinds(),
                width=50,
            )
            closeBlindsButton.grid(
                row=len(self.doors_switches), column=1, padx=10, pady=(0, 20)
            )
            openBlindsButton = customtkinter.CTkButton(
                master=self.doors_frame,
                text="open blinds",
                command=lambda: device.openBlinds(),
                width=50,
            )
            openBlindsButton.grid(
                row=len(self.doors_switches), column=2, padx=10, pady=(0, 20)
            )

    def addLights(self, device: Device):
        if isinstance(device, IntensityLight):
            nameLabel = customtkinter.CTkLabel(
                master=self.lights_frame, text=device.getName()
            )
            nameLabel.grid(
                row=len(self.lights_controls) + 1, column=0, padx=10, pady=(0, 20)
            )
            slider = customtkinter.CTkSlider(
                master=self.lights_frame,
                from_=0,
                to=100,
                width=100,
                command=lambda value: self.slider_event(value, device, None),
            )
            slider.grid(
                row=len(self.lights_controls) + 1, column=1, padx=10, pady=(0, 20)
            )
            self.lights_controls.append(slider)
        else:
            switch = customtkinter.CTkSwitch(
                master=self.lights_frame,
                text=device.getName(),
                command=lambda: self.switch_event(device),
                onvalue="on",
                offvalue="off",
            )
        switch.grid(row=len(self.lights_controls) + 1, column=1, padx=10, pady=(0, 20))
        self.lights_controls.append(switch)

    def addMultimedia(self, device: Device):
        switch = customtkinter.CTkSwitch(
            master=self.multimedia_frame,
            text=device.getName(),
            command=lambda: self.switch_event(device),
            onvalue="on",
            offvalue="off",
        )
        switch.grid(
            row=len(self.multimedia_switches) + 1, column=0, padx=10, pady=(0, 20)
        )
        self.multimedia_switches.append(switch)

    def addDevice(self):
        dialog = customtkinter.CTkInputDialog(text="device name:", title="Add device")
        selectedRoom = None
        for room in self.roomList:
            if room.getName() == self.optionRoom.get():
                selectedRoom = room
        deviceName = dialog.get_input()
        selectedDeviceType = self.optionDeviceType.get()

        if selectedDeviceType == "Audio Device":
            audioDevice = AudioDevice(deviceName)
            selectedRoom.addDevice(audioDevice)
            self.addMultimedia(audioDevice)

        elif selectedDeviceType == "Cooling Device":
            coolingDevice = CoolingDevice(deviceName)
            selectedRoom.addDevice(coolingDevice)
            self.addTemperatureControl(coolingDevice)

        elif selectedDeviceType == "Door":
            door = Door(deviceName)
            selectedRoom.addDevice(door)
            self.addDoor(door)

        elif selectedDeviceType == "Garage Door":
            garageDoor = GarageDoor(deviceName)
            selectedRoom.addDevice(GarageDoor(deviceName))
            self.addDoor(garageDoor)

        elif selectedDeviceType == "Heating Device":
            heatingDevice = HeatingDevice(deviceName)
            selectedRoom.addDevice(heatingDevice)
            self.addTemperatureControl(heatingDevice)

        elif selectedDeviceType == "Light":
            light = Light(deviceName)
            selectedRoom.addDevice(light)
            self.addLights(light)

        elif selectedDeviceType == "dimmable Light":
            dimmableLight = IntensityLight(deviceName)
            selectedRoom.addDevice(dimmableLight)
            self.addLights(dimmableLight)

        elif selectedDeviceType == "TV":
            tv = Tv(deviceName)
            selectedRoom.addDevice(tv)
            self.addMultimedia(tv)

        elif selectedDeviceType == "Window":
            window = Window(deviceName)
            selectedRoom.addDevice(window)
            self.addDoor(window)

        deviceRoom = customtkinter.CTkLabel(
            master=self.devicesFrame, text=selectedRoom.getName()
        )
        deviceRoom.grid(row=len(self.deviceList) + 1, column=0, padx=10, pady=(0, 10))

        deviceType = customtkinter.CTkLabel(
            master=self.devicesFrame, text=selectedDeviceType
        )
        deviceType.grid(row=len(self.deviceList) + 1, column=1, padx=10, pady=(0, 10))

        deviceLabel = customtkinter.CTkLabel(master=self.devicesFrame, text=deviceName)
        deviceLabel.grid(row=len(self.deviceList) + 1, column=2, padx=10, pady=(0, 10))
        self.deviceList.append(deviceLabel)

    def startSetup(self):
        # add rooms
        rooms = []
        rooms.append(Room("Küche"))
        rooms.append(Room("Schlafzimmer"))
        rooms.append(Room("Wohnzimmer"))
        for room in rooms:
            roomLabel = customtkinter.CTkLabel(
                master=self.roomsFrame, text=room.getName()
            )
            roomLabel.grid(row=len(self.roomList) + 2, column=0, padx=10, pady=(0, 10))

            nightmodeButton = customtkinter.CTkButton(
                master=self.roomsFrame,
                text="Nightmode",
                command=lambda: self.Nightmode(room),
            )
            nightmodeButton.grid(
                row=len(self.roomList) + 2, column=1, padx=10, pady=(0, 10)
            )
            self.roomList.append(room)
            self.roomListNames.append(room.getName())
        self.optionRoom.configure(values=self.roomListNames)


if __name__ == "__main__":
    app = GUI()
    app.startSetup()
    app.mainloop()
