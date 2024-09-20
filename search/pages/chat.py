import reflex as rx
from search import ui
from search.state import State


def chat_page() -> rx.Component:
    return ui.base_layout(
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("search"),
                        rx.text("SOURCES", class_name="font-bold"),
                    ),
                    rx.unordered_list(
                        rx.list_item("Item 1"),
                        rx.list_item("Item 2"),
                        rx.list_item("Item 3"),
                        rx.list_item("Item 4"),
                        rx.list_item("Item 5"),
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
                    rx.text(
                        "To add a margin to the box on smaller screens, you can use Tailwind CSS's responsive design classes. These classes allow you to apply different styles based on screen size breakpoints."
                    ),
                ),
                class_name="p-4 w-full md:w-3/4 border-2 border-black rounded-lg",
            ),
            class_name="mt-10 flex items-center justify-center",
        ),
    )
