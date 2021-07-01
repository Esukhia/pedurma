from pathlib import Path

from pedurma.pecha import *
from pedurma.texts import get_text_info, construct_text_obj, get_meta_data
from pedurma.utils import from_yaml

def test_text_obj_serializer_corssvol():
    text_id = "D1115"
    pecha_id = "P000002"
    opf_path = f"./tests/data/{pecha_id}/"
    index = from_yaml(Path(f"{opf_path}/{pecha_id}.opf/index.yml"))
    meta_data = from_yaml(Path(f'{opf_path}/{pecha_id}.opf/meta.yml'))
    text_uuid, text_info = get_text_info(text_id, index)
    text_meta = get_meta_data(pecha_id, text_uuid, meta_data)
    hfmls = from_yaml(Path(f"./tests/data/hfmls/{text_id}.yml"))
    text_obj = construct_text_obj(hfmls, text_meta, opf_path)
    expected_text_obj = Text(
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
                content="\nརིམ་གྱིས་སྦྱངས་\nམེད་ཉི་མ་ཟླ་བ་ཡང་།\n་རྡུལ་ལ་སོགས།\n",
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
                content="\nརྒྱ་གར་གྱི་\n༢༦༤ ༧པེ་〉〉་\nབཞུགས་གོ།\n",
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
    assert text_obj == expected_text_obj


def test_text_obj_serializer():
    text_id = "D1116"
    pecha_id = "P000002"
    opf_path = f"./tests/data/{pecha_id}/"
    index = from_yaml(Path(f"{opf_path}/{pecha_id}.opf/index.yml"))
    meta_data = from_yaml(Path(f'{opf_path}/{pecha_id}.opf/meta.yml'))
    text_uuid, text_info = get_text_info(text_id, index)
    text_meta = get_meta_data(pecha_id, text_uuid, meta_data)
    hfmls = from_yaml(Path(f"./tests/data/hfmls/{text_id}.yml"))
    text_obj = construct_text_obj(hfmls, text_meta, opf_path)
    expected_text_obj = Text(
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
                content="\nམངའ་དབང་མཛད་པ་\nའདི་དག་གིས་ནི་དེའི་\nགིས་ནི་སྐྱེ་བ་ལ་\n",
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
                content="\nདེ་ལ་ནམ་མཁའི་\nབ་ཡང་དག་པར་\nགིས་ནི་ཆོས་སྟོན་པའི་\n",
                name="Page 7",
                vol="2",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470007.jpg/full/max/0/default.jpg",
            )
        ],
    )
    assert text_obj == expected_text_obj
