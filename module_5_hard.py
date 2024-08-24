import time


class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = "None"

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, password, age)

            self.users[nickname] = {'password': password, 'age': age}
            # print(f"Пользователь с именем {nickname} успешно зарегистрирован")
            self.log_in(nickname, password, age)

    def log_in(self, nickname, password, age):
        if nickname in self.users:
            if password == self.users[nickname].get("password"):
                # print(f"Вы успешно залогинились под никнеймом {nickname}")
                self.current_user = nickname

    def log_out(self):
        self.current_user = "None"
        # print("Вы успешно вышли")

    def add(self, *other):
        if len(other) > 0:
            for i in range(len(other)):
                self.videos[other[i].title] = {'duration': other[i].duration,
                                               'time_now': other[i].time_now,
                                               'adult_mode': other[i].adult_mode}

    def get_videos(self, title):
        response = []
        for name in self.videos:
            if title.casefold() in name.casefold():
                response.append(name)
        return response

    def watch_video(self, title):
        # if title in self.videos:
        if self.current_user == "None":
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if title not in self.videos:
            # print("Видео не найдено")
            return

        usr = self.users.get(self.current_user)
        video = self.videos.get(title)
        usr.get("age")

        if video.get('adult_mode') and int(usr.get("age")) < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        # print(f"Приятного просмотра фильма {title}")

        video_start_time = time.time()

        while time.time() - video_start_time <= video.get('duration'):
            duration = int(time.time() - video_start_time)+1
            print(f"{duration} ", end="")
            time.sleep(1)
        else:
            print("Конец видео")


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    #
    # # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    #
    # # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

