from pathlib import Path

from pedurma.pecha import NotesPage, Page, Text
from pedurma.texts import get_pedurma_text_obj, get_text_obj
from pedurma.utils import from_editor, to_editor


def test_text_obj_serializer_corssvol():
    text_id = "D1115"
    pecha_id = "P000002"
    opf_path = str(Path(__file__).parent / "data" / pecha_id)
    text_obj = get_text_obj(pecha_id, text_id, pecha_path=opf_path, bdrc_img=False)
    expected_text_obj = Text(
        id="259260e8e3544fc1a9a27d7dffc72df6",
        pages=[
            Page(
                id="1a26fd08bf2b4ebb9e2d7369347e478b",
                page_no=10,
                content="ཉ༄ཚོ། །རྒྱ་གར་སྐད་དུ།\nསྟ་བ་ནཱ་མ། བོད་སྐད་དུ།\nཔར་འོས་པ་བསྔགས་\n1-10",
                name="Page 1",
                vol="1",
                base_name="v001",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460001.jpg/full/max/0/default.jpg",
                note_ref=["46d97ed3d9ca4ddabc3c413f306df03a"],
            ),
            Page(
                id="e8e314a7457b40348b5dd7a744004900",
                page_no=0,
                content="གཏམ་འདི་ཙམ\nའདི་ཉིད་སྨྲ་བར་\nདང་-། །ཁྱོད་མ\n1-11",
                name="Page 2",
                vol="1",
                base_name="v001",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460002.jpg/full/max/0/default.jpg",
                note_ref=["46d97ed3d9ca4ddabc3c413f306df03a"],
            ),
            Page(
                id="29c64dc1fa624b42b08814ca4f3a78b4",
                page_no=0,
                content="འདོད་གང་དག་\nསྐྱབས་འགྲོ་བ།\nསྟོང་གིས་ཀྱང་།\n1-12",
                name="Page 3",
                vol="1",
                base_name="v001",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460003.jpg/full/max/0/default.jpg",
                note_ref=["46d97ed3d9ca4ddabc3c413f306df03a"],
            ),
            Page(
                id="46d97ed3d9ca4ddabc3c413f306df03a",
                page_no=13,
                content="རྒྱ་གར་གྱི་\n༢༦༤ ༧པེ་〉〉་\nབཞུགས་གོ།",
                name="Page 4",
                vol="1",
                base_name="v001",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460004.jpg/full/max/0/default.jpg",
                note_ref=["46d97ed3d9ca4ddabc3c413f306df03a", "--"],
            ),
            Page(
                id="c11d8db649854c5d89ca3df22047d07b",
                page_no=10,
                content="་་༄ལོ། །རྒྱ་གར་སྐད་དུ།\nདབྱིངས་སུ་བསྟོད་པ།\nའཚལ་ལོ། །གང་ཞིག་\n1-10",
                name="Page 1",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470001.jpg/full/max/0/default.jpg",
                note_ref=["05d117045b0c4ea5aee3aeba558e94bd"],
            ),
            Page(
                id="21671cb910d9486c8ba4793305c00d58",
                page_no=0,
                content="མཐོང་ངོ་། །ཕྱོགས་\nདེ་དང་དེ་ཡི་ཕྱོགས་\nཏིང་འཛིན་རྡོ་རྗེ་ཡིས\n1-11",
                name="Page 2",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470002.jpg/full/max/0/default.jpg",
                note_ref=["05d117045b0c4ea5aee3aeba558e94bd"],
            ),
            Page(
                id="671dc26715434318b3d641521d4e9292",
                page_no=0,
                content="རིམ་གྱིས་སྦྱངས་\nམེད་ཉི་མ་ཟླ་བ་ཡང་།\n་རྡུལ་ལ་སོགས།\n1-12",
                name="Page 3",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470003.jpg/full/max/0/default.jpg",
                note_ref=["05d117045b0c4ea5aee3aeba558e94bd"],
            ),
            Page(
                id="05d117045b0c4ea5aee3aeba558e94bd",
                page_no=13,
                content="འབྱོར་ཆེན་པོ་དེར་\nསྡུག་བསྔལ་གྱིས་\nདེ་ཡི་སྐུ་ལས་",
                name="Page 4",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470004.jpg/full/max/0/default.jpg",
                note_ref=["05d117045b0c4ea5aee3aeba558e94bd", "--"],
            ),
        ],
        notes=[
            NotesPage(
                id="46d97ed3d9ca4ddabc3c413f306df03a",
                page_no=0,
                content="རྒྱ་གར་གྱི་\n      (༢༦༤) ༧པེ་〉〉་\nབཞུགས་གོ།",
                name="Page 4",
                vol="1",
                base_name="v001",
                image_link="https://iiif.bdrc.io/bdr:I1PD95846::I1PD958460004.jpg/full/max/0/default.jpg",
            ),
            NotesPage(
                id="05d117045b0c4ea5aee3aeba558e94bd",
                page_no=0,
                content="འབྱོར་ཆེན་པོ་དེར་\nསྡུག་བསྔལ་གྱིས་\nདེ་ཡི་སྐུ་ལས་",
                name="Page 4",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470004.jpg/full/max/0/default.jpg",
            ),
        ],
    )
    assert text_obj == expected_text_obj


def test_text_obj_serializer():
    text_id = "D1116"
    pecha_id = "P000002"
    opf_path = Path(__file__).parent / "data" / pecha_id
    text_obj = get_text_obj(pecha_id, text_id, pecha_path=opf_path, bdrc_img=False)
    expected_text_obj = Text(
        id="cf52cbae1a7640b688b24135fe566920",
        pages=[
            Page(
                id="3373e79434004aaeb8b2e69649243d2a",
                page_no=14,
                content="ངོས་ལྗོན་ཤིང་\nལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པའོ།\nའདི་དག་གིས་ནི་སྦྱིན་པར་\n1-14",
                name="Page 5",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470005.jpg/full/max/0/default.jpg",
                note_ref=["9efa117a2b9444ac8cb09c198d21cdd8"],
            ),
            Page(
                id="71dff610d4c841c58e9c815582bf8508",
                page_no=0,
                content="མངའ་དབང་མཛད་པ་\nའདི་དག་གིས་ནི་དེའི་\nགིས་ནི་སྐྱེ་བ་ལ་\n1-15",
                name="Page 6",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470006.jpg/full/max/0/default.jpg",
                note_ref=["9efa117a2b9444ac8cb09c198d21cdd8"],
            ),
            Page(
                id="9efa117a2b9444ac8cb09c198d21cdd8",
                page_no=16,
                content="དེ་ལ་ནམ་མཁའི་\nབ་ཡང་དག་པར་\nགིས་ནི་ཆོས་སྟོན་པའི་",
                name="Page 7",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470007.jpg/full/max/0/default.jpg",
                note_ref=["9efa117a2b9444ac8cb09c198d21cdd8", "--"],
            ),
        ],
        notes=[
            NotesPage(
                id="9efa117a2b9444ac8cb09c198d21cdd8",
                page_no=0,
                content="དེ་ལ་ནམ་མཁའི་\nབ་ཡང་དག་པར་\nགིས་ནི་ཆོས་སྟོན་པའི་",
                name="Page 7",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470007.jpg/full/max/0/default.jpg",
            )
        ],
    )
    assert text_obj == expected_text_obj


def test_pedurma_text_obj():
    pecha_id = "P000002"
    dg_pecha_path = Path(__file__).parent / "data" / pecha_id
    namsel_pecha_path = Path(__file__).parent / "data" / pecha_id
    text_id = "D1116"
    pecha_paths = {"namsel": namsel_pecha_path, "google": dg_pecha_path}
    expected_namsel_text_obj = Text(
        id="cf52cbae1a7640b688b24135fe566920",
        pages=[
            Page(
                id="3373e79434004aaeb8b2e69649243d2a",
                page_no=14,
                content="ངོས་ལྗོན་ཤིང་\nལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པའོ།\nའདི་དག་གིས་ནི་སྦྱིན་པར་\n1-14",
                name="Page 5",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470005.jpg/full/max/0/default.jpg",
                note_ref=["9efa117a2b9444ac8cb09c198d21cdd8"],
            ),
            Page(
                id="71dff610d4c841c58e9c815582bf8508",
                page_no=0,
                content="མངའ་དབང་མཛད་པ་\nའདི་དག་གིས་ནི་དེའི་\nགིས་ནི་སྐྱེ་བ་ལ་\n1-15",
                name="Page 6",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470006.jpg/full/max/0/default.jpg",
                note_ref=["9efa117a2b9444ac8cb09c198d21cdd8"],
            ),
            Page(
                id="9efa117a2b9444ac8cb09c198d21cdd8",
                page_no=16,
                content="དེ་ལ་ནམ་མཁའི་\nབ་ཡང་དག་པར་\nགིས་ནི་ཆོས་སྟོན་པའི་",
                name="Page 7",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470007.jpg/full/max/0/default.jpg",
                note_ref=["9efa117a2b9444ac8cb09c198d21cdd8", "--"],
            ),
        ],
        notes=[
            NotesPage(
                id="9efa117a2b9444ac8cb09c198d21cdd8",
                page_no=0,
                content="དེ་ལ་ནམ་མཁའི་\nབ་ཡང་དག་པར་\nགིས་ནི་ཆོས་སྟོན་པའི་",
                name="Page 7",
                vol="2",
                base_name="v002",
                image_link="https://iiif.bdrc.io/bdr:I1PD95847::I1PD958470007.jpg/full/max/0/default.jpg",
            )
        ],
    )
    pedurma_text = get_pedurma_text_obj(text_id, pecha_paths, bdrc_img=False)
    assert pedurma_text.namsel == expected_namsel_text_obj


def test_note_to_editor_view():
    namsel_note = (Path(__file__).parent / "data" / "namsel_note.txt").read_text(
        encoding="utf-8"
    )
    google_note = (Path(__file__).parent / "data" / "google_note.txt").read_text(
        encoding="utf-8"
    )
    namsel_editor_view = to_editor(namsel_note)
    google_editor_view = to_editor(google_note)
    original_namsel_note = from_editor(namsel_editor_view, "namsel")
    original_google_note = from_editor(google_editor_view, "google")
    assert namsel_note == original_namsel_note
    assert google_note == original_google_note
