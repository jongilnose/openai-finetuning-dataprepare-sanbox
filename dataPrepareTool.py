import os
import shutil

filenamePrefix = 'idioms'

# 파일 생성
os.system('openai tools fine_tunes.prepare_data -f ./converted/'+filenamePrefix+'.jsonl')

# 이동할 파일의 원본 경로
original = './converted/'+filenamePrefix+'_prepared.jsonl'

# 파일이 이동할 목적지 경로
target = './prepared/'+filenamePrefix+'_prepared.jsonl'

shutil.move(original, target)