import requests


class TestArtigos:

    api_key = "4V1DgnkBJokayF68aMYaDGu4RJDWk8Zn"

    def test_status_obtem_artigos(self):
        URL = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key={self.api_key}'
        resposta = requests.get(url=URL)
        resposta_dict = resposta.json()
        status = resposta_dict["status"]
        assert status == 'OK'

    def test_tag_query(self):
        URL = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?tag_query("Obama", max_results=2)&api-key={self.api_key}'
        assert 2, len(URL)

    def test_article_search(self):
        URL = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?article_search("Joe Biden", results=80)&api-key={self.api_key}'
        assert 80, len(URL)
        for article in URL:
            assert article, dict
    def test_article_metada(self):
        URL = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?.article_metadata("https://www.nytimes.com/live/2021/02/10/us/impeachment-trial/prosecutors-begin-arguments-against-trump-saying-he-became-the-inciter-in-chief-of-a-dangerous-insurrection")&api-key={self.api_key}'
        assert URL, list
        for article in URL:
            assert article, dict


