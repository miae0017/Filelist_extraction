import pandas as pd
import chardet
from datetime import datetime

# 파일의 인코딩 감지
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
    return result['encoding']

file_path = 'filelist.txt'
encoding = detect_encoding(file_path)

# 프로토콜 이름 입력
protocol_name = input("프로토콜 이름을 입력하세요: ")

# 오늘 날짜를 YYYY-MM-DD 형식으로 가져오기
today_date = datetime.today().strftime('%Y-%m-%d')

# 파일명 생성
file_name = f"{protocol_name}_{today_date}.xlsx"

# filelist.txt 파일 읽기
with open(file_path, 'r', encoding=encoding) as file:
    lines = file.readlines()

# 각 파일 경로를 분리하여 리스트에 저장
data = []
for line in lines:
    line = line.strip()  # 줄 끝의 개행 문자 제거
    parts = line.split('\\')  # 경로를 '\'로 분리
    data.append(parts)

# 데이터 프레임 생성
df = pd.DataFrame(data)

# NaN 값을 '-' 문자로 대체 / ascending sort시 위쪽으로 sorting 되도록 의도함.
df = df.fillna('-')

# 데이터 프레임을 Excel 파일로 저장
df.to_excel(file_name, index=False, header=False)

print("파일 목록이 ", file_name, "로 저장되었습니다.")