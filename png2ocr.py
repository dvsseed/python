from PIL import Image
import pytesseract


# 載入圖片
img = Image.open('11300XX_1.png')

# 使用 pytesseract 從圖像中識別繁體中文文字
text = pytesseract.image_to_string(img, lang='chi_tra')

# 將識別結果儲存到 txt 檔案中
with open('output.txt', 'w', encoding='utf-8') as f:
     f.write(text)


# 如果需要提高繁體中文的辨識率，可以試試以下方法：
# 1. 使用更清晰的影像
# 2. 使用更大的圖像
# 3. 使用更適合的 OCR 引擎，例如 Google Cloud Vision API
