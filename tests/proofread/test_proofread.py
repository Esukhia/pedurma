from pathlib import Path

from pedurma.pecha import ProofreadNotePage
from pedurma.proofreading import get_note_page, get_note_pages


def test_get_note_page():
    text_id = "D1119"
    repo_path = Path(__file__).parent / "data" / "note_page"
    expected_page = ProofreadNotePage(
        manual="manual_note",
        google="google_note",
        img_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460720.jpg/full/max/0/default.jpg",
        page_num=720,
    )

    proofread_page = get_note_page(text_id, cur_pg_num=720, repo_path=repo_path)

    assert expected_page == proofread_page


def test_get_note_pages():
    text_id = "D1119"
    repo_path = Path(__file__).parent / "data" / "note_page"
    expected_note_pages = [
        ProofreadNotePage(
            manual="manual_note",
            google="google_note",
            img_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460720.jpg/full/max/0/default.jpg",
            page_num=720,
        )
    ]

    note_pages = get_note_pages(text_id, repo_path)
    assert expected_note_pages == note_pages
