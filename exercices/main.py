from fastapi import FastAPI, Body
app = FastAPI()

students = [
    {'ID':'001','name':'Ben Mulumba', 'course': 'Computer science' },    
    {'ID':'002','name':'Elysee Lompegnu','course': 'Business admistration' },
    {'ID':'003','name':'Jhon', 'course': 'Epidemology' },
    {'ID':'004','name':'Maurice', 'course': 'Math' }
]

@app.get('/students')
async def all_students ():
    return students