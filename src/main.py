# import flet as ft


# def main(page: ft.Page):
#     page.title = "список друзей"

#     friends = []

#     def friend(add):
#         friends.append(name_input.value)
#         print("Список друзей:", friends)

#     name_input = ft.TextField(
#         label="введите имя")
    
#     button = ft.ElevatedButton(
#         text="Добавить", 
#         on_click=friend)

#     page.add(name_input, button)


# ft.app(main)