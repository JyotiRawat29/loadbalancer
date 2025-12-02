from fastapi import FastAPI
import uvicorn

app =FastAPI()

@app.get("/")
async def hello():
    return {"message":"hello is it working"}

if __name__=='__main__':
    uvicorn.run("app:app",host="0.0.0.0", port = 8000, reload=True)