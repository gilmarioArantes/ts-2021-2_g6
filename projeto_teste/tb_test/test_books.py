import requests


class TestBooks:

    api_key = "4V1DgnkBJokayF68aMYaDGu4RJDWk8Zn"

    def test_status_obtem_livros(self):
        URL = f'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        resposta_dict = resposta.json()
        status = resposta_dict["status"]
        assert status == 'OK'

    def test_qtd_results_obtem_livros(self):
        URL = f'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        resposta_dict = resposta.json()

        num_results = resposta_dict["num_results"]
        results = resposta_dict["results"]

        assert num_results == len(results)
