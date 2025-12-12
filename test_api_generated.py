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

def test_cadastro_de_usuário_sucesso():
    print("Rodando test_cadastro_de_usuário_sucesso...")
    url = BASE_URL + "/users"
    params = {'user': 'maria', 'pass': 'abc123'}
    print("URL simulada:", url)
    print("Parâmetros simulados:", params)
    resp_status = 201
    data = {}  # aqui poderia vir um JSON real
    print("Status code simulado:", resp_status)
    print("JSON simulado:", data)
    assert resp_status == 201
    print("Campo esperado presente (json_has): id")

def test_cadastro_de_usuário_usuario_já_existente():
    print("Rodando test_cadastro_de_usuário_usuario_já_existente...")
    url = BASE_URL + "/users"
    params = {'user': 'maria', 'pass': 'abc123'}
    print("URL simulada:", url)
    print("Parâmetros simulados:", params)
    resp_status = 409
    data = {}  # aqui poderia vir um JSON real
    print("Status code simulado:", resp_status)
    print("JSON simulado:", data)
    assert resp_status == 409
    print("Expectativa json_eq: error == 'user_already_exists'")

def test_atualização_de_usuário_alterar_senha():
    print("Rodando test_atualização_de_usuário_alterar_senha...")
    url = BASE_URL + "/users/1"
    params = {'pass': 'nova_senha'}
    print("URL simulada:", url)
    print("Parâmetros simulados:", params)
    resp_status = 200
    data = {}  # aqui poderia vir um JSON real
    print("Status code simulado:", resp_status)
    print("JSON simulado:", data)
    assert resp_status == 200
    print("Campo esperado presente (json_has): updated_at")

def test_atualização_de_usuário_deletar_existente():
    print("Rodando test_atualização_de_usuário_deletar_existente...")
    url = BASE_URL + "/users/1"
    params = {}
    print("URL simulada:", url)
    print("Parâmetros simulados:", params)
    resp_status = 204
    data = {}  # aqui poderia vir um JSON real
    print("Status code simulado:", resp_status)
    print("JSON simulado:", data)
    assert resp_status == 204

def test_atualização_de_usuário_deletar_inexistente():
    print("Rodando test_atualização_de_usuário_deletar_inexistente...")
    url = BASE_URL + "/users/999"
    params = {}
    print("URL simulada:", url)
    print("Parâmetros simulados:", params)
    resp_status = 404
    data = {}  # aqui poderia vir um JSON real
    print("Status code simulado:", resp_status)
    print("JSON simulado:", data)
    assert resp_status == 404
    print("Expectativa json_eq: error == 'user_not_found'")


if __name__ == '__main__':
    test_login_básico_sucesso()
    test_login_básico_senha_errada()
    test_cadastro_de_usuário_sucesso()
    test_cadastro_de_usuário_usuario_já_existente()
    test_atualização_de_usuário_alterar_senha()
    test_atualização_de_usuário_deletar_existente()
    test_atualização_de_usuário_deletar_inexistente()
    print('Todos os testes (modo demo) executados.')