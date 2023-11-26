from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def f_index():
    return {"FIO": "Кучин Тимур Анатольевич"}


@app.get('/tools')
async def f_indexT():
    return {"Phone": "+7-961-240-22-66"}


@app.get('/users')
async def f_indexU():
    return {"Skills": "C#, Python, Git, PostgreSQL"}
