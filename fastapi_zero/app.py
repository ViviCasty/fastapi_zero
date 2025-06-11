from fastapi import FastAPI

app = FastAPI(title="api da vivi")


@app.get('/')
def read_root():
    return {'message': 'Oi Momoi'}
