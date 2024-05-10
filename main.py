"""
A simple calculator
Author: Veras-D
Date: 24-05-09
"""

import flet as ft
from time import sleep


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
    test_text = ft.Text(color='white', size=40, text_align=ft.TextAlign.CENTER)
    kabom = ft.Text(value='KABOOM!!!', size=100, opacity=0)

    # Adicionando os itens da pagina
    page.add(
        # ft.Row(
        #     [less_bnt,
        #      text_box,
        #      plus_bnt],
        #     alignment=ft.MainAxisAlignment.CENTER
        # ),
        ft.Row(
            [ft.Text(value="Esse app irá se autodestruir em: ", size=40)],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        ft.Row(
            [test_text], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [kabom],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    # Atualizando o que está na tela
    for i in range(10, -1, -1):
        test_text.value = i
        page.update()
        if i == 0:
            kabom.opacity = 100
            page.update()
            # ft.
        sleep(1)


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)
