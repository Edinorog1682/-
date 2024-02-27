import flet
from flet import *
from core.style import *
from core.dicitionary_ru import *
import sqlite3
import core.BD as DB
from assets import *
from views.login import *


class Register(Container):
    def __init__(self, page: Page):
        super().__init__()

        self.image_active = Image(src='assets/')
        self.image_noactive = Image(src='assets/content_1.jpg',
                                    animate_opacity=300,
                                    opacity=1,

                                    )
        page.theme = Theme(font_family="Open Sans")
        page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
            "Open Sans": "/fonts/OpenSans-Regular.ttf"
        }
        # self.Img_register = Image(
        #     src= 'assets/logo_krug.png',
        #     width=100,
        #     height=100,
        #
        # ),
        self.Text_register = Text(
            value='Регистрация',
            color='#f7f7f7',
            font_family="Open Sans",
            size=36,

        )
        self.E_mail = TextField(

            width=320,
            height=40,
            hint_text="E-mail",
            hint_style=TextStyle(color='#f7f7f7'),
            bgcolor=colors.with_opacity(0.5, '#bababa'),
            # border_color='#f7f7f7',
            # border_width=input_border_size,
            content_padding=10,
            border_radius=15,
            prefix_icon=icons.ADMIN_PANEL_SETTINGS,
            text_size=11,
            color='#f7f7f7',
            focused_border_color='#f7f7f7'
            # border
        )
        self.username = TextField(

            width=320,
            height=40,
            hint_text="Наименование компании",
            hint_style=TextStyle(color='#f7f7f7'),
            bgcolor=colors.with_opacity(0.5, '#bababa'),
            # border_color='#f7f7f7',
            # border_width=input_border_size,
            content_padding=10,
            border_radius=15,
            prefix_icon=icons.ADMIN_PANEL_SETTINGS,
            text_size=11,
            color='#f7f7f7',
            focused_border_color='#f7f7f7'
        )
        self.password = TextField(
            width=320,
            height=40,
            hint_text="Пароль",
            hint_style=TextStyle(color='#f7f7f7'),
            bgcolor=colors.with_opacity(0.5, '#bababa'),
            # border_color='#f7f7f7',
            # border_width=input_border_size,
            content_padding=10,
            border_radius=15,
            prefix_icon=icons.ADMIN_PANEL_SETTINGS,
            password=True,
            can_reveal_password=True,

            text_size=11,
            color='#f7f7f7',
            focused_border_color='#f7f7f7'
        )
        self.register_button = ElevatedButton(
            text="Зарегистрироваться",
            width=250,
            height=40,
            style=ButtonStyle(
                bgcolor=colors.LIGHT_BLUE_ACCENT_700,
                color='#f7f7f7',
                # side=BorderSide(0, '#272627'),
                overlay_color='#4077bb'
            ),

            ###Поменял импорт с core.DB import * На import core.DB as DB
            # on_click=lambda e:  reg_cheker.register_check(self.E_mail.value, self.username.value)
            #######Тут я перекуртил еще вызов login_auth() чтобы задоджить ошибку из BD.py
            on_click=lambda e: self.login_auth() if DB.checker.register_check(self.E_mail.value, self.username.value, self.password.value) == "Успешно зарегистрирован" else self.login_auth()
            #on_click=lambda e: checker.check_user(self.login_username.value, self.login_password.value)
        )
        self.login_or_email_error = SnackBar(Text("Вы указали уже существующее имя или e-mail",color="#fff0000"),bgcolor="#1e1c20")
        self.bgImag = Image(src='assets/photo_2023-10-27_12-57-51.jpg',
                            opacity=1,
                            scale=3,
                            height=page.height,
                            # color=colors.with_opacity(1, '#4077bb')
                            )

        self.content = Stack([self.bgImag,
                              Column([
                                  Container(
                                      Column([
                                          Row([Image(src='assets/logo_krug.png', width=125, height=125)],
                                              alignment=MainAxisAlignment.CENTER),
                                          Container(Row([self.Text_register], alignment=MainAxisAlignment.CENTER),
                                                    margin=margin.only(top=15),
                                                    border=border.only(top=border.BorderSide(4, "white"))),
                                      ], width=225), alignment=alignment.center
                                  ),
                                  Container(
                                      Column([
                                          Row([self.E_mail], alignment=MainAxisAlignment.CENTER),
                                          Row([self.username], alignment=MainAxisAlignment.CENTER),
                                          Row([self.password], alignment=MainAxisAlignment.CENTER),
                                          Row([self.register_button], alignment=MainAxisAlignment.CENTER),
                                      ]), margin=flet.margin.symmetric(vertical=page.height / 10)
                                  ),
                                  Container(
                                      Column([
                                          Row([Text(value='Вы уже зарегистрированы?', color='#f7f7f7',
                                                    font_family="Open Sans", size=14)],
                                              alignment=MainAxisAlignment.CENTER),
                                          Row([TextButton(text="Войти", on_click=lambda e: self.page.go("/"))],
                                              alignment=MainAxisAlignment.CENTER)
                                      ])
                                  )
                              ])

                              ])
    def login_auth(self):
        print("Меня вызвали потому что была попытка регаться")

        #Закомментил потому что срет ошибку о том, что этой хуйни нет на старнице т.е. ты ее еще не добавил
        #self.login_or_email_error.open = True
        #self.login_or_email_error.update()

