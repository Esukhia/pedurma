import os
from pathlib import Path

from openpecha.utils import dump_yaml

from pedurma.pecha import NotesPage, Page, Text
from pedurma.save_text import (
    get_new_vol,
    get_old_vol,
    get_text_vol_span,
    save_pedurma_text,
    update_durchen_layer,
    update_index,
    update_page_layer,
)
from pedurma.texts import get_text_obj, remove_last_pages
from pedurma.utils import from_yaml, to_yaml


def get_dummy_text():
    return Text(
        id="259260e8e3544fc1a9a27d7dffc72df6",
        pages=[
            Page(
                id="1a26fd08bf2b4ebb9e2d7369347e478b",
                page_no=1,
                content="ཉ༄ཚོ། །རྒྱ་གར་སྐད་དུ།\nསྟ་བ་ནཱ་མ། བོད་སྐད་དུ།\nཔར་འོས་པ་བསྔགས་",
                name="Page 1",
                vol="1",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460001.jpg/full/max/0/default.jpg",
                note_ref=[
                    "46d97ed3d9ca4ddabc3c413f306df03a",
                    "46d97ed3d9ca4ddabc3c413f306df03a",
                ],
            ),
            Page(
                id="e8e314a7457b40348b5dd7a744004900",
                page_no=2,
                content="གཏམ་འདི་ཙམ\nའདི་ཉིད་སྨྲ་བར་\nདང་-། །ཁྱོད་མ",
                name="Page 2",
                vol="1",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460002.jpg/full/max/0/default.jpg",
                note_ref=[
                    "46d97ed3d9ca4ddabc3c413f306df03a",
                    "46d97ed3d9ca4ddabc3c413f306df03a",
                ],
            ),
            Page(
                id="29c64dc1fa624b42b08814ca4f3a78b4",
                page_no=3,
                content="འདོད་གང་དག་\nསྐྱབས་འགྲོ་བ།\nསྟོང་གིས་ཀྱང་།",
                name="Page 3",
                vol="1",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460003.jpg/full/max/0/default.jpg",
                note_ref=[
                    "46d97ed3d9ca4ddabc3c413f306df03a",
                    "46d97ed3d9ca4ddabc3c413f306df03a",
                ],
            ),
            Page(
                id="46d97ed3d9ca4ddabc3c413f306df03a",
                page_no=4,
                content="རྒྱ་གར་1གྱི་\nབསྡུར་མཆན།\n༢༦༤ ༧པེ་〉〉་\nབཞུགས་གོ།",
                name="Page 4",
                vol="1",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460004.jpg/full/max/0/default.jpg",
                note_ref=["46d97ed3d9ca4ddabc3c413f306df03a"],
            ),
            Page(
                id="c11d8db649854c5d89ca3df22047d07b",
                page_no=1,
                content="་་༄ལོ། །རྒྱ་གར་སྐད་དུ།\nདབྱིངས་སུ་བསྟོད་པ།\nའཚལ་ལོ། །གང་ཞིག་",
                name="Page 1",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470001.jpg/full/max/0/default.jpg",
                note_ref=[
                    "05d117045b0c4ea5aee3aeba558e94bd",
                    "05d117045b0c4ea5aee3aeba558e94bd",
                ],
            ),
            Page(
                id="21671cb910d9486c8ba4793305c00d58",
                page_no=2,
                content="མཐོང་ངོ་། །ཕྱོགས་\nདེ་དང་དེ་ཡི་ཕྱོགས་\nཏིང་འཛིན་རྡོ་རྗེ་ཡིས",
                name="Page 2",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470002.jpg/full/max/0/default.jpg",
                note_ref=[
                    "05d117045b0c4ea5aee3aeba558e94bd",
                    "05d117045b0c4ea5aee3aeba558e94bd",
                ],
            ),
            Page(
                id="671dc26715434318b3d641521d4e9292",
                page_no=3,
                content="རིམ་གྱིས་སྦྱངས་\nམེད་ཉི་མ་ཟླ་བ་ཡང་།\n་རྡུལ་kལ་སོགས།",
                name="Page 3",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470003.jpg/full/max/0/default.jpg",
                note_ref=[
                    "05d117045b0c4ea5aee3aeba558e94bd",
                    "05d117045b0c4ea5aee3aeba558e94bd",
                ],
            ),
            Page(
                id="05d117045b0c4ea5aee3aeba558e94bd",
                page_no=4,
                content="འབྱོར་ཆེན་པོ་3དེར་\nབསྡུར་མཆན།\nསྡུག་བསྔལ་གྱིས་\nདེ་ཡི་སྐུ་ལས་",
                name="Page 4",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470004.jpg/full/max/0/default.jpg",
                note_ref=["05d117045b0c4ea5aee3aeba558e94bd"],
            ),
        ],
        notes=[
            NotesPage(
                id="46d97ed3d9ca4ddabc3c413f306df03a",
                page_no=4,
                content="རྒྱ་གར་གྱི་\nབསྡུར་མཆན།\n༢༦༤ ༧པེ་〉〉་\nབཞུགས་གོ།",
                name="Page 4",
                vol="1",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460004.jpg/full/max/0/default.jpg",
            ),
            NotesPage(
                id="05d117045b0c4ea5aee3aeba558e94bd",
                page_no=4,
                content="འབྱོར་ཆེན་པོ་དེར་\nབསྡུར་མཆན།\nསྡུག་བསྔལ་གྱིས་\nདེ་ཡི་སྐུ་ལས་",
                name="Page 4",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470004.jpg/full/max/0/default.jpg",
            ),
        ],
    )


def test_update_base():
    pecha_opf_path = Path(__file__).parent / "data" / "old_opf"
    pecha_id = "P000002"
    text_obj = get_dummy_text()
    text_obj = remove_last_pages(text_obj)
    pecha_idx = from_yaml((pecha_opf_path / f"{pecha_id}.opf" / "index.yml"))
    text_vol_span = get_text_vol_span(pecha_idx, text_obj.id)
    old_vols = get_old_vol(pecha_opf_path, pecha_id, text_vol_span)
    new_vols = get_new_vol(old_vols, pecha_idx, text_obj)
    expected_vol = (Path(__file__).parent / "data" / "expected_v002.txt").read_text(
        encoding="utf-8"
    )
    assert new_vols["v002"] == expected_vol


def test_update_durchen_layer():
    pecha_opf_path = Path(__file__).parent / "data" / "old_opf"
    pecha_id = "P000002"
    text_obj = get_dummy_text()
    text_obj = remove_last_pages(text_obj)
    durchen_path = (
        pecha_opf_path / f"{pecha_id}.opf" / "layers" / "v002" / "Durchen.yml"
    )
    old_durchen_layer = from_yaml(durchen_path)
    update_durchen_layer(text_obj, pecha_id, pecha_opf_path)
    new_durchen_layer = from_yaml(durchen_path)
    expected_durchen_layer = from_yaml(
        (Path(__file__).parent / "data" / "expected_layers" / "Durchen.yml")
    )
    assert expected_durchen_layer == new_durchen_layer
    dump_yaml(old_durchen_layer, durchen_path)


def test_update_pagination_layer():
    pecha_opf_path = Path(__file__).parent / "data" / "old_opf"
    pecha_id = "P000002"
    text_obj = get_dummy_text()
    text_obj = remove_last_pages(text_obj)
    pagination_path = (
        pecha_opf_path / f"{pecha_id}.opf" / "layers" / "v002" / "Pagination.yml"
    )
    old_pagination_layer = from_yaml(pagination_path)
    update_page_layer(text_obj, pecha_id, pecha_opf_path)
    new_pagination_layer = from_yaml(pagination_path)
    expected_pagination_layer = from_yaml(
        (Path(__file__).parent / "data" / "expected_layers" / "Pagination.yml")
    )
    assert expected_pagination_layer == new_pagination_layer
    dump_yaml(old_pagination_layer, pagination_path)


def test_update_index():
    pecha_opf_path = Path(__file__).parent / "data" / "old_opf"
    pecha_id = "P000002"
    text_obj = get_dummy_text()
    text_obj = remove_last_pages(text_obj)
    pecha_idx = from_yaml((pecha_opf_path / f"{pecha_id}.opf" / "index.yml"))
    new_pecha_idx = update_index(pecha_opf_path, pecha_id, text_obj, pecha_idx)
    new_pecha_idx = to_yaml(new_pecha_idx)
    expected_idx = (Path(__file__).parent / "data" / "expected_index.yml").read_text(
        encoding="utf-8"
    )
    assert new_pecha_idx == expected_idx


def test_save_pedurma_text():
    os.system("cp -r ./tests/save_text/data/P0003 ./tests/save_text/data/P0003_namsel")
    os.system("cp -r ./tests/save_text/data/P0003 ./tests/save_text/data/P0003_google")
    text_id = "D1118"
    pecha_id = "P0003"
    namsel_pecha_path = "./tests/save_text/data/P0003_namsel"
    google_pecha_path = "./tests/save_text/data/P0003_google"
    namsel_text_obj = get_text_obj(pecha_id, text_id, namsel_pecha_path)
    namsel_text_obj.pages[
        0
    ].content = "༄ཚོ། །རྒྱ་གར་སྐད་དུ།\nསྟ་བ་ནཱ་མ། བོད་སྐད་དུ།\nཔར་འོས་པ་བསྔགས་"
    google_text_obj = get_text_obj(pecha_id, text_id, google_pecha_path)
    google_text_obj.pages[
        -2
    ].content = "རིམ་གྱིས་སྦྱངས་\nམེད་ཉི་མ་ཟླ་བ་ཡང་།\n་རྡུལ་llལ་སོགས།"
    pedurma_text_mapping = {
        "namsel": {
            "pecha_id": pecha_id,
            "text_obj": namsel_text_obj,
            "pecha_path": namsel_pecha_path,
        },
        "google": {
            "pecha_id": pecha_id,
            "text_obj": google_text_obj,
            "pecha_path": google_pecha_path,
        },
    }
    save_pedurma_text(pedurma_text_obj=None, pedurma_text_mapping=pedurma_text_mapping)
    new_namsel_text_obj = get_text_obj(pecha_id, text_id, namsel_pecha_path)
    new_google_text_obj = get_text_obj(pecha_id, text_id, google_pecha_path)
    assert new_google_text_obj == google_text_obj
    assert new_namsel_text_obj == namsel_text_obj
    os.system("rm -r ./tests/save_text/data/P0003_namsel")
    os.system("rm -r ./tests/save_text/data/P0003_google")
