from pathlib import Path
from pedurma.texts import get_page_with_note_obj


def test_page_with_note_obj():
    text_id = "D1119_1"
    pg_id = '228'
    base_path = Path('./tests/data/page_with_note/')
    pg_obj = get_page_with_note_obj(text_id, pg_id, base_path)