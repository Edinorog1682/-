from flet import *

import core.BD as DB
from core.style import *
from core.dicitionary_ru import *
import sqlite3
import flet
import views.User_Window
from views.Register import *


class Login(Container):

    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.b = None
        self.login_username = TextField(
            width=input_width,
            height=input_height,
            hint_text=dic_input_login_name,
            hint_style=TextStyle(color=input_text_color),
            bgcolor=input_bgcolor,
            border_color=input_border_color,
            border_width=input_border_size,
            border_radius=input_border_radius,
            prefix_icon=icons.ADMIN_PANEL_SETTINGS,
            text_size=11,
            content_padding=padding.only(top=25),
            color=input_text_color,
            focused_border_color=focus_input_bgcolor
        )
        self.login_password = TextField(
            width=input_width,
            height=input_height,
            hint_text=dic_input_login_password,
            hint_style=TextStyle(color=input_text_color),
            bgcolor=input_bgcolor,
            border_color=input_border_color,
            border_width=input_border_size,
            border_radius=input_border_radius,
            prefix_icon=icons.LOCK,
            text_size=11,
            color=input_text_color,
            password=True,
            can_reveal_password=True,
            content_padding=padding.only(top=25),
            focused_border_color=focus_input_bgcolor
        )

        self.login_button = ElevatedButton(
            text=dic_login_button,
            width=button_width,
            height=button_height,
            style=ButtonStyle(
                bgcolor=colors.LIGHT_BLUE_ACCENT_700,

                color=button_font_color,
                # side=button_border,
                overlay_color=button_overlay
            ),

            on_click=lambda e: self.prov_log()
            # self.page.go('/User_Window') if DB.checker.check_user(self.login_username.value, self.login_password.value) == "Успешный вход" else self.login_auth_log()
        )
        self.Forgot_button = ElevatedButton(
            text=dic_Forgot_button,
            width=160,
            height=30,
            bgcolor=colors.with_opacity(0, '#949494'),
            style=ButtonStyle(
                bgcolor=colors.LIGHT_BLUE_ACCENT_700,

                color=button_font_color,
                side=button_border,
                overlay_color='#ababab'
            )
        )
        self.text_login = Text(
            value=dic_login_name,
            size=48,
            color=login_title_color
        )
        self.regisner_button = TextButton(
            text='Зарегистрироваться',
            width=170,
            height=30,
            on_click=lambda e: self.page.go("/Register")
        )
        self.login_or_password_error = SnackBar(Text("Вы неправильно лоин или пароль", color="#f7f7f7"),
                                                bgcolor=colors.with_opacity(0, '#bababa'))
        self.bgImag_log = Image(src='assets/photo_2023-10-27_12-57-51.jpg',
                                opacity=1,
                                scale=3,
                                height=page.height,
                                # color=colors.with_opacity(1, '#4077bb')
                                )

        self.content = Stack([self.bgImag_log, self.login_or_password_error,
                              Column([
                                  Container(
                                      Column([
                                          Row([Image(src='assets/logo_krug.png', width=125, height=125)],
                                              alignment=MainAxisAlignment.CENTER),
                                          Container(Row([self.text_login], alignment=MainAxisAlignment.CENTER),
                                                    margin=margin.only(top=15),
                                                    border=border.only(top=border.BorderSide(4, "white"))),
                                      ], width=225), alignment=alignment.center
                                  ),
                                  Container(
                                      Column([
                                          Row([self.login_username], alignment=MainAxisAlignment.CENTER),
                                          Row([self.login_password], alignment=MainAxisAlignment.CENTER),
                                          Row([self.login_button], alignment=MainAxisAlignment.CENTER),

                                      ]), margin=flet.margin.symmetric(vertical=page.height / 10)
                                  ),
                                  Container(
                                      Column([
                                          Row([Text(value='Ещё нет аккаунта?', color='#f7f7f7',
                                                    font_family="Open Sans", size=16)],
                                              alignment=MainAxisAlignment.CENTER),
                                          Row([self.regisner_button], alignment=MainAxisAlignment.CENTER)
                                      ])
                                  )
                              ])
                              ])

    def login_auth_log(self):
        print("Меня вызвали потому что была попытка Выхода")
        self.login_or_password_error.open = True
        self.login_or_password_error.update()

    #  if  == "Успешный вход" else
    def prov_log(self):
        views.User_Window.b=self.login_username.value
        a = DB.checker.check_user(self.login_username.value, self.login_password.value)
        print(self.page.views[0].controls)
        if a == self.login_username.value:
            self.b = self.login_username.value
            self.page.go('/User_Window')
        else:
            self.login_auth_log()
