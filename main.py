from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def root():
    return {"message": "pass"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=433, ssl_keyfile="key.pem", ssl_certfile="cert.pem")