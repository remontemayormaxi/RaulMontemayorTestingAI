from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos simulados
articulos = [
    {"id": 1, "titulo": "Introducción a la IA", "contenido": "Contenido sobre IA", "fecha": "2024-04-01", "categoria": "Tecnología"},
    {"id": 2, "titulo": "Aprendiendo Flask", "contenido": "Cómo usar Flask en Python", "fecha": "2024-03-20", "categoria": "Programación"},
    {"id": 3, "titulo": "Ultimos avances en Ciencia", "contenido": "Nuevos descubrimientos", "fecha": "2024-02-15", "categoria": "Ciencia"}
]

@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('q', '').lower()
    resultados = [art for art in articulos if query in art["titulo"].lower()]
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
