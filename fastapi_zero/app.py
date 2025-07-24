from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import (Message, 
                                  UserSchema,
                                  UserPublic, 
                                  UserDB)

app = FastAPI(title='Api da vivi')

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    # return "123"
    return {'message': 'Oi Momoi'}
    # return Message(message="Pei")
    # por padrão o fastapi sempre retorna json


@app.get('/exercicio-html', response_class=HTMLResponse)
def exercicio_aula_02():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo no html </h1>
      </body>
    </html>"""

@app.post('/users/',
          status_code=HTTPStatus.CREATED,
          response_model=UserPublic
          )
def create_user(user: UserSchema):
    user_with_id = UserDB(
        username= user.username,
        email = user.email,
        password= user.password,
        id = len(database)+1
    )
    database.append(user_with_id)
    #user é um objeto
    return user_with_id

