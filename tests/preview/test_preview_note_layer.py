import re
from pathlib import Path
from pedurma.preview_note_layer import build_note_layer
from pedurma.utils import from_yaml


def get_annotations(note_annotations):
    curr_ann = {}
    final_ann = {}
    for num, (_, note_info) in enumerate(note_annotations.items(), 1):
        curr_ann[num] = note_info
        final_ann.update(curr_ann)
        curr_ann = {}
    return final_ann

def test_preview_note_layer():
    preview_text = Path("./tests/preview/data/D11_preview.txt").read_text(encoding="utf-8")
    expected_note_layer = from_yaml(Path("./tests/preview/data/expected_note_layer.yml"))
    expected_note_annotation = get_annotations(expected_note_layer)
    note_layer = build_note_layer(preview_text)
    note_annotation = get_annotations(note_layer['annotations'])
    assert expected_note_annotation == note_annotation
