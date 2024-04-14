# python imagesdedup.py
import imagededup

# 設定要掃描的資料夾
photo_dir = "photo"

# 設定要掃描的圖片格式
image_formats = [".jpg", ".png"]

# 設定重複圖片的相似度閾值
similarity_threshold = 0.9

# 建立 ImageDedup 物件
imagededup = imagededup.ImageDedup(photo_dir, image_formats, similarity_threshold)

# 掃描資料夾中的所有圖片
imagededup.scan()

# 獲取所有重複的圖片
duplicates = imagededup.get_duplicates()

# 輸出重複圖片的檔案名稱
for duplicate in duplicates:
    print(", ".join(duplicate))
