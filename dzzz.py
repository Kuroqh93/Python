class SmartSpeaker:
    def __init__(self, name, max_volume=100):
        self.name = name
        self.max_volume = max_volume
        self.connected_device = None

    def connect_to(self, other_speaker):
        self.connected_device = other_speaker

    def play_music(self, volume):
        if self.connected_device:
            connected_volume = self.connected_device.max_volume
            print(f"{self.name}: Гучність колонки {self.connected_device.name} - {connected_volume}")
        else:
            print(f"{self.name}: Гучність - {volume}")


# Створення двох смарт-колонок
speaker1 = SmartSpeaker("Колонка 1", max_volume=80)
speaker2 = SmartSpeaker("Колонка 2", max_volume=90)

# З'єднання двох колонок
speaker1.connect_to(speaker2)

# Відтворення музики на першій колонці та виведення максимальної гучності другої колонки
volume1 = 70
speaker1.play_music(volume1)