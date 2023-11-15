from flask import Flask , render_template ,request

app = Flask(__name__,template_folder='./static' ) 

@app.route("/")
def index():
    return render_template('index.html',resultado={"valid":False,'error':""} )

@app.route('/calcular', methods=['POST'])
def calculoemprestimo():
    prazo=float(request.form['prazo'])    
    renda=float(request.form['renda'])
    valor=float(request.form['valor'])

    limite_minimo = 2000 

    if renda < limite_minimo:
        return render_template('index.html',resultado={"valid":False,'error':'Renda deve ser no minimo ' + str(limite_minimo)} )
    

    taxa_juros_anual = 0.36  # Taxa de juros anual de 36%

    # Cálculo do valor das prestações mensais com juros compostos
    taxa_juros_mensal = (1 + taxa_juros_anual) ** (1 / 12) - 1
    prestacao_mensal = (valor * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -prazo)
    total=prestacao_mensal*prazo
    return render_template('index.html',resultado={"valid":True,'total':round(total,2),'parcelas':round(prestacao_mensal,2)})

