import os

# Створення папки film_storage (якщо вона не існує)
if not os.path.exists("film_storage"):
    os.mkdir("film_storage")

# Створення директорій від A до Z
for letter in range(ord('A'), ord('Z')+1):
    directory_name = chr(letter)
    path = os.path.join("film_storage", directory_name)
    if not os.path.exists(path):
        os.mkdir(path)



class Film:
    def __init__(self, title, director, year, rating, duration, genre):

        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
        self.duration = duration
        self.genre = genre
        self.storage_address = ""

    def play(self):
        print(f"Now playing {self.title}")

    def stop(self):
        print(f"Stopping {self.title}")

    def get_info(self):
        info = f"{self.title} ({self.year})\n"
        info += f"Directed by: {self.director}\n"
        info += f"Duration: {self.duration} minutes\n"
        info += f"Genre: {self.genre}\n"
        info += f"Rating: {self.rating}\n"
        return info

    def upload_file(self):
        # Створення імені файлу згідно з назвою фільму
        file_name = f"{self.title.replace(' ', '_')}.txt"
        # Визначення літери для дерикторії за першою літерою назви фільму
        dir_letter = self.title[0].upper()
        # Перевірка, чи існує дерикторія для цієї літери, якщо ні - створення
        if not os.path.exists(f"film_storage/{dir_letter}"):
            os.makedirs(f"film_storage/{dir_letter}")
        # Перевірка, чи існує файл з такою ж назвою, якщо ні - створення
        if not os.path.exists(f"film_storage/{dir_letter}/{file_name}"):
            # Створення файлу із збереженням інформації про фільм
            with open(f"film_storage/{dir_letter}/{file_name}", "w") as f:
                f.write(self.get_info())
        # Збереження шляху до файлу
        self.storage_address = f"film_storage/{dir_letter}/{file_name}"

    def get_film_address(self):
        if self.storage_address:
            return os.path.abspath(self.storage_address)
        else:
            return "Файл фільму ще не завантажено"






