#!/usr/bin/env python3
"""Construye la tienda Eclipse Perfums autónoma a partir del catálogo Olfatorio.
Uso: python3 build.py   (lee products.json y ../olfatorio/*)"""
import json, os, re, shutil, pathlib
HERE=pathlib.Path(__file__).parent; SRC=HERE.parent/'olfatorio'
shop=json.load(open(HERE/'products.json'))
data={p['id']:p for p in json.load(open(SRC/'data.json'))}
notemap=json.load(open(SRC/'notemap.json')); meta=json.load(open(SRC/'meta.json'))
ids=[s['id'] for s in shop if s['id'] in data]
# perfumes necesarios: los vendidos + los originales a los que se parecen (solo nombre)
sub={}
for i in ids:
    p=dict(data[i]); sub[i]=p
    m=meta.get(i,{})
    if m.get('inspired') and m['inspired'] in data:
        o=data[m['inspired']]; sub.setdefault(o['id'],{'id':o['id'],'name':o['name'],'brand':o['brand'],'notes':{},'accords':[],'desc':''})
for d in ('img','notes'): (HERE/d).mkdir(exist_ok=True)
for i in ids:
    src=SRC/('img/'+i+'.jpg') if i.startswith('lm-') else SRC/('imgx/'+i+'.avif')
    dst=HERE/'img'/(i+('.jpg' if i.startswith('lm-') else '.avif')); shutil.copy(src,dst)
    for k,L in data[i]['notes'].items():
        for n in L:
            nid=notemap.get(n)
            if nid and (SRC/'notes'/(nid+'.jpg')).exists(): shutil.copy(SRC/'notes'/(nid+'.jpg'), HERE/'notes'/(nid+'.jpg'))
used_notes={n:notemap[n] for i in ids for L in data[i]['notes'].values() for n in L if n in notemap}
sub_meta={i:meta.get(i,{}) for i in ids}
blob="const DATA="+json.dumps(list(sub.values()),ensure_ascii=False)+";\nconst NOTE_IMG="+json.dumps(used_notes,ensure_ascii=False)+";\nconst META="+json.dumps(sub_meta,ensure_ascii=False)+";\nconst SHOP="+json.dumps(shop,ensure_ascii=False)+";\n"
for tpl,out in (('template-luxe.html','index.html'),('template-lookbook.html','claro/index.html'),('template-oscuro.html','oscuro/index.html')):
    s=open(HERE/tpl,encoding='utf-8').read().replace('/*__DATA__*/',blob)
    (HERE/out).parent.mkdir(exist_ok=True); open(HERE/out,'w',encoding='utf-8').write(s)
print('productos:',len(ids),'| iconos de nota:',len(used_notes),'| generado index.html y oscuro/index.html')
