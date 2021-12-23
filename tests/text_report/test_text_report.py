from os import path
from pathlib import Path

from pedurma.text_report import get_text_report


def test_text_report():
    pecha_paths = {"google": str(Path(__file__).parent / "data" / "P973")}
    preview_text = {
        "v001": (Path(__file__).parent / "data" / "D1119_preview.txt").read_text(
            encoding="utf-8"
        )
    }
    text_id = "D1119"
    expected_text_report = {
        "toh_no": "D1119",
        "title": "དཔེ་མེད་པར་བསྟོད་པ།",
        "total_number_of_pages": 4,
        "total_number_of_footnotes": 42,
        "download_date": None,
    }
    text_report = get_text_report(text_id, pecha_paths, preview_text)
    assert expected_text_report["toh_no"] == text_report["toh_no"]
    assert expected_text_report["title"] == text_report["title"]
    assert (
        expected_text_report["total_number_of_pages"]
        == text_report["total_number_of_pages"]
    )
    assert (
        expected_text_report["total_number_of_footnotes"]
        == text_report["total_number_of_footnotes"]
    )
