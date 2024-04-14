import glob
import aspose.words as aw


def convert_word_to_jpg(word_file):
    # load document
    doc = aw.Document("word_file")

    # set output image format
    options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)

    # loop through pages and convert them to PNG images
    for pageNumber in range(doc.page_count):
        options.page_set = aw.saving.PageSet(pageNumber)
        doc.save("temp/" + str(pageNumber + 1) + "_page.png", options)


def main():
    # 創建 temp 子目錄
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 遍歷當前目錄中的 Word 文件
    word_files = glob.glob("*.doc")  # + glob.glob("*.doc") + glob.glob("*.dotx")

    # 遍歷 Word 文件進行轉換
    for word_file in word_files:
        convert_word_to_jpg(word_file)

    print("轉換完成！")


if __name__ == "__main__":
    main()