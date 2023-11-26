from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def f_index():
    return 'Кучин Тимур Анатольевич'


@app.get('/tools')
async def f_indexT():
    return '+7-961-240-22-66'


@app.get('/users')
async def f_indexU():
    return 'C#, Python, Git, PostgreSQL'
