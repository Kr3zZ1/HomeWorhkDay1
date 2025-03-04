import uvicorn
import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Zerg(BaseModel):
    name : str
    birstday : datetime.date
    fangs : int

class Put_Zerg(BaseModel):
    name : str
    fangs : int

zergs = []

@app.get("/zergs", response_model=list[Zerg])
def get_list():
    return zergs

@app.post("/zerg", response_model=Zerg)
def create_zerg(zerg: Zerg):
    zergs.append(zerg)
    return zerg

@app.put("/zerg/{index}", response_model=Zerg)
def put_zerg(index: int, zerg: Zerg):
    if index < 0 or index >= len(zergs):
        raise HTTPException(status_code=404, detail="Zerg not found")
    zergs[index] = zerg
    return zerg

@app.delete("/zerg/{index}", response_model=Zerg)
def delete_zerg(index: int):
    if index < 0 or index >= len(zergs):
        raise HTTPException(status_code=404, detail="Zerg not found")
    deleted_zerg = zergs.pop(index)  # Удаление элемента по индексу
    return deleted_zerg

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

