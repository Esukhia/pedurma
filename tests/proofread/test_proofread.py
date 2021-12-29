from pathlib import Path

from pedurma.pecha import ProofreadNotePage
from pedurma.proofreading import get_note_page


def test_get_note_page():
    text_id = "D1119"
    repo_path = Path(__file__).parent / "data" / "note_page"
    expected_page = ProofreadNotePage(
        manual="manual_note",
        google="google_note",
        img_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460720.jpg/full/max/0/default.jpg",
        page_num=720,
    )

    proofread_page = get_note_page(text_id, repo_path=repo_path)

    assert expected_page == proofread_page
