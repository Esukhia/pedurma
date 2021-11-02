import re
from pathlib import Path

from openpecha.utils import download_pecha

from pedurma.pecha import PedurmaNoteEdit
from pedurma.preprocess import preprocess_namsel_notes
from pedurma.texts import get_durchen, get_hfml_text, get_link, get_vol_meta
from pedurma.utils import from_yaml


def get_meta_data(text_uuid, meta_data):
    try:
        meta = {
            "work_id": meta_data["work_id"],
            "img_grp_offset": meta_data["img_grp_offset"],
            "pref": meta_data["pref"],
            "text_uuid": text_uuid,
        }
    except Exception:
        meta = {}
    return meta


def get_durchen_pages(vol_text):
    durchen_pages = {}
    pages = re.split(r"(〔[𰵀-󴉱]?\d+〕)", vol_text)
    pg_ann = ""
    for i, page in enumerate(pages[1:]):
        if i % 2 == 0:
            pg_ann = page
        else:
            durchen_pages[pg_ann] = page
    return durchen_pages


def get_page_num(page_ann):
    pg_pat = re.search(r"(\d+)", page_ann)
    if pg_pat:
        pg_num = pg_pat.group(1)
    else:
        pg_num = None
    return pg_num


def rm_annotations(text, annotations):
    clean_text = text
    for ann in annotations:
        clean_text = re.sub(ann, "", clean_text)
    return clean_text


def get_num(line):
    tib_num = re.sub(r"\W", "", line)
    tib_num = re.sub(r"(\d+?)r", "", tib_num)
    table = tib_num.maketrans("༡༢༣༤༥༦༧༨༩༠", "1234567890", "<r>")
    eng_num = int(tib_num.translate(table))
    return eng_num


def get_durchen_pg_num(clean_page):
    pg_num = 0
    try:
        page_ann = re.findall(r"<p\d+-(\d+)\>", clean_page)
        pg_num = page_ann[-1]
    except Exception:
        pass
    return pg_num


def get_page_refs(page_content):
    refs = re.findall(r"<r.+?>", page_content)
    if refs:
        if len(refs) > 2:
            refs[0] = get_num(refs[0])
            refs[-1] = get_num(refs[-1])
            return (refs[0], refs[-1])
        else:
            refs[0] = get_num(refs[0])
            return (refs[0], "0")
    else:
        return ("0", "0")


def process_page(page_ann, page_content, vol_meta):
    durchen_image_num = get_page_num(page_ann)
    pg_link = get_link(durchen_image_num, vol_meta)
    unwanted_annotations = [
        r"〔[𰵀-󴉱]?\d+〕",
        r"\[\w+\.\d+\]",
        r"<d",
        r"d>",
    ]
    page_content = rm_annotations(page_content, unwanted_annotations)
    durchen_pg_num = get_durchen_pg_num(page_content)
    pg_ref_first, pg_ref_last = get_page_refs(page_content)
    page_obj = PedurmaNoteEdit(
        image_link=pg_link,
        image_no=durchen_image_num,
        page_no=durchen_pg_num,
        ref_start_page_no=pg_ref_first,
        ref_end_page_no=pg_ref_last,
        vol=vol_meta["volume_number"],
    )
    return page_obj


def get_pages_to_edit(durchen_pages, vol_meta):
    pages_to_edit = []
    for page_ann, page_content in durchen_pages.items():
        pages_to_edit.append(process_page(page_ann, page_content, vol_meta))
    return pages_to_edit


def get_pedurma_edit_notes(hfml_text, text_meta):
    pedurma_edit_notes = []
    for vol, text_content in hfml_text.items():
        vol_meta = get_vol_meta(vol, text_meta)
        durchen = get_durchen(text_content)
        durchen_pages = get_durchen_pages(durchen)
        pedurma_edit_notes += get_pages_to_edit(durchen_pages, vol_meta)
    return pedurma_edit_notes


def get_pedurma_text_edit_notes(pecha_id):
    pecha_path = download_pecha(pecha_id, needs_update=False)
    meta_data = from_yaml(Path(f"{pecha_path}/{pecha_id}.opf/meta.yml"))
    hfmls = get_hfml_text(pecha_path, pecha_id)
    pedurma_edit_notes = get_pedurma_edit_notes(hfmls, meta_data)
    return pedurma_edit_notes
