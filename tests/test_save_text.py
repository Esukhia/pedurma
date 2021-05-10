import copy
import os
from pathlib import Path

from pedurma.texts import get_text_obj
from pedurma.save_text import *



def test_update_base():
    pecha_opf_path = Path('./tests/data/save_text/old_opf')
    pecha_id = "P000002"
    text_id = "D1116"
    text_obj = Text(
        id="cf52cbae1a7640b688b24135fe566920",
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
    text_vol_span = get_text_vol_span(pecha_idx, text_obj.id)
    old_vols = get_old_vol(pecha_opf_path, pecha_id, text_vol_span)
    new_vols = get_new_vol(old_vols, pecha_idx, text_obj)
    expected_vol = Path('./tests/data/save_text/expected_v002.txt').read_text(encoding='utf-8')
    assert new_vols['v002'] == expected_vol

def test_update_layers():
    pecha_opf_path = Path('./tests/data/save_text/old_opf/')
    pecha_id = "P000002"
    text_id = "D1116"
    text_obj = Text(
        id="cf52cbae1a7640b688b24135fe566920",
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
    text_vol_span = get_text_vol_span(pecha_idx, text_obj.id)
    old_vols = get_old_vol(pecha_opf_path, pecha_id, text_vol_span)
    new_vols = get_new_vol(old_vols, pecha_idx, text_obj)
    for (vol_id, old_vol_base), (_, new_vol_base) in zip(old_vols.items(), new_vols.items()):
        updater = Blupdate(old_vol_base, new_vol_base)
        old_layers = get_old_layers(pecha_opf_path, pecha_id, vol_id)
        for layer_name, old_layer in old_layers.items():
            update_ann_layer(old_layer, updater)
            new_layer = yaml.safe_dump(old_layer, sort_keys=False)
            expected_layer = Path(f'./tests/data/save_text/expected_layers/{layer_name}.yml').read_text(encoding='utf-8')
            assert new_layer == expected_layer

def test_update_index():
    pecha_opf_path = Path('./tests/data/save_text/old_opf/')
    pecha_id = "P000002"
    text_id = "D1116"
    text_obj = Text(
        id="259260e8e3544fc1a9a27d7dffc72df6",
        pages=[
            Page(
                id="1a26fd08bf2b4ebb9e2d7369347e478b",
                page_no=1,
                content="\nཉ༄ཚོ། །རྒྱ་གར་སྐད་དུ།\nསྟ་བ་ནཱ་མ། བོད་སྐད་དུ།\nཔར་འོས་པ་བསྔགས་\n",
                name="Page 1",
                vol="1",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460001.jpg/full/max/0/default.jpg",
                note_ref="46d97ed3d9ca4ddabc3c413f306df03a",
            ),
            Page(
                id="e8e314a7457b40348b5dd7a744004900",
                page_no=2,
                content="\nགཏམ་འདི་ཙམ\nའདི་ཉིད་སྨྲ་བར་\nདང་-། །ཁྱོད་མ\n",
                name="Page 2",
                vol="1",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460002.jpg/full/max/0/default.jpg",
                note_ref="46d97ed3d9ca4ddabc3c413f306df03a",
            ),
            Page(
                id="29c64dc1fa624b42b08814ca4f3a78b4",
                page_no=3,
                content="\nའདོད་གང་དག་\nསྐྱབས་འགྲོ་བ།\nསྟོང་གིས་ཀྱང་།\n",
                name="Page 3",
                vol="1",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460003.jpg/full/max/0/default.jpg",
                note_ref="46d97ed3d9ca4ddabc3c413f306df03a",
            ),
            Page(
                id="c11d8db649854c5d89ca3df22047d07b",
                page_no=1,
                content="\n་་༄ལོ། །རྒྱ་གར་སྐད་དུ།\nདབྱིངས་སུ་བསྟོད་པ།\nའཚལ་ལོ། །གང་ཞིག་\n",
                name="Page 1",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470001.jpg/full/max/0/default.jpg",
                note_ref="05d117045b0c4ea5aee3aeba558e94bd",
            ),
            Page(
                id="21671cb910d9486c8ba4793305c00d58",
                page_no=2,
                content="\nམཐོང་ངོ་། །ཕྱོགས་\nདེ་དང་དེ་ཡི་ཕྱོགས་\nཏིང་འཛིན་རྡོ་རྗེ་ཡིས\n",
                name="Page 2",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470002.jpg/full/max/0/default.jpg",
                note_ref="05d117045b0c4ea5aee3aeba558e94bd",
            ),
            Page(
                id="671dc26715434318b3d641521d4e9292",
                page_no=3,
                content="\nརིམ་གྱིས་སྦྱངས་\nམེད་ཉི་མ་ཟླ་བ་ཡང་།\n་རྡུལ་kལ་སོགས།\n",
                name="Page 3",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470003.jpg/full/max/0/default.jpg",
                note_ref="05d117045b0c4ea5aee3aeba558e94bd",
            ),
        ],
        notes=[
            NotesPage(
                id="46d97ed3d9ca4ddabc3c413f306df03a",
                page_no=4,
                content="\nརྒྱ་གར་གྱི་\n༢༦༤ ༧པེ་〉〉་\nབཞུགས་གོ།",
                name="Page 4",
                vol="1",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460004.jpg/full/max/0/default.jpg",
            ),
            NotesPage(
                id="05d117045b0c4ea5aee3aeba558e94bd",
                page_no=4,
                content="\nའབྱོར་ཆེན་པོ་དེར་\nསྡུག་བསྔལ་གྱིས་\nདེ་ཡི་སྐུ་ལས་\n",
                name="Page 4",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470004.jpg/full/max/0/default.jpg",
            ),
        ],
    )
    pecha_idx = yaml.safe_load((pecha_opf_path / f"{pecha_id}.opf/index.yml").read_text(encoding='utf-8'))
    new_pecha_idx = update_index(pecha_opf_path, pecha_id, text_obj, pecha_idx)
    new_pecha_idx = yaml.safe_dump(new_pecha_idx, sort_keys=False)
    expected_idx = Path('./tests/data/save_text/expected_index.yml').read_text(encoding='utf-8')
    assert new_pecha_idx == expected_idx


def test_integration():
    os.system('cp -r ./tests/data/save_text/P0003 ./tests/data/save_text/P0003_copy')
    pecha_opf_path = Path('./tests/data/save_text/P0003_copy/')
    pecha_id = "P0003"
    text_id = "D1118"
    text_obj = get_text_obj(pecha_id, text_id, pecha_opf_path)
    new_last_page = "\nརིམ་གྱིས་སྦྱངས་\nམེད་ཉི་མ་ཟླ་བ་ཡང་།\n་རྡུལ་kkལ་སོགས།\n"
    text_obj.pages[-1].content = new_last_page
    old_pecha_idx = yaml.safe_load((pecha_opf_path / f'{pecha_id}.opf/index.yml').read_text(encoding='utf-8'))
    prev_pecha_idx = copy.deepcopy(old_pecha_idx)
    new_pecha_idx = update_index(pecha_opf_path, pecha_id, text_obj, old_pecha_idx)
    update_old_layers(pecha_opf_path, pecha_id, text_obj, prev_pecha_idx)
    update_base(pecha_opf_path, pecha_id, text_obj, prev_pecha_idx)
    new_pecha_idx = yaml.safe_dump(new_pecha_idx, sort_keys=False)
    (pecha_opf_path / f'{pecha_id}.opf/index.yml').write_text(new_pecha_idx, encoding='utf-8')
    new_text_obj = get_text_obj(pecha_id, text_id, pecha_opf_path)
    assert new_text_obj == text_obj
    os.system('rm -r ./tests/data/save_text/P0003_copy')