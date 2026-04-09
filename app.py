from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Database
items = [
    {"id": 1, "item": "pen"},
    {"id": 2, "item": "pencil"},
    {"id": 3, "item": "book"}
]

# Model for creating new item
class NewItem(BaseModel):
    name: str  # Only name, ID will be auto-generated

# GET - List all items
@app.get("/items")
def get_items():
    return {"items": items}

# GET - Get one item
@app.get("/items/{item_id}")
def get_one_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# POST - Create new item
@app.post("/items", status_code=201)
def add_item(item: NewItem):
    # Generate new ID (max existing ID + 1)
    new_id = max([i["id"] for i in items]) + 1 if items else 1
    new_item = {"id": new_id, "item": item.name}
    items.append(new_item)
    return new_item

# PUT - Update existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: NewItem):
    for i in range(len(items)):
        if items[i]["id"] == item_id:
            items[i]["item"] = item.name
            return {"message": "Item updated", "item": items[i]}
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE - Remove item
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for i in range(len(items)):
        if items[i]["id"] == item_id:
            items.pop(i)
            return  # No content
    raise HTTPException(status_code=404, detail="Item not found")