
from fastapi import FastAPI
from routers import animal, animal_association
import uvicorn


app = FastAPI()


@app.on_event(event_type='startup')
def startup_event():
    print('Startup event')


@app.on_event(event_type='shutdown')
def shutdown_event():
    print('Shut down')


app.include_router(router=animal.router)
app.include_router(
    router=animal_association.router,
    prefix='/admin'
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == '__main__':
    uvicorn.run(app=app)


