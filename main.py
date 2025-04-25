from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversao_temperatura', methods=['POST'])
def conversao_temperatura():
    try:
        celsius = int(request.form['celsius'])
        fahrenheit = round((celsius * 9/5) + 32, 2)
        kelvin = round(celsius + 273.15, 2)
        return render_template('index.html', fahrenheit=fahrenheit, kelvin=kelvin)
    except Exception as e:
        fahrenheit = f'Ocorreu um erro inesperado {e}'
        kelvin = f'Ocorreu um erro inesperado {e}'
        return render_template('index.html', fahrenheit=fahrenheit, kelvin=kelvin)

if __name__ == '__main__':
    app.run(debug=True)
