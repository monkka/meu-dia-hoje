from flask import Flask, render_template, request, redirect, url_for
from datetime import date

import random

frases = [
    "Hoje é dia de brilhar (ou pelo menos tentar 😅).",
    "Se não for pra arrasar, nem levanta da cama!",
    "Tarefa por tarefa, a gente domina o mundo. 💪",
    "Vai com sono mesmo, mas vai!",
    "Meta do dia: sobreviver com estilo 😎.",
    "Organizada sim, cansada também.",
    "Checklists são o novo superpoder. 🦸‍♀️",
    "Se eu não fizer hoje, amanhã sou eu que sofro. 😬",
    "Tô pronta pra fingir que sou produtiva!",
    "A vida é uma planilha, e eu tô tentando não dar erro.",
    "Tem dias que a gente precisa chutar o balde e pisar na areia. ⛱️",
    "I never cry (just watching movies), and I am so productive🎶  . It's an art!",
    "Menos é mais. Ser simples requer tempo e esforço.",
    "Ninguém está seguro quando pensa ser seu privilégio decidir por si mesmo"
]

frase_do_dia = ""
data_frase = None

app = Flask(__name__)
tarefas = []
resolvidas = []

@app.route("/", methods=["GET", "POST"])
def index():
    global tarefas, resolvidas, frase_do_dia, data_frase

    if request.method == "POST":
        nova = request.form.get("nova_tarefa")
        if nova:
            tarefas.append(nova)
        return redirect(url_for("index"))

    hoje = date.today()
    if data_frase != hoje:
        frase_do_dia = random.choice(frases)
        data_frase = hoje

    return render_template("index.html", tarefas=tarefas, resolvidas=resolvidas, frase_do_dia=frase_do_dia)

@app.route("/resolver/<int:id>", methods=['POST'])
def resolver(id):
    global tarefas, resolvidas
    resolvidas.append(tarefas[id])
    tarefas.pop(id)
    return redirect(url_for("index"))

@app.route("/acabou", methods=["POST"])
def limpar_resolvidas():
    global resolvidas
    resolvidas = []
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
