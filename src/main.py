import flet as ft


def main(page: ft.Page):

    def change_name(e):
        print(name_input.value)

    
    name_input = ft.TextField(
        label="Some text",
        on_click=change_name
    )


    page.add(name_input)



ft.app(main)