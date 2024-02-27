from flet import *
from core.style import *
from core.dicitionary_ru import *

class Dashboard(Container):
    def __init__(self, page:Page):
        super().__init__()
        self.content = Container(
            Text(value="Панель управления")
        )