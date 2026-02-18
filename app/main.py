import uvicorn
from fastapi import FastAPI
from app.api import base as api_endpoints

app=FastAPI()

@app.get('/')
def general():
    return {'message': 'General age'}


app.include_router(api_endpoints.v1_endpoints)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)