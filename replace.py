import os

# 定義要尋找的舊程式碼（直接使用你提供的字串，包含隱形的不間斷空格）
old_text = """<article>
											<a href="index.html" class="image"><img src="images/main_info.jpg" alt="" /></a>
											<p>夜幕低垂，說書人化身嚮導，以音符翻開神祕物語。邀請您在星群下，聆聽關於夢與記憶的幻影奇談。</p>
										</article>"""

# 定義要替換成的新程式碼
new_text = """<article>
											<a href="index.html" class="image"><img src="images/main_info.jpg" alt="" /></a>
											<p>夜幕低垂，說書人化身嚮導，以音符翻開神祕物語。邀請您在星群下，聆聽關於夢與記憶的幻影奇談。</p>
											<a href="book.pdf" class="button fit" style="font-size: 1em; "><i class="fas fa-file-download"></i> 下載文字版 PDF 節目冊檔案</a>
										</article>"""

# 遍歷當前資料夾
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            
            # 使用 utf-8 讀取網頁內容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 如果內容有完全符合的選單，就進行更換
            if old_text in content:
                updated_content = content.replace(old_text, new_text)
                
                # 寫回原本的檔案
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"成功更新檔案: {file}")
            else:
                print(f"跳過（未偵測到相符內容）: {file}")

print("--- 所有檔案處理完畢 ---")