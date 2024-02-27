from flet import *

from views import User_Window
from views.login import Login
from views.User_Window import Dashboard
from core.style import *
from views.Register import *

class Main(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        page.window_width = windows_width #Определяем размеры окна
        page.theme_mode = ThemeMode.DARK #Устанавливаем тему приложения
        page.window_resizable = True #Запрещаем изменять размер окна
        self.helper()

    def helper(self):
        self.page.on_route_change = self.on_route_change 
        self.page.go("/")

    def on_route_change(self, route):
        route_page = {
            "/": Login,
            "/Register": Register,
            "/User_Window": User_Window,
        }[self.page.route](self.page)
        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                        [route_page]
            )
        )


if __name__ == '__main__':
    app(target=Main, assets_dir="assets")