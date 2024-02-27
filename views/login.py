from flet import *


from core.style import *
from core.dicitionary_ru import *
import sqlite3
import flet
from core.BD import *
from views.Register import *

class Login(Container):
    def __init__(self, page: Page):
        super().__init__()

        self.image_active = Image(src='assets/')
        self.image_noactive = Image(src='assets/',
                                    animate_opacity=300,
                                    opacity=0)

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
                bgcolor= colors.LIGHT_BLUE_ACCENT_700,

                color=button_font_color,
                side=button_border,
                overlay_color=button_overlay
            ),

            on_click=lambda e: checker.check_user(self.login_username.value, self.login_password.value)
        )
        self.Forgot_button = ElevatedButton(
            text=dic_Forgot_button,
            width=160,
            height=30,
            bgcolor=colors.with_opacity(0, '#949494'),
            style = ButtonStyle(
                bgcolor=colors.LIGHT_BLUE_ACCENT_700,

                color=button_font_color,
                side=button_border,
                overlay_color='#ababab'
            )
        )
        self.regisner_button = TextButton(
            text='Зарегистрироваться',
            width=170,
            height=30,
            on_click= lambda e: self.page.go("/Register")
        )




        self.content = Container(
            Stack([
                self.image_active,
                self.image_noactive,

                Container(
                    Stack([
                        Image(
                            src='assets/logo_krug.png',
                            width=100,
                            height=100,

                        ),
                        Container(
                            Text(
                                value=dic_login_name,
                                size=48,
                                color=login_title_color
                            ),
                            border=border.only(top=border.BorderSide(4, "white")),
                            margin=login_title_margin
                        )
                    ]),
                    alignment=alignment.center
                ),
                Container(
                    Container(
                        Column([
                            self.login_username,
                            self.login_password,
                            Row([self.login_button], alignment=button_align),
                            Row([self.Forgot_button], alignment=button_align),
                            Column([
                                Row([flet.Text(value="Ещё нет аккаунта?", size=16, color='#ffffff',
                                               text_align=flet.TextAlign.CENTER)], alignment=MainAxisAlignment.CENTER),
                                Row([self.regisner_button], alignment=button_align)],
                            alignment=MainAxisAlignment.END,
                            spacing = 20)

                        ],
                            spacing=40),
                        padding=20,
                        width=form_width,
                        height=form_height,
                        # bgcolor=form_bgcolor,
                        border_radius=10,


                        # border=form_border,
                        margin=form_margin
                    ),
                    margin=flet.margin.symmetric(vertical=page.height / 10),
                    alignment = alignment.center
                ),


            ]),
        )

