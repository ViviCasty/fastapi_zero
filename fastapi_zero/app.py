from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='Api da vivi')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    # return "123"
    return {'message': 'Oi Momoi'}
    # return Message(message="Pei")
    # por padrão o fastapi sempre retorna json


@app.get('/html', response_class=HTMLResponse)
def read_root_html():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo no html </h1>
      </body>
    </html>"""
