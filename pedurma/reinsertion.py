import re


def construct_notes(note_id, note):
    combined_notes = f'<({note_id})'
    for pub, note_value in note.items():
        if note_value:
            combined_notes += f"{pub}{note_value},"
    combined_notes += '>'
    return combined_notes


def reinsert_pedurma_notes(pg, notes):
    new_pg = pg
    for note_id, note in notes.items():
        combined_note = construct_notes(note_id, note)
        new_pg = re.sub('#', combined_note, new_pg, 1)
    return new_pg

def get_preview_pg(pg_with_note):
    pg_content = pg_with_note.content
    notes = pg_with_note.notes
    preview_pg = reinsert_pedurma_notes(pg_content, notes)
    return preview_pg

