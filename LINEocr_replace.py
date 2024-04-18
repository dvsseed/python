with open('lineocr.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('lineocr.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        line = line.replace("中华民图", "中華民國")
        line = line.replace("中華民国", "中華民國")
        line = line.replace("發文字院", "發文字號")
        line = line.replace("發文字统", "發文字號")
        line = line.replace("文字统", "發文字號")
        line = line.replace("遠別", "速別")
        line = line.replace("附伴", "附件")
        line = line.replace("密等及解密條件戏保密期展", "密等及解密條件或保密期限")
        line = line.replace("贵學會", "貴學會")
        line = line.replace("贵學会", "貴學會")
        line = line.replace("贵学会", "貴學會")
        line = line.replace("营運管理系统", "營運管理系統")
        line = line.replace("契約规範", "契約規範")
        line = line.replace("社法人永清發展", "社團法人永續發展")
        line = line.replace("社围法人永清發展工程學会", "社團法人永續發展工程學會")
        line = line.replace("社團法人永績發展工程學介", "社團法人永續發展工程學會")
        line = line.replace("耐本", "副本")
        line = line.replace(":", "：")
        line = line.replace(",", "，")
        f.write(line)

print('文字罝換完成!!')