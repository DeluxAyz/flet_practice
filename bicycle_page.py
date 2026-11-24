import flet as balls
from buttons import grey_hover, dark_button
from landing_style import  COLORS


def bicyclePage(page):

    # page.bgcolor = COLORS['balls_white'/] this gets overridden so not working

    back_button= balls.TextButton(
        "Return to Landing",
        on_click=lambda e: page.go('/'),
        on_hover= grey_hover,
        style=balls.ButtonStyle(
            color=COLORS['dark_grey'],
            shape=balls.RoundedRectangleBorder(radius=24),
            text_style=balls.TextStyle(
                font_family='the_art',
                size=16,
            ),
        ),
    )

    unknown_button= balls.TextButton(
        "Don't Click...",
        on_click=lambda e: page.go('/'),
        on_hover= grey_hover,
        style=balls.ButtonStyle(
            color=COLORS['dark_grey'],
            shape=balls.RoundedRectangleBorder(radius=24),
            text_style=balls.TextStyle(
                font_family='the_art',
                size=16,
            ),
        ),
    )

    navbro = balls.Row(
        controls = [back_button, unknown_button],
        alignment = balls.MainAxisAlignment.SPACE_BETWEEN
    )

    main_button = dark_button(
        balls.Text('UNDERSTAND', size=14, color=COLORS['balls_white'], font_family='the_art')
    )

    second_button = balls.TextButton(
        "Allured",
        on_hover= grey_hover,
        style=balls.ButtonStyle(
            color=COLORS['dark_grey'],
            shape=balls.RoundedRectangleBorder(radius=24),
            text_style=balls.TextStyle(
                font_family='the_art',
                size=14,
            ),
        ),
    )

    stuffButtons = balls.Row(
        controls = [main_button, second_button],
        spacing= 20,
        alignment= balls.MainAxisAlignment.START,
    )

    mainStuff = balls.Column(
        controls= [
            balls.Text(
                'The Quiet Adventure', 
                style= balls.TextStyle(
                    height= 0.85,
                ),
                size=48, font_family='the_robot', color=COLORS['balls_black']
            ),
            balls.Text(
                'Like a gaze towards mystic lands only you can see',
                style= balls.TextStyle(
                    height= 1,
                ),
                size= 24, font_family= 'the_robot', color=COLORS['balls_black'],
            ),
            stuffButtons,
        ],
        spacing= 15,
        alignment= balls.MainAxisAlignment.START,
    )

    bottomStuff = balls.Column(
        controls = [
            balls.Text('ABOUT', size=14, font_family='the_robot', color=COLORS['balls_black']),
            balls.Text(
                # warning, long text I didn't know how to break ahead...
                'SO THIS DESIGN IS GOTTEN FROM PINTEREST, I USUALLY DESIGN MY OWN WORKS, BUT THIS WAS A SIMPLE FLET LAYOUT PRACTICE. THE DESIGN CAUGHT ME AS SOMETHING THAT CAN BE DONE FAST AND TOUCHES THE BASICS.',
                size=14, font_family='the_robot', color=COLORS['balls_black']
            )
        ],
        spacing= 10,
        alignment= balls.MainAxisAlignment.START,
    )

    stuff= balls.Container(
        content= (
            balls.Column( controls=[mainStuff, bottomStuff], alignment= balls.MainAxisAlignment.SPACE_BETWEEN )
        ),
        expand= 1,
    )

    right_image = balls.Container(
        border_radius=24,
        expand=2,
        image= balls.DecorationImage(
            src='assets/pexels-media-844813-1695365190656.jpeg',
            fit= balls.ImageFit.COVER
        )
    )

    mainLayout = balls.Row(
        controls= [
            stuff, right_image
        ],
        expand= True,
        spacing= 10,
    )

    return balls.View(
        '/bicycle',
        [navbro, mainLayout],
        bgcolor = COLORS['balls_white'],
        padding= 30,
        spacing= 30,
        vertical_alignment=balls.MainAxisAlignment.CENTER,
        horizontal_alignment=balls.CrossAxisAlignment.CENTER
    )

