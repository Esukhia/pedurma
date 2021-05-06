from json import detect_encoding
from pedurma.texts import get_derge_google_text_obj, get_text_obj, serialize_text_obj
from pedurma import *



if __name__ == "__main__":
    text_id = "D1119"
    # google_text = get_text_obj("P000791", text_id)
    dg_text = get_derge_google_text_obj(text_id)
    namsel_text = get_text_obj("P000792", text_id)
    preview = get_preview_page(dg_text.pages[0], namsel_text.pages[0], dg_text.notes[0], namsel_text.notes[0])
    # dg_text = get_derge_google_text_obj(text_id)