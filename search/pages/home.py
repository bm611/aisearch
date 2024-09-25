import reflex as rx
from search import ui
from search.state import State


def home_page() -> rx.Component:
    return ui.base_layout(
        rx.vstack(
            rx.spacer(),
            rx.heading(
                "Web Search with AI",
                class_name="text-4xl md:text-6xl",
            ),
            rx.hstack(
                rx.text("Powered by ", class_name="md:text-2xl"),
                rx.image(
                    "/Brave_Logo.png",
                    height="2em",
                    width="1.8em",
                    size=20,
                ),
                rx.text("Brave and ", class_name="md:text-2xl"),
                rx.icon(
                    "sparkles",
                    size=24,
                    color="var(--indigo-10)",
                ),
                rx.text("Gemini ", class_name="md:text-2xl"),
                class_name="flex items-center",
            ),
            rx.hstack(
                rx.input(
                    placeholder="Enter your prompt here...",
                    class_name="p-2 h-12 w-72 md:w-[40rem] md:h-14 rounded-md text-md md:text-lg shadow-2xl border-2 border-black bg-transparent",
                    value=State.query,
                    on_change=State.set_query,
                ),
                rx.button(
                    rx.icon("arrow-up"),
                    class_name="h-12 md:h-14 rounded-md text-md shadow-2xl",
                    on_click=State.handle_submit,
                ),
                class_name="mt-8",
            ),
            class_name="flex items-center h-[50vh]",
        ),
    )
