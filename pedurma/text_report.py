import re
from datetime import datetime

from openpecha.core.pecha import OpenPechaFS


def get_text_title(pecha_path):
    text_title = ""
    opf = OpenPechaFS(pecha_path)
    opf_meta = opf.read_meta_file()
    text_source_metadata = opf_meta.get("source_metadata", {})
    if text_source_metadata:
        text_title = text_source_metadata.get("title", "")
    return text_title


def get_number_of_pages(vol_text):
    pg_anns = re.findall(r"\d+-\d+", vol_text)
    return len(pg_anns)


def get_number_of_footnotes(vol_text):
    footnotes_annotations = re.findall("<.+?>", vol_text)
    return len(footnotes_annotations)


def get_text_report(text_id, pecha_paths, preview_text):
    text_report = {
        "toh_no": text_id,
        "title": None,
        "total_number_of_pages": None,
        "total_number_of_footnotes": None,
        "download_date": None,
    }
    text_report["title"] = get_text_title(pecha_paths["google"])
    number_of_pages = 0
    number_of_footnotes = 0
    for vol_num, vol_text in preview_text.items():
        number_of_pages += get_number_of_pages(vol_text)
        number_of_footnotes += get_number_of_footnotes(vol_text)
    text_report["total_number_of_pages"] = number_of_pages
    text_report["total_number_of_footnotes"] = number_of_footnotes
    text_report["download_date"] = datetime.now()
    return text_report
