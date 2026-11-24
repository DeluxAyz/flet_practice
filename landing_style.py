import flet as balls
import os

def ballsStyle (page):
    """
    All Styles are set up here.
    """

    fonts_dir = os.path.join(os.path.dirname(__file__), "fonts_delux")
    page.fonts = {
        "the_robot": os.path.join(fonts_dir, "Roboto-Medium.ttf"),
        "the_art": os.path.join(fonts_dir, "Satoshi-Variable.ttf"),
    }

    page.padding = balls.padding.all(18)
    page.scroll = 'adaptive'
    page.bgcolor = COLORS['balls_black']

    
COLORS = {
    'balls_black': "#000000",
    'balls_white': '#d5e4e6',
    'muted_grey': "#c6cecf",
    'dark_grey': "#2e3035",
}