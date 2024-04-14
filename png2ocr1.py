# from google.cloud import vision
# from google.cloud.vision import types
from google.cloud import vision_v1
types = vision_v1.types

def detect_text(path):
    """Detects text in the file located in path."""
    client = vision_v1.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    # 将识别结果保存到 txt 文件中
    with open('output.txt', 'w', encoding='utf-8') as f:
        for text in texts:
            f.write(text.description + '\n')

# 使用示例
detect_text('11300XX_1.png')
