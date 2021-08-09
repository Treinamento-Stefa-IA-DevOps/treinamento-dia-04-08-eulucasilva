import pickle
from fastapi import FastAPI, Query

app = FastAPI(
    title = "API Sobrevivência Titanic",
    version = "1.0.0",
    description  = "Prediz se um pessoa com determinadas características passadas como parâmetro é capaz de sobreviver a algum possível acidente do Titanic"
)


@app.post('/model', status_code=200)
## Coloque seu codigo na função abaixo
def titanic(*, Sex:int = Query(..., ge=0, le=1), Age:float = Query(..., gt=0.1), Lifeboat:int, Pclass: int = Query(..., ge=1, le=3)):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
    
    predicao = titanic.predict([[Sex, Age, Lifeboat, Pclass]]).tolist() 
    mensagem = "Você morreria no Titanic!"

    #print(mensagem)
    #print (predicao)
    survivor = bool(predicao[0])
    #print (survivor)
    
    if survivor:
        mensagem = "Predição realizada com sucesso: Você sobreviveria ao Titanic. Ufa!"

    #print(mensagem)
    return {
        'survived': survivor,
        'status': 200,
        'message': mensagem
    }

@app.get('/model')
def get():
    return "API para predição de sobrevivência do Titanic"
