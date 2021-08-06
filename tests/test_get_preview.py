import re
import pytest

from collections import defaultdict
from pathlib import Path

from pedurma.pecha import *
from pedurma.exceptions import PageNumMissing
from pedurma.reconstruction import get_preview_page, get_preview_text, split_text, create_docx
from pedurma.utils import from_yaml

def get_dummy_preview():
    dg_pecha_path = Path('./tests/data/preview/P791')
    namsel_pecha_path = Path('./tests/data/preview/P792')
    text_id = "D1111"
    pecha_paths = {
        'namsel': namsel_pecha_path,
        'google': dg_pecha_path
    }
    preview_text = get_preview_text(text_id, pecha_paths)
    return preview_text

def test_get_preview_page():
    gb_pg_yml = from_yaml(
        Path("./tests/data/page_obj/109b_dg.yml")
    )
    g_body_page = Page(
        id=gb_pg_yml["id"],
        page_no=gb_pg_yml["page_no"],
        content=gb_pg_yml["content"],
        name=gb_pg_yml["name"],
        vol=gb_pg_yml["vol"],
        image_link=gb_pg_yml["image_link"],
        note_ref=gb_pg_yml["note_ref"],
    )
    nb_pg_yml = from_yaml(
        Path("./tests/data/page_obj/109b_n.yml")
    )
    n_body_page = Page(
        id=nb_pg_yml["id"],
        page_no=nb_pg_yml["page_no"],
        content=nb_pg_yml["content"],
        name=nb_pg_yml["name"],
        vol=nb_pg_yml["vol"],
        image_link=nb_pg_yml["image_link"],
        note_ref=nb_pg_yml["note_ref"],
    )
    gd_pg_yml = from_yaml(
        Path("./tests/data/notes_page_obj/113a_g.yml")
    )
    g_durchen_page = NotesPage(
        id=gd_pg_yml["id"],
        page_no=gd_pg_yml["page_no"],
        content=gd_pg_yml["content"],
        name=gd_pg_yml["name"],
        vol=gd_pg_yml["vol"],
        image_link=gd_pg_yml["image_link"],
    )
    nd_pg_yml = from_yaml(
        Path("./tests/data/notes_page_obj/113a_n.yml")
    )
    n_durchen_page = NotesPage(
        id=nd_pg_yml["id"],
        page_no=nd_pg_yml["page_no"],
        content=nd_pg_yml["content"],
        name=nd_pg_yml["name"],
        vol=nd_pg_yml["vol"],
        image_link=nd_pg_yml["image_link"],
    )
    expected_prev_page = Path(
        "./tests/data/prev_pg.txt"
    ).read_text(encoding="utf-8")
    preview_page = get_preview_page(
        g_body_page, n_body_page, g_durchen_page, n_durchen_page
    )
    assert expected_prev_page == preview_page


def test_page_num_missing():
    with pytest.raises(PageNumMissing):
        gb_pg_yml = from_yaml(
        Path("./tests/data/page_obj/19a_dg.yml")
        )
        g_body_page = Page(
            id=gb_pg_yml["id"],
            page_no=gb_pg_yml["page_no"],
            content=gb_pg_yml["content"],
            name=gb_pg_yml["name"],
            vol=gb_pg_yml["vol"],
            image_link=gb_pg_yml["image_link"],
            note_ref=gb_pg_yml["note_ref"],
        )
        nb_pg_yml = from_yaml(
            Path("./tests/data/page_obj/19a_n.yml")
        )
        n_body_page = Page(
            id=nb_pg_yml["id"],
            page_no=nb_pg_yml["page_no"],
            content=nb_pg_yml["content"],
            name=nb_pg_yml["name"],
            vol=nb_pg_yml["vol"],
            image_link=nb_pg_yml["image_link"],
            note_ref=nb_pg_yml["note_ref"],
        )
        gd_pg_yml = from_yaml(
            Path("./tests/data/notes_page_obj/13a_g.yml")
        )
        g_durchen_page = NotesPage(
            id=gd_pg_yml["id"],
            page_no=gd_pg_yml["page_no"],
            content=gd_pg_yml["content"],
            name=gd_pg_yml["name"],
            vol=gd_pg_yml["vol"],
            image_link=gd_pg_yml["image_link"],
        )
        nd_pg_yml = from_yaml(
            Path("./tests/data/notes_page_obj/13a_n.yml")
        )
        n_durchen_page = NotesPage(
            id=nd_pg_yml["id"],
            page_no=nd_pg_yml["page_no"],
            content=nd_pg_yml["content"],
            name=nd_pg_yml["name"],
            vol=nd_pg_yml["vol"],
            image_link=nd_pg_yml["image_link"],
        )
        preview_page = get_preview_page(
            g_body_page, n_body_page, g_durchen_page, n_durchen_page)

def test_get_preview_text():
    preview_text = get_dummy_preview()
    expected_preview = Path('./tests/data/preview/D1111_preview.txt').read_text(encoding='utf-8')
    assert preview_text['v001'] == expected_preview


def test_get_docx_text():
    collation_text = ''
    text_id = "D1111"
    output_path = Path.home()
    preview_text = get_dummy_preview()
    for vol_id, text in preview_text.items():
        collation_text += f"{text}\n\n"
    collation_text = collation_text.replace('\n', '')
    collation_text = re.sub(r'(\|.+?\|)', r'\n\g<1>\n', collation_text)
    chunks = split_text(collation_text)
    docx_path = create_docx(text_id, chunks, output_path)
    expected_path = Path.home() / "D1111.docx"
    assert docx_path == expected_path
    expected_path.unlink()