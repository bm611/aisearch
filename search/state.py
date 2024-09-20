import reflex as rx


class State(rx.State):
    query: str = ""

    def set_query(self, query: str):
        self.query = query

    def handle_submit(self):
        return rx.redirect("/chat")
