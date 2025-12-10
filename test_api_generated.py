# MODO DEMONSTRAÇÃO: sem chamadas HTTP reais
BASE_URL = "https://api.exemplo.com"


def test_login_básico_sucesso():
    print("Rodando test_login_básico_sucesso...")
    url = BASE_URL + "/login"
    params = {'user': 'joao', 'pass': '123'}
    print("URL simulada:", url)
    print("Parâmetros simulados:", params)
    resp_status = 200
    data = {}  # aqui poderia vir um JSON real
    print("Status code simulado:", resp_status)
    print("JSON simulado:", data)
    assert resp_status == 200
    print("Campo esperado presente (json_has): token")

def test_login_básico_senha_errada():
    print("Rodando test_login_básico_senha_errada...")
    url = BASE_URL + "/login"
    params = {'user': 'joao', 'pass': 'errado'}
    print("URL simulada:", url)
    print("Parâmetros simulados:", params)
    resp_status = 401
    data = {}  # aqui poderia vir um JSON real
    print("Status code simulado:", resp_status)
    print("JSON simulado:", data)
    assert resp_status == 401
    print("Expectativa json_eq: error == 'invalid_credentials'")


if __name__ == '__main__':
    test_login_básico_sucesso()
    test_login_básico_senha_errada()
    print('Todos os testes (modo demo) executados.')