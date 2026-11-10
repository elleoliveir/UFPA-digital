from flask import Flask, render_template, request, jsonify
from rag_engine import rag_instance  # Importa nossa instância já carregada

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    dados = request.json
    pergunta = dados.get('mensagem')
    
    if not pergunta:
        return jsonify({"erro": "Mensagem vazia"}), 400

    try:
        # Chama o motor RAG
        resposta = rag_instance.obter_resposta(pergunta)
        return jsonify({"resposta": resposta})
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"resposta": "Desculpe, ocorreu um erro interno no servidor."}), 500

if __name__ == '__main__':
    # debug=True apenas para desenvolvimento
    app.run(debug=True, port=5000)