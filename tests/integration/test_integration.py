from json import detect_encoding
from pedurma.texts import get_derge_google_text_obj, get_text_obj, serialize_text_obj
from pedurma import *



if __name__ == "__main__":
    text_id = "D1119"
    dg_text = get_derge_google_text_obj(text_id)