import requests


class TestMaisPopulares:

    api_key = "4V1DgnkBJokayF68aMYaDGu4RJDWk8Zn"

    def test_obter_mais_populares_homepage(self):
        URL = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        assert resposta.status_code == 200

    def test_obter_mais_populares_autenticacao_falha(self):
        URL = f'https://api.nytimes.com/svc/topstories/v2/home.json?'
        resposta = requests.get(url=URL)
        assert resposta.status_code == 401

    def test_obter_mais_populares_retorna_json(self):
        URL = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        assert isinstance(resposta.json(), dict)

    def test_obter_mais_populares_politica(self):
        URL = f'https://api.nytimes.com/svc/topstories/v2/politics.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        assert isinstance(resposta.json(), dict)

    def test_obter_mais_populares_ciencia_http(self):
        URL = f'http://api.nytimes.com/svc/topstories/v2/science.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        assert isinstance(resposta.json(), dict)
