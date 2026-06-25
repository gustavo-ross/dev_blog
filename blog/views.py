from django.http import HttpResponse


def home(request):
    mensagem = "<h1>Bem-Vindo ao Devblog!</h1> <p>Em breve, artigos aqui.</p>"

    return HttpResponse(mensagem)


def sobre_nos(request):
    mensagem = "<h1>Sobre o Devblog!</h1> <p>Ainda nem existe, então não tem muito o que falar.</p>"

    return HttpResponse(mensagem)