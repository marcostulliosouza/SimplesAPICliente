import requests

def obter_usuarios():
    # URL da API JSONPlaceholder para obter dados de usuários
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        resposta = requests.get(url)

        # Verificando se a requisição foi bem-sucedida (código de status 200)
        if resposta.status_code == 200:
            # Convertendo a resposta para formato JSON
            dados_usuarios = resposta.json()

            # Exibindo os dados dos usuários
            for usuario in dados_usuarios:
                print(f"Nome: {usuario['name']}, Email: {usuario['email']}")
        else:
            print(f"Erro na requisição. Código de status: {resposta.status_code}")

    except Exception as e:
        print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    obter_usuarios()
