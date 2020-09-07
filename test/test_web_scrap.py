from web_scraper.web_scraper import get_citations_needed_count,get_citations_needed_report

def test_connection():
    pass

def test_verify_count():
    expected='Number of citation :6'
    actual=get_citations_needed_count()
    assert expected==actual

def test_verfiy_passage():
    passages=get_citations_needed_report()
    expected=True
    for p in passages:

        actual='[citation needed]' in p['paragraph need for citation']
        assert expected==actual
