class Player:
    def __init__(self, name, media_type, quality="HD"):
        self.name = name
        self.media_type = media_type
        self.quality = quality
        self.current_time = 0

    def play(self):
        print(f"{self.media_type} '{self.name}' started playing at {self.current_time} seconds.")

    def pause(self):
        print(f"{self.media_type} '{self.name}' paused at {self.current_time} seconds.")

    def save_last_time(self):
        print(f"Last watched time for {self.media_type} '{self.name}' saved at {self.current_time} seconds.")

    def change_quality(self, quality):
        self.quality = quality
        print(f"{self.media_type} '{self.name}' quality changed to {quality}.")
