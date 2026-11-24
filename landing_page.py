import flet as balls  # used balls here for fun and brain training, adapt to anything
from landing_style import ballsStyle, COLORS
from buttons import grey_hover, dark_button

def landingPage(page):
    page.title= 'Seeing what I can really do with Flet'
    #page.vertical_alignment = balls.MainAxisAlignment.CENTER
    page.horizontal_alignment = balls.CrossAxisAlignment.CENTER

    ballsStyle(page)

    hero_text = balls.Text(
        'DIGITAL DESIGNER',
        size= 120,
        font_family= 'the_robot',
        color= COLORS['balls_white'],
        width= 700,
        style= balls.TextStyle(
            height= 0.8,
        ),
        text_align= balls.TextAlign.CENTER,
    )

    description = balls.Text(
        'Creating Immersive Experiences',
        size= 16,
        font_family= 'the_art',
        color= COLORS['muted_grey'],
        text_align= balls.TextAlign.CENTER,
    )

    hero_center = balls.Column(
        controls=[
            description,
            hero_text
        ],
        horizontal_alignment= balls.CrossAxisAlignment.CENTER,
        alignment= balls.MainAxisAlignment.CENTER,
        spacing= 20
    )

    def menu_hover(e):
        if e.data == "true":
            e.control.style.shape = balls.RoundedRectangleBorder(radius=24)
            e.control.bgcolor = COLORS['muted_grey']
        else:
            e.control.style.shape = balls.RoundedRectangleBorder(radius=0)
            e.control.bgcolor = None
        page.update()

    logo = balls.TextButton(
        "Arbitrary",
        style=balls.ButtonStyle(
            color=COLORS['muted_grey'],
            shape=balls.RoundedRectangleBorder(radius=0),
            text_style=balls.TextStyle(
                font_family='the_art',
                size=16,
            ),
        ),
        on_hover=menu_hover,
    )
    menu = balls.TextButton(
        "Menu",
        style=balls.ButtonStyle(
            color=COLORS['muted_grey'],
            shape=balls.RoundedRectangleBorder(radius=0),
            text_style=balls.TextStyle(
                font_family='the_art',
                size=16,
            ),
        ),
        on_hover=menu_hover,
    )

    navbar = balls.Row(
        controls=[
            logo, menu
        ],
        alignment= balls.MainAxisAlignment.SPACE_BETWEEN
    )

    left_image = balls.Container(
        border_radius=24,
        expand=True,
        image= balls.DecorationImage(
            src= 'assets/download (5).jpeg',
            fit=balls.ImageFit.COVER,
        )
    )

    right_image = balls.Container(
        border_radius=24,
        expand=True,
        image= balls.DecorationImage(
            src='assets/pexels-media-844813-1695365190656.jpeg',
            fit= balls.ImageFit.COVER
        )
    )

    left_overlay = balls.Container(
        content=balls.Column(
            controls=[
                grey_hover(balls.Text('The Denim Flux', size=20, color=COLORS['balls_white'])),
                balls.Text('It all kind of started from a pinterest board.', size=16, color=COLORS['muted_grey']),
            ],
            horizontal_alignment=balls.CrossAxisAlignment.START,
            alignment=balls.MainAxisAlignment.CENTER,
            spacing=300,
        ), padding= 20, visible=False,
    )

    def left_hover(e):
        if e.data == "true":
            left_overlay.visible = True
        else:
            left_overlay.visible = False
        page.update()

    left_card = balls.Container(
        content= balls.Stack(  # a stack because the on hover effects are kind of like an overlay
            controls=[left_image, left_overlay]
        ),
        on_hover=left_hover,
        height=400,
        border_radius=24,
        expand= True,
    )

    right_overlay = balls.Container(
        content=balls.Column(
            controls=[
                grey_hover(balls.Text('The Quiet Adventure', size=20, color=COLORS['balls_white'])),
                balls.Text('Like a gaze towards mystic lands only you can see', size=16, color=COLORS['muted_grey']),
            ],
            horizontal_alignment=balls.CrossAxisAlignment.START,
            alignment=balls.MainAxisAlignment.CENTER,
            spacing=300,
        ), padding=20, visible=False,
    )

    def right_hover(e):
        if e.data == "true":
            right_overlay.visible = True
        else:
            right_overlay.visible = False
        page.update()

    right_card = balls.Container(
        content= balls.Stack(  # a stack because the on hover effects are kind of like an overlay
            controls=[right_image, right_overlay]
        ),
        on_hover=right_hover,
        on_click= lambda e: page.go('/bicycle'),
        height=400,
        border_radius=24,
        expand=True,
    )

    image_section = balls.Container(
        content=balls.Row(
            controls=[
                left_card,
                right_card,
            ],
            spacing=20,
            expand=True,
        ),
        expand=True,
    )

    layout = balls.View(
        '/',
        controls = [
            navbar, hero_center, image_section,
        ],
        spacing= 100,
        vertical_alignment= balls.MainAxisAlignment.CENTER,
        horizontal_alignment= balls.CrossAxisAlignment.CENTER,
        scroll=balls.ScrollMode.AUTO 
    )

    return layout


