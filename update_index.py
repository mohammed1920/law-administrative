import os
import re

def get_html_title(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
    except Exception:
        pass
    return file_path

def generate_index():
    main_file = "index.html"
    files = sorted([f for f in os.listdir('.') if f.startswith('ch') and f.endswith('.html')])
    
    with open(main_file, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html>\n<html dir="rtl" lang="ar">\n<head>\n')
        f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write('<title>فهرس فصول الكتاب</title>\n')
        f.write('<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">\n')
        f.write('<style>\n')
        f.write('  body { font-family: "Cairo", sans-serif; background: #080808; color: #f8fafc; padding: 20px; margin: 0; min-height: 100vh; }\n')
        f.write('  .header { text-align: center; padding: 30px 0; }\n')
        f.write('  h1 { color: #d4af37; font-size: 1.8rem; margin-bottom: 5px; text-shadow: 0 0 15px rgba(212, 175, 55, 0.4); }\n')
        
        # تنسيق اسم الكتاب (بدل تحديث ذكي)
        f.write('  .book-name { color: #a67c00; font-size: 1.1rem; font-weight: bold; margin-bottom: 25px; letter-spacing: 1px; }\n')
        
        f.write('  .container { max-width: 650px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding-bottom: 60px; }\n')
        f.write('  .chapter-card { \n')
        f.write('      background: rgba(20, 20, 20, 0.8); \n')
        f.write('      border: 1px solid rgba(212, 175, 55, 0.1); border-radius: 14px; \n')
        f.write('      padding: 16px 20px; text-decoration: none; transition: all 0.3s ease; \n')
        f.write('      display: flex; align-items: center; gap: 15px; \n')
        f.write('  }\n')
        f.write('  .chapter-card:hover { \n')
        f.write('      transform: scale(1.02); border-color: #d4af37; \n')
        f.write('      background: rgba(212, 175, 55, 0.05); \n')
        f.write('  }\n')
        f.write('  .chapter-title { color: #f8fafc; font-size: 1.05rem; font-weight: bold; flex-grow: 1; }\n')
        f.write('  .chapter-icon { background: #d4af37; color: #080808; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-size: 0.85rem; font-weight: 700; order: -1; }\n')
        f.write('  .telegram-btn { \n')
        f.write('      display: flex; align-items: center; justify-content: center; gap: 10px; \n')
        f.write('      background: linear-gradient(135deg, #a67c00, #d4af37); color: #080808; \n')
        f.write('      padding: 16px 30px; border-radius: 50px; text-decoration: none; font-weight: bold; \n')
        f.write('      margin-top: 35px; align-self: center; \n')
        f.write('  }\n')
        f.write('  .footer { text-align: center; margin-top: 40px; font-size: 0.7rem; color: #444; }\n')
        f.write('</style>\n</head>\n<body>\n')
        
        # التعديل هنا: وضع اسم الكتاب بدل الجملة السابقة
        f.write('<div class="header">\n')
        f.write('  <h1>فهرس فصول الكتاب</h1>\n')
        f.write('  <div class="book-name"> القانون الدستوري</div>\n') 
        f.write('</div>\n')
        
        f.write('<div class="container">\n')
        for index, file_name in enumerate(files, start=1):
            arabic_title = get_html_title(file_name)
            f.write(f'  <a href="{file_name}" class="chapter-card">\n')
            f.write(f'    <span class="chapter-icon">{index}</span>\n')
            f.write(f'    <span class="chapter-title">{arabic_title}</span>\n')
            f.write(f'  </a>\n')
        
        f.write('  <a href="https://t.me/M5M5P" class="telegram-btn">انضم لقناة التليجرام ✈️</a>\n')
        f.write('  <div class="footer">تم التحديث بواسطة فاعل خير  </div>\n')
        f.write('</div>\n</body>\n</html>')

if __name__ == "__main__":
    generate_index()
