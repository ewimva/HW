import flet as ft
from database import Database
from pprint import pprint


def main(page: ft.Page):
    page.title = "Ваши расходы"
    itle = ft.Text("Ваши расходы", size=40, weight=ft.FontWeight.BOLD)
    database = Database("database.sqlite")
    database.create_tables()
    pprint(database.all_())
    page.data = database.get_total()

    name_input = ft.TextField(label="Название расхода")
    amount_input = ft.TextField(label="Сумма расхода")
    total_text = ft.Text(f"Общая сумма расходов: {page.data}")

    def build_rows():
        rows = []
        for t in database.all_():
            rows.append(
                ft.Row([
                    ft.Text(t[1], size=20, color=ft.colors.PINK),
                    ft.Text(str(int(t[2])), size=20),
                    ft.IconButton(icon=ft.icons.EDIT_OUTLINED, icon_color=ft.colors.BLUE),
                    ft.IconButton(icon=ft.icons.DELETE_OUTLINED, icon_color=ft.colors.RED),
                ])
            )
        return rows

    def add_expense(e):
        if name_input.value and amount_input.value.isdigit():
            amount = int(amount_input.value)
            page.data += amount
            total_text.value = f"Общая сумма расходов: {page.data}"
            database.add_expenses(name_input.value, amount)
            name_input.value = ""
            amount_input.value = ""
            todo_list_area.controls = build_rows()
            page.update()

    add_button = ft.ElevatedButton("Добавить", on_click=add_expense, color=ft.colors.PINK, bgcolor=ft.colors.AMBER)
    form_area = ft.Row([name_input, amount_input, add_button])
    todo_list_area = ft.Column(expand=True, scroll="always", controls=build_rows())

    page.add(form_area, total_text, todo_list_area)

ft.app(main)
