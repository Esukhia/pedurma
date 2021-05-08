from openpecha.blupdate import *
from pedurma.pecha import *
from pedurma.texts import serialize_text_obj

def get_old_vol(pecha_opf_path, pecha_id, text_obj):
    old_vols = {}
    for vol_id in text_obj.vol_span:
        old_vols[vol_id] = (pecha_opf_path / f"{pecha_id}.opf/base/{vol_id}.txt").read_text(encoding='utf-8')
    return old_vols

def get_old_text_base(pecha_idx, old_vol_base, text_id, text_vol_num):
    text_span = pecha_idx['annotations'][text_id]['span']
    for vol_span in text_span:
        if vol_span['vol'] == text_vol_num:
            return old_vol_base[vol_span['start']:vol_span['end']]
    return ''

def get_new_vol(old_vols, pecha_idx, text_obj):
    new_vols = {}
    new_text = serialize_text_obj(text_obj)
    for vol_id, new_text_base in new_text.items():
        vol_num = int(vol_id[1:])
        old_vol_base = old_vols[vol_id]
        old_text_base = get_old_text_base(pecha_idx, old_vol_base, text_obj.id, vol_num)
        if new_text_base[0] == "\n":
            new_text_base = new_text_base[1:]
        new_vol_base = old_vol_base.replace(old_text_base, new_text_base)
        new_vols[vol_id] = new_vol_base
    return new_vols

def update_base(pecha_opf_path, pecha_id, text_obj, pecha_idx = None):
    if not pecha_idx:
        pecha_idx = yaml.safe_load((pecha_opf_path / f"{pecha_id}.opf/index.yml").read_text(encoding='utf-8'))
    old_vols = get_old_vol(pecha_opf_path, pecha_id, text_obj)
    new_vols = get_new_vol(old_vols, pecha_idx, text_obj)
    for vol_id, new_vol_base in new_vols.items():
        (pecha_opf_path / f"{pecha_id}.opf/base/{vol_id}.txt").write_text(new_vol_base, encoding='utf-8')
        print(f'INFO: {vol_id} base updated..')

def get_old_layers(pecha_opf_path, pecha_id, vol_id):
    old_layers = {}
    layer_paths = list((pecha_opf_path / f"{pecha_id}.opf/layers/{vol_id}").iterdir())
    for layer_path in layer_paths:
        layer_name = layer_path.stem
        layer_content = yaml.safe_load(layer_path.read_text(encoding='utf-8'))
        old_layers[layer_name] = layer_content
    return old_layers

def update_layer(pecha_opf_path, pecha_id, vol_id, old_layers, updater):
    for layer_name, old_layer in old_layers.items():
        update_ann_layer(old_layer, updater)
        new_layer = yaml.safe_dump(old_layer, sort_keys=False)
        (pecha_opf_path / f"{pecha_id}.opf/layers/{vol_id}/{layer_name}.yml").write_text(new_layer, encoding='utf-8')
        print(f'INFO: {vol_id} {layer_name} has been updated...')
    
def update_old_layers(pecha_opf_path, pecha_id, text_obj, pecha_idx = None):
    if not pecha_idx:
        pecha_idx = yaml.safe_load((pecha_opf_path / f"{pecha_id}.opf/index.yml").read_text(encoding='utf-8'))
    old_vols = get_old_vol(pecha_opf_path, text_obj)
    new_vols = get_new_vol(old_vols, pecha_idx, text_obj)
    for (vol_id, old_vol_base), (_, new_vol_base) in zip(old_vols.items(), new_vols.items()):
        updater = Blupdate(old_vol_base, new_vol_base)
        old_layers = get_old_layers(pecha_opf_path, pecha_id, vol_id)
        update_layer(pecha_opf_path, pecha_id, vol_id, old_layers, updater)

