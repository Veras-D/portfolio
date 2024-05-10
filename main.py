"""
A simple calculator
(function) def main(page: Page) -> None
"""

import flet as ft


def main(page: ft.Page):
    """Main page

    Args:
        page (ft.Page): Flet object
    """
    def less(e):
        text_box.value = str(int(text_box.value) - 1)
        page.update()


    def plus(e):
        text_box.value = str(int(text_box.value) + 1)
        page.update()
    page.title = 'Calculadora'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    # Criando itens da pagina
    less_bnt = ft.IconButton(ft.icons.REMOVE, on_click=less, on_focus=less)
    plus_bnt = ft.IconButton(ft.icons.ADD, on_click=plus)
    text_box = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER)

    # Adicionando os itens da pagina
    page.add(
        ft.Row(
            [less_bnt,
             text_box,
             plus_bnt],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)
