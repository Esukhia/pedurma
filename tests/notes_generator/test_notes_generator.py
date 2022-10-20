from pathlib import Path

import pytest

from pedurma.notes import get_pedurma_edit_notes, get_pedurma_text_edit_notes
from pedurma.pecha import PedurmaNoteEdit
from pedurma.utils import from_yaml

text_meta = {
    "work_id": "W1PD95844",
    "source_metadata": {
        "base": {
            "v001": {
                "image_group_id": "I1PD95846",
                "title": "",
                "order": 1,
                "base_file": "v001.txt",
            },
            "v002": {
                "image_group_id": "I1PD95847",
                "title": "",
                "order": 2,
                "base_file": "v002.txt",
            },
        }
    },
}


def test_notes_generator_crossvol():
    text_id = "D1118"
    hfml_texts = from_yaml(
        (Path(__file__).parent / "data" / "hfmls" / f"{text_id}.yml")
    )
    result = get_pedurma_edit_notes(hfml_texts, text_meta, bdrc_img=False)
    expected_result = [
        PedurmaNoteEdit(
            image_link="https://iiif-dev.bdrc.io/bdr:I1PD95846::I1PD958460004.jpg/full/max/0/default.jpg",
            image_no=4,
            page_no=304,
            ref_start_page_no="264",
            ref_end_page_no="279",
            vol=1,
            base_name="v001",
        ),
        PedurmaNoteEdit(
            image_link="https://iiif-dev.bdrc.io/bdr:I1PD95846::I1PD958460005.jpg/full/max/0/default.jpg",
            image_no=5,
            page_no=305,
            ref_start_page_no="280",
            ref_end_page_no="299",
            vol=1,
            base_name="v001",
        ),
        PedurmaNoteEdit(
            image_link="https://iiif-dev.bdrc.io/bdr:I1PD95846::I1PD958460006.jpg/full/max/0/default.jpg",
            image_no=6,
            page_no=306,
            ref_start_page_no="301",
            ref_end_page_no="304",
            vol=1,
            base_name="v001",
        ),
        PedurmaNoteEdit(
            image_link="https://iiif-dev.bdrc.io/bdr:I1PD95847::I1PD958470004.jpg/full/max/0/default.jpg",
            image_no=4,
            page_no=187,
            ref_start_page_no="180",
            ref_end_page_no="0",
            vol=2,
            base_name="v002",
        ),
        PedurmaNoteEdit(
            image_link="https://iiif-dev.bdrc.io/bdr:I1PD95847::I1PD958470005.jpg/full/max/0/default.jpg",
            image_no=5,
            page_no=188,
            ref_start_page_no="1",
            ref_end_page_no="2",
            vol=2,
            base_name="v002",
        ),
        PedurmaNoteEdit(
            image_link="https://iiif-dev.bdrc.io/bdr:I1PD95847::I1PD958470006.jpg/full/max/0/default.jpg",
            image_no=6,
            page_no=189,
            ref_start_page_no="0",
            ref_end_page_no="0",
            vol=2,
            base_name="v002",
        ),
    ]

    assert result == expected_result


def test_notes_generator():
    text_id = "D1119"
    hfml_texts = from_yaml(
        (Path(__file__).parent / "data" / "hfmls" / f"{text_id}.yml")
    )
    result = get_pedurma_edit_notes(hfml_texts, text_meta, bdrc_img=False)
    expected_result = [
        PedurmaNoteEdit(
            image_link="https://iiif-dev.bdrc.io/bdr:I1PD95847::I1PD958470009.jpg/full/max/0/default.jpg",
            image_no=9,
            page_no=595,
            ref_start_page_no="589",
            ref_end_page_no="0",
            vol=2,
            base_name="v002",
        ),
        PedurmaNoteEdit(
            image_link="https://iiif-dev.bdrc.io/bdr:I1PD95847::I1PD958470010.jpg/full/max/0/default.jpg",
            image_no=10,
            page_no=596,
            ref_start_page_no="595",
            ref_end_page_no="0",
            vol=2,
            base_name="v002",
        ),
    ]

    assert result == expected_result


@pytest.mark.skip(reason="tested functional")
def test_get_pedurma_edit_notes_from_text_id():
    text_id = "D1115"
    pedurma_edit_notes = get_pedurma_text_edit_notes(text_id, bdrc_img=False)
    assert pedurma_edit_notes
