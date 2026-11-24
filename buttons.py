import flet as balls
from landing_style import ballsStyle, COLORS  

def grey_hover(menu_text):

    button = balls.Container(
        content = menu_text,
        bgcolor= balls.Colors.with_opacity(0.7, COLORS['dark_grey']),
        width= 200,
        border_radius= 24,
        alignment= balls.alignment.center,
    )

    return button

def dark_button(button_text):

    button = balls.Container(
        content= button_text,
        bgcolor= COLORS['balls_black'],
        border_radius= 24,
        padding= 12,
    )

    return button
