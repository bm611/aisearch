import reflex as rx


def base_layout(*args, **kwargs) -> rx.Component:
    return rx.container(
        # rx.color_mode.button(position="top-right"),
        rx.fragment(
            *args,
            **kwargs,
        ),
        size="4",
    )
