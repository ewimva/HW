import flet as ft


def main(page: ft.Page):
    # установка заголовка
    page.title = "Привет мир"

    friends = ['Elmira', 'Nasiba', 'Nika', 'Nursultan', 'Nurlis', 'Emir']

    def name(check):
        if name_input.value in friends:
            print('Drug naiden', name_input.value)
        else:
            print('Drug ne naiden', name_input.value)

    # функция, которая будет вызываться при изменении значения текстового поля
    #def change_name(e):
    #    print(name_input.value)

    # создание текстового поля
    name_input = ft.TextField(
        label="введите имя",  # текст подсказки
        on_change=name,  # функция, которая будет вызываться при изменении значения
    )

    # добавление текстового поля на страницу(окно)
    page.add(name_input)


ft.app(main)