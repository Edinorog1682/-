import flet
from flet import *
from core.style import *
from core.dicitionary_ru import *
import sqlite3
from core.BD import *
from assets import *


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
                side=BorderSide(0, '#272627'),
                overlay_color='#4077bb'
            ),
            # on_click=lambda e:  reg_cheker.register_check(self.E_mail.value, self.username.value)
        )
        self.bgImag = Image(src='assets/content_2.jpg', animate_opacity=300,
                            opacity=1,

                            )

        self.content = Column([
            Stack([
                self.bgImag,
                Container(
                    Column([
                        Container(
                            Row([
                                Image(
                                    src='assets/logo_krug.png',
                                    width=100,
                                    height=100,

                                )], alignment=MainAxisAlignment.CENTER), margin=margin.only(top=20)
                        ),
                        Row([self.Text_register], alignment=MainAxisAlignment.CENTER),
                        Container(
                            Column([
                                Row([self.E_mail], alignment=MainAxisAlignment.CENTER),
                                Row([self.username], alignment=MainAxisAlignment.CENTER),
                                Row([self.password], alignment=MainAxisAlignment.CENTER),

                            ], spacing=10), margin=flet.margin.symmetric(vertical=page.height / 10)),
                        Row([self.register_button], alignment=MainAxisAlignment.CENTER),
                        Column([
                            Row([Text(value='Вы уже зарегистрированы?', color='#f7f7f7', font_family="Open Sans",
                                      size=14, )],
                                alignment=MainAxisAlignment.CENTER),
                            Row([TextButton(text="Войти", on_click=lambda e: self.page.go("/"))],
                                alignment=MainAxisAlignment.CENTER)
                        ], alignment=flet.MainAxisAlignment.END)
                    ])
                )
            ])

        ],
            horizontal_alignment=CrossAxisAlignment.CENTER,

        )