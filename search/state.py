import reflex as rx
from search import backend


class State(rx.State):
    query: str = ""
    answer: str = ""
    metadata: list[dict[str, str]] = []
    is_generating: bool = False

    def set_query(self, query: str):
        self.query = query

    def update_query(self):
        self.query = ""
        return rx.redirect("/")

    def handle_submit(self):
        self.is_generating = True
        return rx.redirect("/chat")

    async def generate_answer_async(self):
        if self.is_generating:
            self.answer, self.metadata = backend.generate_answer(self.query)
            self.is_generating = False
