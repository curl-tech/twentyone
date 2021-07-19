import uvicorn
from Backend.app import config

if __name__=="__main__":
    uvicorn.run("Backend.app.app:app", host=config.settings.HOST, port=config.settings.PORT, reload=config.settings.DEBUG_MODE)     
    #Location is specified as app/test.py and it is the main fastapi file
    #HOST, PORT and DEBUG_MODE can be configured in config.py