import uvicorn

if __name__=="__main__":
    uvicorn.run("app.test:app", host="0.0.0.0", port=8000, reload=True)     #location is specified as app/test.py and it is the main fastapi file