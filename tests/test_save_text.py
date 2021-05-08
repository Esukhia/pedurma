from pathlib import Path

from pedurma.texts import get_text_obj
from pedurma.save_text import *



def test_update_base():
    pecha_opf_path = Path('./tests/data/save_text/old_opf')
    pecha_id = "P000002"
    text_id = "D1116"
    text_obj = Text(
        id="cf52cbae1a7640b688b24135fe566920",
        vol_span=['v002'],
        pages=[
            Page(
                id="3373e79434004aaeb8b2e69649243d2a",
                page_no=5,
                content="\nངོས་ལྗོན་ཤིང་\nལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པའོ།\nའདི་དག་གིས་ནི་སྦྱིན་པར་\n",
                name="Page 5",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470005.jpg/full/max/0/default.jpg",
                note_ref="9efa117a2b9444ac8cb09c198d21cdd8",
            ),
            Page(
                id="71dff610d4c841c58e9c815582bf8508",
                page_no=6,
                content="\nམངའ་དབང་མཛད་པ་\nའདི་དག་གིས་ནི་དེའི་\nགིས་ནི་སྐྱེ་kkབ་ལ་\n",
                name="Page 6",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470006.jpg/full/max/0/default.jpg",
                note_ref="9efa117a2b9444ac8cb09c198d21cdd8",
            ),
        ],
        notes=[
            NotesPage(
                id="9efa117a2b9444ac8cb09c198d21cdd8",
                page_no=7,
                content="\nདེ་ལ་ནམ་མཁའི་\nབ་ཡང་དག་པར་\nགིས་ནི་ཆོས་སྟོན་པའི་",
                name="Page 7",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470007.jpg/full/max/0/default.jpg",
            )
        ],
    )
    pecha_idx = yaml.safe_load((pecha_opf_path / f"{pecha_id}.opf/index.yml").read_text(encoding='utf-8'))
    old_vols = get_old_vol(pecha_opf_path, pecha_id, text_obj)
    new_vols = get_new_vol(old_vols, pecha_idx, text_obj)
    expected_vol = Path('./tests/data/save_text/expected_v002.txt').read_text(encoding='utf-8')
    assert new_vols['v002'] == expected_vol

def test_update_layers():
    pecha_opf_path = Path('./tests/data/save_text/old_opf/')
    pecha_id = "P000002"
    text_id = "D1116"
    text_obj = Text(
        id="cf52cbae1a7640b688b24135fe566920",
        vol_span=['v002'],
        pages=[
            Page(
                id="3373e79434004aaeb8b2e69649243d2a",
                page_no=5,
                content="\nངོས་ལྗོན་ཤིང་\nལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པའོ།\nའདི་དག་གིས་ནི་སྦྱིན་པར་\n",
                name="Page 5",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470005.jpg/full/max/0/default.jpg",
                note_ref="9efa117a2b9444ac8cb09c198d21cdd8",
            ),
            Page(
                id="71dff610d4c841c58e9c815582bf8508",
                page_no=6,
                content="\nམངའ་དབང་མཛད་པ་\nའདི་དག་གིས་ནི་དེའི་\nགིས་ནི་སྐྱེ་kkབ་ལ་\n",
                name="Page 6",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470006.jpg/full/max/0/default.jpg",
                note_ref="9efa117a2b9444ac8cb09c198d21cdd8",
            ),
        ],
        notes=[
            NotesPage(
                id="9efa117a2b9444ac8cb09c198d21cdd8",
                page_no=7,
                content="\nདེ་ལ་ནམ་མཁའི་\nབ་ཡང་དག་པར་\nགིས་ནི་ཆོས་སྟོན་པའི་",
                name="Page 7",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470007.jpg/full/max/0/default.jpg",
            )
        ],
    )
    pecha_idx = yaml.safe_load((pecha_opf_path / f"{pecha_id}.opf/index.yml").read_text(encoding='utf-8'))
    old_vols = get_old_vol(pecha_opf_path, pecha_id, text_obj)
    new_vols = get_new_vol(old_vols, pecha_idx, text_obj)
    for (vol_id, old_vol_base), (_, new_vol_base) in zip(old_vols.items(), new_vols.items()):
        updater = Blupdate(old_vol_base, new_vol_base)
        old_layers = get_old_layers(pecha_opf_path, pecha_id, vol_id)
        for layer_name, old_layer in old_layers.items():
            update_ann_layer(old_layer, updater)
            new_layer = yaml.safe_dump(old_layer, sort_keys=False)
            expected_layer = Path(f'./tests/data/save_text/expected_layers/{layer_name}.yml').read_text(encoding='utf-8')
            assert new_layer == expected_layer
    