from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculadora.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        # Obtener los datos del formulario
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacion = request.form['operacion']
        
        # Realizar la operación seleccionada
        if operacion == 'suma':
            resultado = num1 + num2
            operador = '+'
        elif operacion == 'resta':
            resultado = num1 - num2
            operador = '-'
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
            operador = '×'
        elif operacion == 'division':
            if num2 != 0:
                resultado = num1 / num2
                operador = '÷'
            else:
                return render_template('calculadora.html', error="Error: No se puede dividir entre cero")
        else:
            return render_template('calculadora.html', error="Error: Operación no válida")
        
        # Formatear el resultado
        if resultado == int(resultado):
            resultado = int(resultado)
        
        return render_template('calculadora.html', 
                             resultado=resultado, 
                             num1=num1, 
                             num2=num2, 
                             operador=operador)
    
    except ValueError:
        return render_template('calculadora.html', error="Error: Por favor ingresa números válidos")
    except Exception as e:
        return render_template('calculadora.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)