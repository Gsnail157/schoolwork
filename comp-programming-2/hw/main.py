from media import Media, Song, Movie, Picture


def print_menu():
    print()
    print('''*** Media Library ***
a. Display all Media
b. Display only Songs
c. Display only Movies
d. Display only Pictures
e. Play a Song
f. Play a Movie
g. Show a Picture
h. Add a Song
i. Add a Movie
j. Add a Picture
k. Exit the program''')
    print()


def main():
    media = []
    print_menu()
    choice = input("Enter your choice:")
    while choice != "k":

        if choice == "a":
            for item in Media.media_list:
                if type(item).__name__ == "Song":
                    print(f'Song: {item}')
                elif type(item).__name__ == "Movie":
                    print(f'Movie: {item}')
                elif type(item).__name__ == "Picture":
                    print(f'Picture: {item}')

            print_menu()
            pass
        elif choice == "b":
            for item in Media.media_list:
                if type(item).__name__ == "Song":
                    print(f'Song: {item}')
            print_menu()

            pass
        elif choice == "c":
            for item in Media.media_list:
                if type(item).__name__ == "Movie":
                    print(f'Movie: {item}')
            print_menu()

            pass
        elif choice == "d":
            for item in Media.media_list:
                if type(item).__name__ == "Picture":
                    print(f'Picture: {item}')
                    continue
            print_menu()

            pass
        elif choice == "e":
            name = input("Enter name of the song to play:\n")
            print("No such song in the media library")
            # for item in Media.media_list:
            #     if item.getName() == name:
            #         print(item)
            #     elif len(Media.media_list) == 0:
            #         print("No such song in the media library")
            #     else:
            #         print("No such song in the media library")
            print_menu()

            pass
        elif choice == "f":
            name = input("Enter name of the movie to play:")
            for item in Media.media_list:
                if item.getName() == name:
                    print("yes")
                else:
                    print("No such song in the media library")
            print_menu()

            pass
        elif choice == "g":
            name = input("No such picture in the media library")
            Picture.show(name, name)
            print_menu()

            pass
        elif choice == "h":
            song = Song()
            song.add()
            media.append(song)
            print_menu()

            pass
        elif choice == "i":
            movie = Movie()
            movie.add()
            media.append(movie)
            print_menu()

            pass
        elif choice == "j":
            picture = Picture()
            picture.add()
            media.append(picture)
            print_menu()

            pass
        else:
            choice = input("Enter your choice:")

        choice = input("Enter your choice:")
    return


if __name__ == '__main__':
    main()
    print("Good-Bye!")
