from fastapi import FastAPI
from routing.books import router as books_routing


app = FastAPI()

app.include_router(books_routing)