# This Entire project was purely for practice, from last year, back in my Flet Days

import flet as balls
from landing_page import landingPage
from landing_style import ballsStyle
from denim_page import denimPage
from bicycle_page import bicyclePage


def main(page: balls.Page):
    page.title= 'Seeing what I can really do with Flet'
    #page.vertical_alignment = balls.MainAxisAlignment.CENTER
    page.scroll = 'adaptive'
    page.horizontal_alignment = balls.CrossAxisAlignment.CENTER

    ballsStyle(page)

    home = landingPage(page)
    denim = denimPage(page)
    bicycle = bicyclePage(page)


    def theNavWays(e):
        page.views.clear()

        if page.route == '/':
            page.views.append(home)
        elif page.route == '/denim':
            page.views.append(denim)
        elif page.route == '/bicycle':
            page.views.append(bicycle)

        page.update()
        # end of theNavWays

    page.on_route_change = theNavWays  # connecting my function to route changing

    page.go('/')  # triggering route change initially

balls.app(target=main)
