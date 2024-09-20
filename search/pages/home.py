import reflex as rx
from search import ui


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
                    name="new_item",
                    placeholder="Enter your prompt here...",
                    class_name="p-4 h-12 w-64 md:w-[40rem] md:h-14 rounded-md text-md md:text-lg shadow-2xl ring-2 ring-gray-300",
                ),
                rx.button(
                    rx.icon("arrow-up"),
                    class_name="h-12 md:h-14 rounded-md text-md shadow-2xl",
                ),
                class_name="mt-8",
            ),
            class_name="flex items-center h-[30vh] md:h-[50vh]",
        ),
    )
