<<<<<<< HEAD
from fastapi import FastAPI
=======
print("HELLO WORLD")


from flask import Flask
>>>>>>> 975f4b01cf95c44cb08606c8c79aaaeea75024f7

app = FastAPI()


<<<<<<< HEAD
@app.get("/")
async def root():
    return {"message": "Hello World"}
=======
@app.route("/",methods=['POST','GET'])
def newfun():
    return {'status': 'home!'}


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
>>>>>>> 975f4b01cf95c44cb08606c8c79aaaeea75024f7
