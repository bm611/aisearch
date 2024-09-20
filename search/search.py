"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from . import pages

style = {
    "font_family": "Lexend",
    "font_size": "16px",
}

app = rx.App(
    style=style,
    theme=rx.theme(
        appearance="light",
    ),
    stylesheets=[
        "/fonts/font.css",  # This path is relative to assets/
    ],
)
# pages & routes
app.add_page(pages.home_page, route="/")
app.add_page(pages.chat_page, route="/chat")
