# import flet as ft

# def main(page: ft.Page):
#     page.title = "Ваши расходы"

#     expenses = []
#     expenses_text = ft.Text("")
#     total_text = ft.Text("Общая сумма расходов: 0")
#     name_input = ft.TextField(label="Название расхода")
#     amount_input = ft.TextField(label="Сумма расхода")

#     def expense(add):
#         name = name_input.value
#         amount = amount_input.value
#         expenses.append((name, amount))

#         text = ""
#         total = 0
#         for item in expenses:
#             text += item[0] + ": " + item[1] + "\n"
#             try:
#                 total += int(item[1])
#             except:
#                 pass




#         expenses_text.value = text
#         total_text.value = "Общая сумма расходов: " + str(total)


#         page.update()

#     button = ft.ElevatedButton(text="Добавить", on_click=expense)



#     page.add(
#         ft.Text("Ваши расходы", size=30), name_input, amount_input, button, expenses_text, total_text)





# ft.app(main)
