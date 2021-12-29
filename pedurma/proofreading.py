from pedurma.pecha import ProofreadNotePage
from pedurma.utils import from_yaml


def get_first_page_num(text_id, repo_path):
    google_note_page_paths = list((repo_path / "google_notes" / text_id).iterdir())
    google_note_page_paths.sort()
    first_pg_num = int(google_note_page_paths[0].stem)
    return first_pg_num


def get_note_page_img_link(text_id, pg_num, repo_path):
    text_meta = from_yaml((repo_path / "google_notes" / text_id / "meta.yml"))
    image_grp_id = text_meta.get("img_grp_id", "")
    img_link = f"https://iiif.bdrc.io/bdr:{image_grp_id}::{image_grp_id}{int(pg_num):04}.jpg/full/max/0/default.jpg"
    return img_link


def get_note_page(text_id, prev_pg_num=None, repo_path=None):
    if prev_pg_num:
        cur_pg_num = prev_pg_num + 1
    else:
        cur_pg_num = get_first_page_num(text_id, repo_path)
    manual_note = (
        repo_path / "manual_notes" / text_id / f"{cur_pg_num}.txt"
    ).read_text(encoding="utf-8")
    google_note = (
        repo_path / "google_notes" / text_id / f"{cur_pg_num}.txt"
    ).read_text(encoding="utf-8")
    img_link = get_note_page_img_link(text_id, cur_pg_num, repo_path)

    page = ProofreadNotePage(
        manual=manual_note, google=google_note, img_link=img_link, page_num=cur_pg_num
    )
    return page


def update_note_page(text_id, page: ProofreadNotePage, repo_path=None):
    new_manual_note_page = page.manual
    cur_pg_num = page.page_num
    (repo_path / "manual_notes" / text_id / f"{cur_pg_num}.txt").write_text(
        new_manual_note_page, encoding="utf-8"
    )
    print(f"INFO: {cur_pg_num} updated")
