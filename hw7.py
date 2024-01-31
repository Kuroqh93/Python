class BluetoothDevice:
    def __init__(self, brand, model, max_volume, bass_boost):
        self.brand = brand
        self.model = model
        self.max_volume = max_volume
        self.bass_boost = bass_boost
        self.connected_device = None

    def connect(self, other_device):
        self.connected_device = other_device

blueD1 = BluetoothDevice("lmb", "plotnacolonka", 1000, "yes")
blueD2 = BluetoothDevice("lmb", "Cih", 300, "no")

blueD1.connect(blueD2)
if blueD1.connected_device:
    print(blueD1.connected_device.max_volume)
else:
    print("No connected device.")
