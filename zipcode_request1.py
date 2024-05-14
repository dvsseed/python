import requests
import pandas as pd
import time

def get_zip_code(address):
    api_url = f'https://zip5.5432.tw/zip5json.py?adrs={address}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get('zipcode6')
    return None

def main(input_xlsx, output_xlsx):
    df = pd.read_excel(input_xlsx)  # 讀取 Excel 檔案

    zip_codes = []
    for address in df['住址']:
        zip_code = get_zip_code(address)
        if zip_code:
            zip_codes.append(zip_code)
        else:
            zip_codes.append('NA')
        time.sleep(1)  # 增加延遲時間

    df['郵遞區號'] = zip_codes

    df.to_excel(output_xlsx, index=False)  # 將 DataFrame 寫入 Excel 檔案，不包含索引

if __name__ == "__main__":
    input_xlsx = 'yilanma_zipcode.xlsx'  # 請替換成你的輸入Excel檔案路徑
    output_xlsx = 'output_file.xlsx'  # 請替換成你的輸出Excel檔案路徑
    main(input_xlsx, output_xlsx)
