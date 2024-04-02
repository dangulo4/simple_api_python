#  import FASTAPI from fastapi module to simplify the creation of API's
from fastapi import FastAPI
#  create an instance
app = FastAPI()
# specify the endpoint for HTTP GET request
# @app.get('/get-message')
# async def read_root():
#   return {'Message': 'Congrats! This is your first API'}

@app.get('/get-message')
def hello(name: str):
  return {'Message':"Congrats " + name + '! This is your first API!'}

# Initial static string
static_string = 'Initial Text'

# add additional text
@app.post('/add')
async def add_text(text: str):
  global static_string
  static_string += text
  return{'Message':'Text added', 'current_string': static_string}

# replace text
@app.put('/change')
async def change_text(new_text: str):
  global static_string
  static_string = new_text
  return{'Message':'Text changed','current_string': static_string}

# clears text
@app.delete('/remove')
async def remove_text():
  global static_string
  static_string = ''
  return{'Message': 'Text removed'}