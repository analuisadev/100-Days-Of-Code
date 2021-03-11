from Day_95_96_97_98 import app


@app.route("/") #definindo rota para a página
def index(): #função para pag principal
    return "Hello World"
