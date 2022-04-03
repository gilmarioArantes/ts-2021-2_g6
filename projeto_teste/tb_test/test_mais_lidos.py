import requests


class TestMaisLidos:
    url = f"https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json"
    params = {"api-key": "4V1DgnkBJokayF68aMYaDGu4RJDWk8Zn"}

    def test_obter_mais_lidos(self):
        resposta = requests.get(url=self.url, params=self.params)
        assert resposta.status_code == 200

    def test_status_obter_mais_lidos_sem_api_key(self):
        resposta = requests.get(url=self.url)
        assert resposta.status_code == 401

    def test_tipo_retorno_api(self):
        resposta = requests.get(url=self.url, params=self.params)
        assert isinstance(resposta.json(), dict)

    def test_retorno_api_com_http(self):
        resposta = requests.get(url=self.url.replace("https", "http"), params=self.params)
        assert resposta.status_code == 200

