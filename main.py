from fastapi import FastAPI
import operation
import uvicorn
from pydantic import BaseModel


class add_in(BaseModel):
    inp1: int
    inp2: int

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/add")
async def add(input:add_in):
    value = operation.addition(a = input.inp1,b = input.inp2)
    print(value)
    return {"message": str(value)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=1055)
