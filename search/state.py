import reflex as rx
from search import backend


class State(rx.State):
    query: str = ""
    answer: str = ""

    def set_query(self, query: str):
        self.query = query

    def handle_submit(self):
        self.answer = backend.generate_answer(self.query)
        return rx.redirect("/chat")
