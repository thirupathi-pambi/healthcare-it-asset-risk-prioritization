import csv
from collections import Counter
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]

def score(asset):
    points={'healthy':0,'warning':25,'critical':60}[asset['condition']]
    if asset['type']=='workstation' and asset['os']=='Windows 10':points+=30
    if int(asset['purchase_year'])<=2021:points+=15
    return min(100,points)

def main():
    with (ROOT/'data/assets.csv').open() as f:assets=list(csv.DictReader(f))
    for a in assets:a['risk_score']=score(a);a['priority']='high' if a['risk_score']>=60 else 'medium' if a['risk_score']>=25 else 'low'
    out=ROOT/'output';out.mkdir(exist_ok=True)
    with (out/'asset_priorities.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(assets[0]));w.writeheader();w.writerows(sorted(assets,key=lambda x:-x['risk_score']))
    counter=Counter(a['priority'] for a in assets)
    blocks=''.join(f'<li>{escape(k.title())}: {counter[k]}</li>' for k in ('high','medium','low'))
    (out/'summary.html').write_text(f'<html><head><meta charset="utf-8"><title>Asset health</title></head><body style="font:18px system-ui;margin:50px"><h1>Fictional clinic assets</h1><p>{len(assets)} tracked assets</p><ul>{blocks}</ul><p>Risk model is illustrative and not a security certification.</p></body></html>')
    print('Saved output/asset_priorities.csv and output/summary.html')
if __name__=='__main__':main()
