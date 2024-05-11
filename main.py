from fastapi import FastAPI
from fastapi import Form

from typing import Annotated

from pydantic import EmailStr

app = FastAPI()

@app.post("/login")
async def login(email: Annotated[EmailStr, Form()], password: Annotated[str, Form()]):
  return {"email": email}
