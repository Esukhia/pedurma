from pathlib import Path
from pedurma.preprocess import get_derge_google_text

def test_get_derge_google_hfml():
    derge_hfml = Path('./tests/data/hfmls/derge_D1119.txt').read_text(encoding='utf-8')
    google_hfml = Path('./tests/data/hfmls/google_D1119.txt').read_text(encoding='utf-8')
    expected_hfml = Path('./tests/data/hfmls/derge_google_D1119.txt').read_text(encoding='utf-8')
    derge_google_hfml = get_derge_google_text(derge_hfml, google_hfml)
    assert expected_hfml == derge_google_hfml