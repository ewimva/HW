import flet as ft
from database import Database
from pprint import pprint


def main(page: ft.Page):
    page.title = "Ваши расходы"
    itle = ft.Text("Ваши расходы", size=40, weight=ft.FontWeight.BOLD)
    database = Database("database.sqlite")
    database.create_tables()
    pprint(database.all_())
    page.data = None
    # page.data = database.get_total()

    name_input = ft.TextField(label="Название расхода")
    amount_input = ft.TextField(label="Сумма расхода")
    total_text = ft.Text(f"Общая сумма расходов: {page.data}")

    def build_rows():
        rows = []
        for t in database.all_():
            rows.append(
                ft.Row([
                    ft.Text(t[1], size=20, color=ft.Colors.PINK),
                    ft.Text(str(int(t[2])), size=20),
                    ft.IconButton(icon=ft.Icons.EDIT_OUTLINED, icon_color=ft.Colors.BLUE, icon_size=20,),
                    ft.IconButton(icon=ft.Icons.DELETE_OUTLINED, icon_color=ft.Colors.RED, icon_size=20, on_click=before_delete, data=t[0],),
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
            expense_list_area.controls = build_rows()
            page.update()

    def before_delete(e):
        page.data = e.control.data
        print(e.control.data)
        page.open(delete_modal)
        page.update()

    def handle_close_delete(e):
        delete_modal.open = False
        page.update()

    def delete_expense(e):
        print(page.data)
        database.delete_expense(page.data)
        delete_modal.open = False
        total = database.get_total()
        total_text.value = f"Общая сумма расходов: {total}"
        expense_list_area.controls = build_rows()
        page.update()

    add_button = ft.ElevatedButton("Добавить", on_click=add_expense, color=ft.Colors.PINK, bgcolor=ft.Colors.AMBER)
    form_area = ft.Row([name_input, amount_input, add_button])
    expense_list_area = ft.Column(expand=True, scroll="always", controls=build_rows())

    delete_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Подтвердите удаление"),
        content=ft.Text("Вы действительно хотите удалить расход?"),
        actions=[
            ft.ElevatedButton(
                "Удалить",
                on_click=delete_expense,
                bgcolor=ft.Colors.RED,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                "Отменить",
                on_click=handle_close_delete,
                bgcolor=ft.Colors.GREEN,
                color=ft.Colors.WHITE,
            ),
        ],
    )

    page.add(form_area, total_text, expense_list_area)

ft.app(main)