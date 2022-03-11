import os
from pathlib import Path

import pytest

from pedurma.preview import get_preview_text


def test_get_preview_text():
    dg_pecha_path = str(Path(__file__).parent / "data" / "P972")
    namsel_pecha_path = str(Path(__file__).parent / "data" / "P973")
    text_id = "D1119"
    pecha_paths = {"namsel": namsel_pecha_path, "google": dg_pecha_path}
    output_path = Path.home()
    expected_output_path = Path.home() / text_id
    expected_pecha_id = "P972"
    preview_output_path, google_pecha_id = get_preview_text(
        text_id, output_path, pecha_paths, bdrc_img=False
    )
    assert expected_output_path == preview_output_path
    assert expected_pecha_id == google_pecha_id
    os.system(f"rm -r {str(expected_output_path)}")
