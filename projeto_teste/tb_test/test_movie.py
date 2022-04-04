import json

import requests


class TestMovieReviews:

    api_key = "4V1DgnkBJokayF68aMYaDGu4RJDWk8Zn"

    def test_status_obtem_filmes_reviews(self):
        URL = f'https://api.nytimes.com/svc/movies/v2/reviews/picks.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        resposta_dict = resposta.json()
        status = resposta_dict["status"]
        assert status == 'OK'

    def test_error_when_have_no_apikey(self):
        URL = f'https://api.nytimes.com/svc/movies/v2/reviews/picks.json?api-key='
        resposta = requests.get(url=URL)
        status = resposta.status_code
        assert status == 401

    def test_busca_por_titulo(self):
        URL = f'https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=godfather&api-key={self.api_key}'
        resposta = requests.get(url=URL)
        resposta_dict = resposta.json()
        myList = resposta_dict["results"]
        resultado = myList[0]
        assert resultado["display_title"].find("Godfather") != -1

    def test_busca_todas_as_criticas(self):
        URL = f'https://api.nytimes.com/svc/movies/v2/critics/all.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        resposta_dict = resposta.json()
        status = resposta_dict["status"]
        num_results = resposta_dict["num_results"]
        assert status == 'OK' and num_results > 1

    def test_busca_criticas_full_time(self):
        URL = f'https://api.nytimes.com/svc/movies/v2/critics/full-time.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        resposta_dict = resposta.json()
        status = resposta_dict["status"]
        num_results = resposta_dict["num_results"]
        assert status == 'OK' and num_results > 1

    def test_busca_criticas_part_time(self):
        URL = f'https://api.nytimes.com/svc/movies/v2/critics/part-time.json?api-key={self.api_key}'
        resposta = requests.get(url=URL)
        resposta_dict = resposta.json()
        status = resposta_dict["status"]
        num_results = resposta_dict["num_results"]
        assert status == 'OK' and num_results > 1

