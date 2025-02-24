from fastapi import FastAPI, HTTPException, status


app = FastAPI()
items = []
items_id = 1


@app.get('/')
def root():
    return {'message': 'Hello World!!!'}
