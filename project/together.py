# В цьому завданні ви будете реалізовувати інтерактивну музичну бібліотеку. Бібліотека має містити
# виконавців (Назва, Учасники, Рік заснування та Альбоми). Альбомів в свою чергу може бути декілька.
# Ваша програма має зчитувати дані з файлу з серіалізованими даними та зберігати їх в цей файл під
# час додавання або зміни інформації про виконавця чи Альбома.
# Програма має також давати змогу, додавати/змінювати/видаляти виконавця та альбоми в ньому.
# Виконавцем може бути як сольний артист так і група, тому учасників у виконавці може бути декілька.
# Вся структура файлів та їх назви за вами.
import json


def music_ultra():
    music_library = []
    with open('music_library.json', 'r') as food:
        music_library = json.load(food)

    def add_name():
        result = []
        answer = input('Enter name performer: ')
        result.append(answer)
        return result

    def add_year():
        while True:
            result = []
            answer = input('Enter year of creation: ').lower()
            if answer.isdigit():
                result.append(answer)
                return result
            else:
                print('Please, use digits')

    def add_participants():
        user_choose = 'y'
        result = []
        while user_choose == 'y':
            answer = input('Enter name participants: ')
            result.append(answer)
            user_choose = input('Do you want to add another participants?: y or n ')
        return result

    def add_albums():
        user_choose = 'y'
        result = []
        while user_choose == 'y':
            answer = input('Enter album name: ').lower()
            result.append(answer)
            user_choose = input('Do you want to add another album?: y or n ')
        return result

    add_mapping = {
        "name": add_name,
        "year of creation": add_year,
        "participants": add_participants,
        "albums": add_albums
    }

    def add_new_performer():
        new_record = {}
        for keys, func in add_mapping.items():
            new_record[keys] = func()
        print('\nYour list added')
        for idx, val in new_record.items():
            print(idx + ':', end=' ')
            print(*val, sep=', ', end='\n')
        music_library.append(new_record)

    def delete_performer():
        if music_library:
            print('We have', len(music_library), 'lists to delete')
            view_list()
            user_choose = input('\nWhich performer do you want to delete? ')
            if user_choose.isdigit():
                user_choose = int(user_choose) - 1
                if user_choose in range(0, len(music_library)):
                    del music_library[user_choose]
                    print(f'We removed the list at number {user_choose + 1}')
                else:
                    print('You entered the wrong number')
            else:
                print('Please, use numbers')
        else:
            print('The list is empty, nothing to delete')

    def change_performer():
        if music_library:
            print('We have', len(music_library), 'performers to change:')
            albums = [album['name'] for album in music_library]
            album = choice_getter(albums)

            fields = music_library[album]
            field = choice_getter(fields)

            field_name = list(music_library[album].keys())[field]
            if field_name == "name":
                music_library[album][field_name] = add_name()
            elif field_name == "year of creation":
                music_library[album][field_name] = add_year()

            if field_name in ("participants", "albums"):
                action_choice = ['delete', 'add new', 'exit']
                choice = choice_getter(action_choice)
                choice_name = action_choice[choice]

                if choice_name == 'delete':
                    list_values = music_library[album][field_name]
                    del_choice = choice_getter(list_values)
                    user_choose = input('\nAre you sure do you want to delete {}?: y or n '.
                                        format(music_library[album][field_name][del_choice]))
                    if user_choose == 'y':
                        del music_library[album][field_name][del_choice]
                        print('Your choice is deleted')
                elif choice_name == 'add new':
                    if field_name == "participants":
                        music_library[album][field_name] += add_participants()
                    else:
                        music_library[album][field_name] += add_albums()

                elif choice_name == 'exit':
                    exit()
        else:
            print('The list is empty, nothing to change')

    def choice_getter(choice_list):
        while True:
            for index, val in enumerate(choice_list, start=1):
                print(f"{index} - {val}")

            choice = input('Make your choice, what do you want to change: ')
            if not choice.isdigit():
                print('Please, use digits\n')
                continue
            choice = int(choice)
            if choice in range(0, len(choice_list)+1):
                return choice - 1
            else:
                print('You entered the wrong number\n')

    def view_list():
        if music_library:
            for index, val in enumerate(music_library, start=1):
                print('\nList № {}:'.format(index))
                for i in val:
                    print(i + ':', end=' ')
                    print(*music_library[index-1][i], sep=', ', end='\n')
        else:
            print('The list is empty')

    def user_exit():
        with open('music_library.json', 'w') as fod:
            json.dump(music_library, fod, indent=4)

    mapping = {
            'a': add_new_performer,
            'd': delete_performer,
            'v': view_list,
            'c': change_performer,
            'e': user_exit
        }

    key = ''
    while key != 'e':
        key = input('\nChoose an action to work with the music library:\n'
                    'a - for adding the new performer\n'
                    'd - for deleting the performer\n'
                    'v - for viewing the list of performers\n'
                    'c - for changing the performer\n'
                    'e - for exit\n'
                    ).lower()

        if key in mapping:
            mapping[key]()
        else:
            print('You are wrong, try again')


music_ultra()
