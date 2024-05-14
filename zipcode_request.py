import requests
import csv
import time

def get_zip_code(address):
    api_url = f'https://zip5.5432.tw/zip5json.py?adrs={address}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get('zipcode6')
    return None

def main(input_csv, output_csv):
    with open(input_csv, newline='', encoding='utf-8-sig') as f:  # 使用 'utf-8-sig' 編碼處理 BOM
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        address = row['住址']
        zip_code = get_zip_code(address)
        if zip_code:
            row['郵遞區號'] = zip_code
        else:
            row['郵遞區號'] = 'NA'  # Not Available
        time.sleep(1)  # 增加延遲時間1秒

    fieldnames = ['會員編號', '姓名', '郵遞區號', '住址', '市話', 'E-MAIL']

    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as f:  # 使用 'utf-8-sig' 編碼處理 BOM
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')  # 將 delimiter 設定為逗號
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    input_csv = 'yilanma_zipcode.csv'  # 請替換成你的輸入CSV檔案路徑
    output_csv = 'output_file.csv'  # 請替換成你的輸出CSV檔案路徑
    main(input_csv, output_csv)
