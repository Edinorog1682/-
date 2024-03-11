import flet as ft
from flet import NavigationDrawer
from core.style import *
from core.dicitionary_ru import *
import time
from views.login import Login


class User_Window(Login):
    def __init__(self, page: Page):
        super().__init__(page)
        self.i = 0
        self.b = False
        self.login_page = None
        self.login_page = self.page.views[0].controls[0].login_username.value
        self.my_type_writter_text = Text(self.login_page, no_wrap=False)
        self.Text = Text(f'Добро пожаловать, {self.login_page}', size=24, color='#f7f7f7',opacity=self.i)

        self.content = Stack([
            Container(
                Column([
                    Row([self.Text], alignment=MainAxisAlignment.CENTER)
                ]),  on_hover =  self.glav_anim, margin=ft.margin.symmetric(vertical=page.height / 2)
            )

        ],visible=True)
        self.menu_but = ft.ElevatedButton("Show drawer", on_click=self.show_drawer)
        page.drawer = ft.NavigationDrawer(visible=True,
                                        controls=[
                                            ft.Container(height=12),
                                            ft.NavigationDrawerDestination(
                                                label="Item 1",
                                                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                                                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
                                            ),
                                            ft.Divider(thickness=2),
                                            ft.NavigationDrawerDestination(
                                                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                                                label="Item 2",
                                                selected_icon=ft.icons.MAIL,
                                            ),
                                            ft.NavigationDrawerDestination(
                                                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                                                label="Item 3",
                                                selected_icon=ft.icons.PHONE,
                                            ),
                                        ],
                                        )
        self.content = ft.Stack([
            page.drawer, self.menu_but
        ])#,visible=False

    def show_drawer(self, e):
        self.menu.visible = True
        self.page.update()
        self.menu.update()
    def glav_anim(self,e):
        self.i = 0
        if not self.b:
            while self.i < 1:
                self.i += 0.001
                self.Text.opacity = self.i
                self.page.update()
                self.b = True
                time.sleep(0.01)
                print(self.i)

