import requests


class TestArtigos:

    api_key = "4V1DgnkBJokayF68aMYaDGu4RJDWk8Zn"

    def test_status_obtem_artigos(self):
        URL = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key={self.api_key}'
        resposta = requests.get(url=URL)
        resposta_dict = resposta.json()
        status = resposta_dict["status"]
        assert status == 'OK'

    def test_retorno_api(self):
        URL = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key={self.api_key}'
        resposta = requests.get(url=URL)
        return resposta.json()
        assert true
