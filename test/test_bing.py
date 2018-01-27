from bs4 import BeautifulSoup

from app.scrapers import Bing


def test_parse_response():
    html_text = """<li class="b_algo">
        <h2><a href="mock_url">mock_title</h2>
        <div class="b_caption"><p>mock_desc</p>
        </div><li>"""
    dummy_soup = BeautifulSoup(html_text, 'html.parser')
    resp = Bing().parse_response(dummy_soup)
    expected_resp = [{
        'title': u'mock_title',
        'link': u'mock_url',
        'desc': u'mock_desc'
    }]
    assert resp == expected_resp


def test_parse_image_response():
    html_text = """<a class="iusc" href="mock_url">mock_title</a>"""
    dummy_soup = BeautifulSoup(html_text, 'html.parser')
    resp = Bing().parse_image_response(dummy_soup)
    link_image = 'https://www.bing.com' + 'mock_url'
    expected_resp = [{
        'link': link_image
    }]
    assert resp == expected_resp


def test_parse_video_response():
    html_text = """<a aria-label="mock_title Duration" class="mc_vtvc_link"
        href="mock_url"></a>"""
    dummy_soup = BeautifulSoup(html_text, 'html.parser')
    resp = Bing().parse_video_response(dummy_soup)
    link_video = 'https://www.bing.com' + 'mock_url'
    expected_resp = [{
        'title': u'mock_title',
        'link': link_video,
    }]
    assert resp == expected_resp


def test_parse_news_response():
    html_text = """<div class="t_s"><div class="t_t"><a class="title" href="mock_link">mock_title</a></div><div class="snippet">mock_desc</div></div>"""
    dummy_soup = BeautifulSoup(html_text, 'html.parser')
    resp = Bing().parse_news_response(dummy_soup)
    expected_resp = [{
        'title': u'mock_title',
        'link': u'mock_link',
        'desc': u'mock_desc'
    }]
    assert resp == expected_resp
