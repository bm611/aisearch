import reflex as rx
from search import backend


class State(rx.State):
    query: str = ""
    answer: str = ""
    metadata: list[dict[str, str]] = []
    is_generating: bool = False
    is_fetching_metadata: bool = False

    def set_query(self, query: str):
        self.query = query

    def update_query(self):
        self.query = ""
        self.metadata = []
        return rx.redirect("/")

    def handle_submit(self):
        self.is_fetching_metadata = True
        return rx.redirect("/chat")

    async def fetch_metadata_async(self):
        if self.is_fetching_metadata:
            self.metadata = backend.fetch_metadata(self.query)
            self.is_fetching_metadata = False
            self.is_generating = True
            # return self.generate_answer_async

    async def generate_answer_async(self):
        if self.is_generating:
            self.answer = backend.generate_answer(self.query, self.metadata)
            self.is_generating = False
