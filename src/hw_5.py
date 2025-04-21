import flet as ft

def main(page: ft.Page):
    page.title = "Ваши расходы"
    title = ft.Text("Ваши расходы", size=40, weight=ft.FontWeight.BOLD)

    name_input = ft.TextField(label="Название расхода")
    amount_input = ft.TextField(label="Сумма расхода")
    total = 0
    total_text = ft.Text(f"Общая сумма расходов: {total}")

    def expense(add):
        nonlocal total
        amount = int(amount_input.value)
        total += amount
        total_text.value = f"Общая сумма расходов: {total}"

        expenses_column.controls.append(
            ft.Row(
            controls=[
                ft.Text(name_input.value, size=20),
                ft.Text(str(amount), size=20, color=ft.colors.BLUE),
                ft.IconButton(icon=ft.icons.EDIT, icon_color=ft.colors.BLUE),
                ft.IconButton(icon=ft.icons.DELETE, icon_color=ft.colors.RED),
            ]
            )
        )
        name_input.value = ""
        amount_input.value = ""
        name_input.focus()
        page.update()

    add_button = ft.ElevatedButton(text="Добавить", on_click=expense)
    form = ft.Row(controls=[name_input, amount_input, add_button])
    expenses_column = ft.Column(scroll="always", expand=True)

    page.add(title, form, total_text, expenses_column)




ft.app(main)
