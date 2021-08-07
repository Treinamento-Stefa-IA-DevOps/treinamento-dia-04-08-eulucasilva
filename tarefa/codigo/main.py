import pickle
from fastapi import FastAPI, status

app = FastAPI(
    title = "API Sobrevivência Titanic",
    version = "1.0.0",
    description  = "Prediz se um pessoa com determinadas características passadas como parâmetro é capaz de sobreviver a algum possível acidente do Titanic"
)


@app.post('/model', status_code=200)
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass: int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
        predicao = titanic.predict([[Sex, Age, Lifeboat, Pclass]]).tolist() 
       
    return {
        'survived': predicao,
        'status': status.HTTP_200_CREATED,
        'message': "Predição realizada com sucesso: Você sobreviveria ao Titanic. Ufa!"
    }

@app.get('/model')
def get():
    return "API para predição de sobrevivência do Titanic"
