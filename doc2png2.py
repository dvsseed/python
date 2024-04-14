import glob
from spire.doc import *
from spire.doc.common import *


def convert_word_to_jpg(word_file):
    # Create a Document object
    document = Document()

    # Load a doc or docx file
    document.LoadFromFile(word_file)

    # Loop through the pages in the document
    for i in range(document.GetPageCount()):

        # Convert a specific page to bitmap image
        imageStream = document.SaveImageToStreams(i, ImageType.Bitmap)

        # Save the bitmap to a PNG file
        with open('temp/ToImage-{0}.png'.format(i), 'wb') as imageFile:
            imageFile.write(imageStream.ToArray())

    document.Close()

def main():
    # 創建 temp 子目錄
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 遍歷當前目錄中的 Word 文件
    word_files = glob.glob("*.doc")

    # 遍歷 Word 文件進行轉換
    for word_file in word_files:
        convert_word_to_jpg(word_file)

    print("轉換完成！")


if __name__ == "__main__":
    main()