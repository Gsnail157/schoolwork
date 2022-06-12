from abc import ABC, abstractmethod


class Media(ABC):
    media_list = []

    def __init__(self, name='', rating=0):
        self.__name = name
        self.__rating = rating

    def __str__(self):
        return f'{self.getName()}, {self.getRating()} stars,'

    def getName(self):
        return str(self.__name)

    def getRating(self):
        return int(self.__rating)

    def setRating(self, value):
        self.__rating = value
        return

    @abstractmethod
    def add(self):
        pass


class Movie(Media):
    def __init__(self, name='', rating=0, director='', running_time=0):
        Media.__init__(self, name, rating)
        self.__director = director
        self.__running_time = running_time

    def __str__(self):
        return f'{super().__str__()} Directed by: {self.getDirector()}, Running time: {self.getRunningTime()} minutes.'

    def getDirector(self):
        return str(self.__director)

    def setDirector(self, name):
        self.__director = name
        return

    def getRunningTime(self):
        return int(self.__running_time)

    def setRunningTime(self, time):
        self.__running_time = time
        return

    def play(self):
        for item in Media.media_list:
            if item.getName() == name:
                print(item)
            else:
                print("No such movie in the media library")
        return

    def add(self):
        name = input("Enter movie name: ")
        director = input("Enter director:")
        duration = int(input("Enter movie duration:"))
        rating = int(input("Enter rating:"))
        movie = Movie(name, rating, director, duration)
        Media.media_list.append(movie)
        print("Movie added!")
        return


class Song(Media):
    def __init__(self, name='', rating=0, artist='', album=0):
        Media.__init__(self, name, rating)
        self.__artist = artist
        self.__album = album

    def __str__(self):
        return f'{super().__str__()} Artist: {self.getArtist()}, Album: {self.getAlbum()}.'

    def getArtist(self):
        return str(self.__artist)

    def setArtist(self, name):
        self.__artist = name
        return

    def getAlbum(self):
        return str(self.__album)

    def setAlbum(self, name):
        self.__album = name
        return

    def play(self, name):
        for item in Media.media_list:
            if item.getName() == name:
                print(item)
            elif len(Media.media_list) == 0:
                print("No such song in the media library")
            else:
                print("No such song in the media library")
        return

    def add(self):
        name = input("Enter song name:")
        artist = input("Enter artist:")
        album = input("Enter album:")
        rating = int(input("Enter rating:"))
        song = Song(name, rating, artist, album)
        Media.media_list.append(song)
        print("Song added!")
        return


class Picture(Media):
    def __init__(self, name='', rating=0, dpi=0):
        Media.__init__(self, name, rating)
        #self.__dpi = dpi if dpi > 200 else 200
        self.__dpi = dpi

    def __str__(self):
        return f'{super().__str__()} Resolution: {self.__dpi} dpi.'

    def getResolution(self):
        return int(self.__dpi)

    def setResolution(self, value):
        self.__dpi = int(value)
        return

    def show(self, name):
        for item in Media.media_list:
            if item.getName() == name:
                print(item)
            else:
                print("No such picture in the media library")
        return

    def add(self):
        name = input("Enter picture name:")
        dpi = int(input("Enter dpi:"))
        rating = int(input("Enter rating:"))
        pic = Picture(name, rating, dpi)
        Media.media_list.append(pic)
        print("Picture added!")
