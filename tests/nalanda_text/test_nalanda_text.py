from pathlib import Path

from pedurma.nalanda_text import Pedurma
from pedurma.pecha import PageWithNote
from pedurma.utils import to_yaml


def get_empty_note(note_link, vol):
    page_note = {"notes": {}, "note_pg_link": note_link, "vol": vol}
    page_note = to_yaml(page_note)
    return page_note


def test_get_page():
    text_id = "D1119_001"
    page_id = "0229"
    base_path = Path(__file__).parent / "data" / "page_with_note"
    project_name = "nalanda"
    pedurma = Pedurma(project_name, base_path)
    pg_obj = pedurma.get_page(text_id, page_id)
    expected_pg_obj = PageWithNote(
        text_id=text_id,
        page_id=page_id,
        content="༄༅༅། །རྒྱ་གར་སྐད་དུ། ནི་རུ་#པ་མ་སྟ་བཾ།#𰶧 བོད་སྐད་དུ། དཔེ་མེད་",
        page_image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460229.jpg/full/max/0/default.jpg",
        note="'1':\n  《པེ་》: ལྟར་བཀོད།\n  《སྣར་》: ལྟར་བཀོད།\n  《སྡེ》: ''\n  《ཅོ་》: ''\n",
        note_image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460231.jpg/full/max/0/default.jpg",
    )
    assert pg_obj == expected_pg_obj


def test_save_page():
    text_id = "D1119_001"
    page_id = "0230"
    base_path = Path(__file__).parent / "data" / "page_with_note"
    project_name = "nalanda"
    note_pg_link = (
        "https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460231.jpg/full/max/0/default.jpg"
    )
    # create empty page
    (base_path / project_name / f"{text_id}/pages/{page_id}.txt").write_text(
        "", encoding="utf-8"
    )
    # creat empty note
    empty_pg_note = get_empty_note(note_pg_link, vol=1)
    (base_path / project_name / f"{text_id}/notes/{page_id}.yml").write_text(
        empty_pg_note, encoding="utf-8"
    )
    pedurma = Pedurma(project_name, base_path)
    new_pg_obj = PageWithNote(
        text_id=text_id,
        page_id=page_id,
        content="༄༅༅། །རྒྱ་གར་སྐད་དུ། ནི་རུ་#པ་མ་སྟ་བཾ།#𰶧 བོད་སྐད་དུ། དཔེ་མེད་",
        page_image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460230.jpg/full/max/0/default.jpg",
        note="'1':\n  《པེ་》: ལྟར་བཀོད།\n  《སྣར་》: ལྟར་བཀོད།\n  《སྡེ》: ''\n  《ཅོ་》: ''\n",
        note_image_link=note_pg_link,
    )
    pedurma.save_page(new_pg_obj)
    saved_pg_obj = pedurma.get_page(text_id, page_id)
    assert new_pg_obj == saved_pg_obj
    (base_path / project_name / text_id / "pages" / f"{page_id}.txt").unlink()
    (base_path / project_name / text_id / "notes" / f"{page_id}.yml").unlink()


def test_get_reinsert_preview_pg():
    text_id = "D1119_001"
    pg_id = "0228"
    base_path = Path(__file__).parent / "data" / "page_with_note"
    project_name = "nalanda"
    pedurma = Pedurma(project_name, base_path)
    pg_obj = pedurma.get_page(text_id, pg_id)
    preview_pg = pedurma.get_preview(pg_obj)
    expected_preview_pg = (
        Path(__file__).parent / "data" / "page_with_note" / "preview_pg.txt"
    ).read_text(encoding="utf-8")
    assert expected_preview_pg == preview_pg


def test_download_text():
    text_id = "D1119_001"
    base_path = Path(__file__).parent / "data" / "page_with_note"
    project_name = "nalanda"
    pedurma = Pedurma(project_name, base_path)
    collation_text = pedurma.get_collation_text(text_id)
    expected_collation_text = (base_path / "collation_text.txt").read_text(
        encoding="utf-8"
    )
    assert expected_collation_text == collation_text
