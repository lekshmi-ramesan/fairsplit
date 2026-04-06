from fastapi import FastAPI

app = FastAPI()

friends = ["alice","bon","char"]
@app.get("/friends")
def get_all():
    #return{"friends":friends}