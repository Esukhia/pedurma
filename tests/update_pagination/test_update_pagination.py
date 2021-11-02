from pathlib import Path

from pedurma.pagination_update import update_pagination
from pedurma.pecha import PedurmaNoteEdit
from pedurma.utils import from_yaml


def test_pagination_update_crossvol():
    pecha_id = "c1f25688a5da47c1be49a5c0eb0326a5"
    text_id = "D1118"
    pecha_path = (Path(__file__).parent / "data")
    
    index = from_yaml((Path(__file__).parent / "data" / f"{pecha_id}.opf" / "index.yml"))
    pages_to_edit = [
        PedurmaNoteEdit(
            image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460004.jpg/full/max/0/default.jpg",
            image_no=4,
            page_no=4,
            ref_start_page_no="1",
            ref_end_page_no="3",
            vol=1,
        ),
        PedurmaNoteEdit(
            image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460005.jpg/full/max/0/default.jpg",
            image_no=5,
            page_no=5,
            ref_start_page_no="4",
            ref_end_page_no="4",
            vol=1,
        ),
        PedurmaNoteEdit(
            image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470004.jpg/full/max/0/default.jpg",
            image_no=4,
            page_no=4,
            ref_start_page_no="1",
            ref_end_page_no="3",
            vol=2,
        ),
        PedurmaNoteEdit(
            image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470005.jpg/full/max/0/default.jpg",
            image_no=5,
            page_no=5,
            ref_start_page_no="0",
            ref_end_page_no="0",
            vol=2,
        ),
    ]
    for vol, new_pagination_layer in update_pagination(
        pecha_id, text_id, pages_to_edit, index, pecha_path
    ):
        expected_layer = from_yaml((Path(__file__).parent / "data" / "paginations" / text_id / f"v{int(vol):03}.yml"))
        assert new_pagination_layer == expected_layer


def test_pagination_update():
    pecha_id = "e5248654f5e44f8e9216f3f38ed75ee8"
    text_id = "D1119"
    pecha_path = (Path(__file__).parent / "data")
    index = from_yaml((Path(__file__).parent / "data" / f"{pecha_id}.opf" / "index.yml"))
    pages_to_edit = [
        PedurmaNoteEdit(
            image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470004.jpg/full/max/0/default.jpg",
            image_no=9,
            page_no=9,
            ref_start_page_no="7",
            ref_end_page_no="8",
            vol=2,
        ),
        PedurmaNoteEdit(
            image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470005.jpg/full/max/0/default.jpg",
            image_no=10,
            page_no=10,
            ref_start_page_no="0",
            ref_end_page_no="0",
            vol=2,
        ),
    ]
    for vol, new_pagination_layer in update_pagination(
        pecha_id, text_id, pages_to_edit, index, pecha_path
    ):
        expected_layer = from_yaml((Path(__file__).parent / "data" / "paginations" / text_id / f"v{int(vol):03}.yml"))
        assert new_pagination_layer == expected_layer


def test_invalid_pg_ref():
    pecha_id = "e5248654f5e44f8e9216f3f38ed75ee8"
    text_id = "D1119"
    pecha_path = (Path(__file__).parent / "data")
    index = from_yaml((Path(__file__).parent / "data" / f"{pecha_id}.opf" / "index.yml"))
    pages_to_edit = [
        PedurmaNoteEdit(
            image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470004.jpg/full/max/0/default.jpg",
            image_no=9,
            page_no=9,
            ref_start_page_no="9",
            ref_end_page_no="8",
            vol=2,
        ),
        PedurmaNoteEdit(
            image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470005.jpg/full/max/0/default.jpg",
            image_no=10,
            page_no=10,
            ref_start_page_no="7",
            ref_end_page_no="10",
            vol=2,
        ),
    ]
    for vol, new_pagination_layer in update_pagination(
        pecha_id, text_id, pages_to_edit, index, pecha_path
    ):
        expected_layer = from_yaml((Path(__file__).parent / "data" / f"{pecha_id}.opf" / "layers" / "v002" / "Pagination.yml"))
        assert new_pagination_layer == expected_layer
