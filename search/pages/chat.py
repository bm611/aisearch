import reflex as rx
from search import ui
from search.state import State


def source_card(val):
    return rx.card(
        rx.link(
            rx.flex(
                rx.avatar(src=val["img"], size="1"),
                rx.box(
                    rx.text(val["name"], class_name="font-bold"),
                    rx.text(
                        val["url"],
                        class_name="truncate w-full text-sm text-gray-500",
                    ),
                ),
                spacing="2",
                flex_grow=0,
            ),
            href=val["url"],
            is_external=True,
        ),
        as_child=True,
    )


def chat_page() -> rx.Component:
    return ui.base_layout(
        rx.vstack(
            rx.button(
                "HOME",
                on_click=State.update_query,
                size="2",
                variant="surface",
                color_scheme="gray",
            ),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("book-open-text"),
                        rx.text("SOURCES", class_name="font-bold"),
                    ),
                    rx.cond(
                        State.is_fetching_metadata,
                        rx.center(
                            rx.hstack(
                                rx.spinner(size="3"),
                                rx.text("Fetching Sources..."),
                                class_name="flex justify-center items-center",
                            ),
                        ),
                        rx.center(
                            rx.grid(
                                rx.foreach(State.metadata, source_card),
                                columns=rx.breakpoints(
                                    initial="1", sm="2", md="3", lg="4"
                                ),
                                gap=10,
                            ),
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
                    rx.cond(
                        State.is_generating,
                        rx.vstack(
                            rx.hstack(
                                rx.spinner(size="3"),
                                rx.text("Generating answer..."),
                                class_name="flex justify-center items-center",
                            ),
                            rx.markdown(State.answer),
                        ),
                        rx.markdown(State.answer),
                    ),
                ),
                class_name="p-4 w-full md:w-3/4 border-2 border-black rounded-lg",
            ),
            class_name="mt-10 flex items-center justify-center",
        ),
        on_mount=[State.fetch_metadata_async, State.generate_answer],
    )
