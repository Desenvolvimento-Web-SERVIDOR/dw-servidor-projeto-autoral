# ↓ Importa as ferramentas necessárias do Flask ↓

# Flask: É a ferramenta principal, a classe que usamos para criar nossa aplicação web.
# request: Um objeto que contém todas as informações que o navegador do usuário nos enviou (como o tipo de navegador, qual URL ele pediu, etc.).
# make_response: Uma função para construir um objeto de resposta mais complexo.
# redirect: Uma função para enviar o navegador do usuário para outra URL.
# url_for: Uma função auxiliar para criar URLs para outras rotas do nosso código, em vez de escrevê-las manualmente.
# abort: Uma função para parar a requisição imediatamente e retornar um código de erro (como "Página não encontrada" ou "Acesso Proibido").


#COMENTÁRIO TESTE AAAAAAAAAAAAAAAAAA

from flask import Flask, request, make_response, redirect, url_for, abort

# Cria a instância da aplicação web, guardando na variável app
app = Flask(__name__)

@app.route('/')  # Define a função a ser executada quando o usuário acessa a URL raiz do site
def index():
    return '<h1>Página Inicial</h1><p>Projeto Autoral!</p>'

@app.route('/user/<nome>')  # Cria uma rota dinâmina com base no usuário logado. O <nome> da URL vira um parâmetro na função
def user(nome):
    return f'<h1> Olá, {nome}!</h1><p>Esta é a sua página de usuário.</p>'  # Usamos "f-string" do python para inserir o valor da variável nome diretamente no nosso HTML

@app.route('/contextorequisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')  # Acessamos os cabeçalhos (headers) da requisição para pegar a informação de User-Agent, que é uma string de texto que identifica o navegador e sistema operacional do usuário.
    metodo = request.method  # Pegamos o método HTTP usado
    return f'''
        <h1>Contexto da Requisição</h1>
        <p>Seu navegador é: {user_agent}</p>
        <p>O método HTTP utilizado foi: {metodo}</p>
        '''

@app.route('/codigostatusdiferente')
def codigo_status_diferente():
    return '<h1>Página com status 202</h1>...', 202

@app.route('/objetoresposta')
def objeto_resposta():
    response = make_response('<h1>Esta resposta é um objeto Flask</h1>')  # Usamos make_response para criar um objeto de resposta completo.
    response.headers['X-Custom-Header'] = 'Desenvolvimento Web: Servidor'
    return response

@app.route('/redirecionamento')
def redirecionamento():
    return redirect("https://www.ifsp.edu.br/")

@app.route('/abortar')
def abortar():
    abort(403)  # Esta função interrompe a execução imediatamente e retorna um erro. 403 significa "Forbidden" (Acesso Proibido).

@app.errorhandler(403)  # Esse decorador NÃO cria uma rota, ele executa a função forbidden e exibe o que ela retorna. Permite criar páginas de erro personalizadas
def forbidden(error):
    return '<h1>Acesso Proibido!</h1>...', 403



