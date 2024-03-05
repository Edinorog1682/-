from flet import *
from core.style import *
from core.dicitionary_ru import *
import time
from views.login import Login


class User_Window(Login):
    def __init__(self, page: Page):
        super().__init__(page)
        self.b=None
        print(self.b)
        self.login = self.page.views[0].controls[0].content.controls[2].controls[1].content.controls[0].controls[0].value
        print(self.page.views[0].controls[0].content)

        self.Text = Text(f'Добро пожаловать, {self.login}')

        self.content = Container(
            Stack([self.Text

                   ])
        )



