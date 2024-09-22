import reflex as rx
from search import ui
from search.state import State


def chat_page() -> rx.Component:
    return ui.base_layout(
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("book-open-text"),
                        rx.text("SOURCES", class_name="font-bold"),
                    ),
                    rx.center(
                        rx.grid(
                            rx.card("https://example.com"),
                            rx.card("https://randomwebsite.org"),
                            rx.card("https://sampleurl.net"),
                            rx.card("https://testdomain.com"),
                            rx.card("https://dummysite.io"),
                            rx.card("https://dummysite.io"),
                            columns="3",
                            gap=10,
                        ),
                    ),
                ),
                class_name="p-4 w-full md:w-3/4 border-2 border-black rounded-lg",
            ),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("square-chevron-right"),
                        rx.text("QUESTION", class_name="font-bold"),
                    ),
                    rx.text(State.query),
                ),
                class_name="p-4 w-full md:w-3/4 border-2 border-black rounded-lg",
            ),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("message-square-quote"),
                        rx.text("ANSWER", class_name="font-bold"),
                    ),
                    rx.markdown(State.answer),
                ),
                class_name="p-4 w-full md:w-3/4 border-2 border-black rounded-lg",
            ),
            class_name="mt-10 flex items-center justify-center",
        ),
    )
