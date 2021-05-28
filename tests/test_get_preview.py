from collections import defaultdict
from pathlib import Path

from git.objects.submodule.base import END



import pytest
import yaml

from pedurma.pecha import *
from pedurma.exceptions import PageNumMissing
from pedurma.reconstruction import get_preview_page, get_preview_text
from pedurma.preprocess import put_derge_line_break, get_derge_hfml_text
from pedurma.texts import get_text_obj, get_durchen_page_obj, get_hfml_text
from pedurma.utils import from_yaml, to_yaml


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
    dg_pecha_path = Path('./tests/data/preview/P791')
    namsel_pecha_path = Path('./tests/data/preview/P792')
    text_id = "D1111"

    derge_google_text_obj = get_text_obj("P791", text_id, dg_pecha_path)
    namsel_text_obj = get_text_obj("P792", text_id, namsel_pecha_path)
    preview_text = defaultdict(str)
    dg_pages = derge_google_text_obj.pages
    dg_notes = derge_google_text_obj.notes
    namsel_pages = namsel_text_obj.pages
    namsel_notes = namsel_text_obj.notes
    for dg_page, namsel_page in zip(dg_pages, namsel_pages):
        vol_num = dg_page.vol
        dg_durchen = get_durchen_page_obj(dg_page, dg_notes)
        namsel_durchen = get_durchen_page_obj(namsel_page, namsel_notes)
        if dg_durchen == None or namsel_durchen == None:
            print('Either of durchen is unable to locate')
            continue
        preview_text[f'v{int(vol_num):03}'] += get_preview_page(dg_page, namsel_page, dg_durchen, namsel_durchen)
    derge_text = from_yaml(Path('./tests/data/preview/D1111_derge.yml'))
    collation_text_with_derge_linebr = put_derge_line_break(preview_text, derge_text)
    expected_preview = Path('./tests/data/preview/D1111_preview.txt').read_text(encoding='utf-8')
    assert collation_text_with_derge_linebr == expected_preview