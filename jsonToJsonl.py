import json

filenamePrefix = 'idioms'

# JSON 파일 읽기
with open('dataset/'+filenamePrefix+'.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# JSONL 파일로 쓰기
with open('converted/'+filenamePrefix+'.jsonl', 'w', encoding='utf-8') as f:
    for entry in data:
        f.write(json.dumps(entry, ensure_ascii=False))
        f.write('\n')
