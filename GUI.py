import tkinter
import tkinter.messagebox
import customtkinter
from CoolingDevice import CoolingDevice
from Light import Light
from Room import Room
from IntensityLight import IntensityLight
from Tv import Tv
from Window import Window
from Door import Door

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("Smart Home Controller")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=0)

        # Rooms
        self.roomList = []
        self.roomsFrame = customtkinter.CTkScrollableFrame(self, label_text="Rooms")
        self.roomsFrame.grid(
            row=0,
            column=0,
            padx=(20, 0),
            pady=(20, 0),
            sticky="nsew",
            columnspan=2,
        )
        self.roomsFrame.grid_columnconfigure(0, weight=1)
        self.addRoomButton = customtkinter.CTkButton(
            master=self.roomsFrame,
            text="add Room",
            command=self.addRoom,
        )
        self.addRoomButton.grid(row=0, column=0, padx=20, pady=0)
        self.roomLabels = []

        # Devices
        self.devicesFrame = customtkinter.CTkScrollableFrame(self, label_text="Devices")
        self.devicesFrame.grid(
            row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", columnspan=2
        )
        self.devicesFrame.grid_columnconfigure(0, weight=1)

        self.optionRoom = customtkinter.CTkOptionMenu(
            master=self.devicesFrame, values=self.roomList
        )
        self.optionRoom.set("select room")
        self.optionRoom.grid(row=0, column=0, padx=20, pady=0)

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
                "Tv",
                "Window",
            ],
        )

        self.addDeviceButton = customtkinter.CTkButton(
            master=self.devicesFrame,
            text="add Device",
            command=self.addDevice,
        )

        self.addDeviceButton.grid(row=0, column=1, padx=20, pady=0)
        self.deviceLabels = []

        # Heating controls
        self.heating_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Heating"
        )
        self.heating_frame.grid(
            row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.heating_frame.grid_columnconfigure(0, weight=1)
        self.heating_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(
                master=self.heating_frame, text=f"Heizung {i}"
            )
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.heating_switches.append(switch)

        # Multimedia
        self.multimedia_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Multimedia"
        )
        self.multimedia_frame.grid(
            row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.multimedia_frame.grid_columnconfigure(0, weight=1)
        self.multimedia_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(
                master=self.multimedia_frame, text=f"Door {i}"
            )
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.multimedia_switches.append(switch)

        # doors
        self.doors_frame = customtkinter.CTkScrollableFrame(self, label_text="Doors")
        self.doors_frame.grid(
            row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.doors_frame.grid_columnconfigure(0, weight=1)
        self.doors_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.doors_frame, text=f"Door {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.doors_switches.append(switch)

        # lights
        self.lights_frame = customtkinter.CTkScrollableFrame(self, label_text="Lights")
        self.lights_frame.grid(
            row=1, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.lights_frame.grid_columnconfigure(0, weight=1)
        self.lights_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(
                master=self.lights_frame, text=f"Lampe {i}"
            )
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.lights_switches.append(switch)

    def addRoom(self):
        dialog = customtkinter.CTkInputDialog(text="Enter room name", title="add Room")
        newRoom = Room(dialog.get_input())
        roomLabel = customtkinter.CTkLabel(
            master=self.roomsFrame, text=newRoom.getName()
        )
        roomLabel.grid(row=len(self.roomLabels) + 1, column=0, padx=10, pady=(0, 10))
        self.roomLabels.append(roomLabel)
        self.roomList.append(newRoom)
        self.optionRoom.configure(values=self.roomList)

    def addDevice(self):
        dialog = customtkinter.CTkInputDialog(text="device name:", title="Add device")
        selectedRoom = self.optionRoom.get()
        index = self.roomList.index(selectedRoom)
        self.roomList[index].addDevice()
        deviceLabel = customtkinter.CTkLabel(
            master=self.devicesFrame, text=dialog.get_input()
        )
        deviceLabel.grid(
            row=len(self.deviceLabels) + 1, column=0, padx=10, pady=(0, 10)
        )
        self.deviceLabels.append(deviceLabel)

    def startSetup(self):
        rooms = []
        rooms.append(Room("Küche"))
        rooms.append(Room("Schlafzimmer"))
        rooms.append(Room("Wohnzimmer"))
        for room in rooms:
            roomLabel = customtkinter.CTkLabel(
                master=self.roomsFrame, text=room.getName()
            )
            roomLabel.grid(
                row=len(self.roomLabels) + 1, column=0, padx=10, pady=(0, 10)
            )
            self.roomLabels.append(roomLabel)
            self.roomList.append(room.getName())
        self.optionRoom.configure(values=self.roomList)


if __name__ == "__main__":
    app = GUI()
    app.startSetup()
    app.mainloop()
