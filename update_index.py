import os
import re
import urllib.request
import json

def get_repo_info():
    """يجلب وصف المستودع باستخدام مكتبة البايثون الأساسية"""
    try:
        # الحصول على رابط المستودع
        repo_url = os.popen("git remote get-url origin").read().strip()
        match = re.search(r'github\.com[:/](.+?)/(.+?)(\.git)?$', repo_url)
        if match:
            user_name = match.group(1)
            repo_name = match.group(2).replace('.git', '')
            
            api_url = f"https://api.github.com/repos/{user_name}/{repo_name}"
            
            # فتح الرابط باستخدام مكتبة urllib الأساسية
            with urllib.request.urlopen(api_url) as response:
                data = json.loads(response.read().decode())
                desc = data.get('description')
                if desc:
                    return desc
    except:
        pass
    return "القانون الإداري" # اسم احتياطي

def get_html_title(file_path):
    """يقرأ عنوان الفصل من داخل الملف"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).split('-')[0].strip()
    except:
        pass
    return file_path

def generate_index():
    main_file = "index.html"
    files = sorted([f for f in os.listdir('.') if f.startswith('ch') and f.endswith('.html')])
    
    book_title = get_repo_info()
    
    with open(main_file, "w", encoding="utf-8") as f:
        f.write(f'''<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>فهرس فصول - {book_title}</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
<style>
  body {{ font-family: "Cairo", sans-serif; background: #080808; color: #f8fafc; padding: 20px; margin: 0; min-height: 100vh; }}
  .header {{ text-align: center; padding: 30px 0; }}
  h1 {{ color: #d4af37; font-size: 1.8rem; margin-bottom: 5px; text-shadow: 0 0 15px rgba(212, 175, 55, 0.4); }}
  .book-name {{ color: #a67c00; font-size: 1.1rem; font-weight: bold; margin-bottom: 25px; letter-spacing: 1px; }}
  .container {{ max-width: 650px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding-bottom: 60px; }}
  .chapter-card {{ background: rgba(20, 20, 20, 0.8); border: 1px solid rgba(212, 175, 55, 0.1); border-radius: 14px; padding: 16px 20px; text-decoration: none; transition: all 0.3s ease; display: flex; align-items: center; gap: 15px; }}
  .chapter-card:hover {{ transform: scale(1.02); border-color: #d4af37; background: rgba(212, 175, 55, 0.05); }}
  .chapter-title {{ color: #f8fafc; font-size: 1.05rem; font-weight: bold; flex-grow: 1; }}
  .chapter-icon {{ background: #d4af37; color: #080808; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-size: 0.85rem; font-weight: 700; order: -1; }}
  .telegram-btn {{ display: flex; align-items: center; justify-content: center; gap: 10px; background: linear-gradient(135deg, #a67c00, #d4af37); color: #080808; padding: 16px 30px; border-radius: 50px; text-decoration: none; font-weight: bold; margin-top: 35px; align-self: center; }}
  .footer {{ text-align: center; margin-top: 40px; font-size: 0.7rem; color: #444; }}
</style>
</head>
<body>
<div class="header">
  <h1>فهرس فصول الكتاب</h1>
  <div class="book-name">{book_title}</div>
</div>
<div class="container">
''')
        
        for index, file_name in enumerate(files, start=1):
            arabic_title = get_html_title(file_name)
            f.write(f'''  <a href="{file_name}" class="chapter-card">
    <span class="chapter-icon">{index}</span>
    <span class="chapter-title">{arabic_title}</span>
  </a>\n''')
        
        f.write('''  <a href="https://t.me/M5M5P" class="telegram-btn">انضم لقناة التليجرام ✈️</a>
  <div class="footer">تم التحديث بواسطة فاعل خير</div>
</div>
</body>
</html>''')

if __name__ == "__main__":
    generate_index()
