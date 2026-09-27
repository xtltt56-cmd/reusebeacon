"""Recount the existing issue-data snapshots without treating pass_rate as all assertions passed."""
import hashlib
import json
import re
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main():
    rows=[]
    sources=[]
    contradictions=[]
    for path in sorted((ROOT/'results').glob('iteration-*.json')):
        data=json.loads(path.read_text(encoding='utf-8'))
        sources.append({'file':path.relative_to(ROOT).as_posix(),'sha256_lf':hashlib.sha256(path.read_bytes().replace(b'\r\n',b'\n')).hexdigest(),'runs':len(data['runs'])})
        for key,run in data['runs'].items():
            rows.append((path.stem,key,run))
            grade=run.get('grading',{})
            text=json.dumps(grade,ensure_ascii=False)
            fractions=[(int(a),int(b)) for a,b in re.findall(r'(?<!\d)(\d+)/(\d+)(?!\d)',text)]
            partial=sorted(set((a,b) for a,b in fractions if 0<=a<b))
            if grade.get('pass_rate')==1 and partial:
                contradictions.append({'file':path.relative_to(ROOT).as_posix(),'run':key,'pass_rate':1,'partial_assertion_counts':partial})
    def compare(prefix, iterations):
        subset=[(k,r) for it,k,r in rows if it in iterations and k.startswith(prefix)]
        arms={arm:[r['total_tokens'] for k,r in subset if k.endswith('/'+arm)] for arm in ('with_skill','without_skill','with_search_first')}
        means={arm:statistics.mean(values) for arm,values in arms.items()}
        return {'n_per_arm':{k:len(v) for k,v in arms.items()},'mean_reported_total_tokens':means,
                'reusebeacon_vs_no_skill_percent':100*(means['with_skill']/means['without_skill']-1)}
    result={'scope':'Recalculation of already-published JSON; no independent replay of these model runs.',
            'sources':sources,'record_count':len(rows),'unique_run_keys':len({k for _,k,_ in rows}),
            'task_ids':sorted({re.match(r'eval-\d+',k).group() for _,k,_ in rows}),
            'records_in_iterations_5_6_7':sum(it in ('iteration-5','iteration-6','iteration-7') for it,_,_ in rows),
            'pass_rate_with_partial_assertions':contradictions,
            'v032_csv':compare('eval-2-',('iteration-5','iteration-7')),
            'v032_cron':compare('eval-6-',('iteration-5','iteration-7'))}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
