import os

# 定義要尋找的舊程式碼（直接使用你提供的字串，包含隱形的不間斷空格）
old_text = """<span class="opener">團隊成員</span>
											<ul>
												<li><a href="staff_concert.html">音樂會籌備團隊</a></li>
												<li><a href="staff_stage.html">現場工作人員</a></li>
												<li><a href="staff_ksawo.html">高雄中學校友管樂團</a></li>
												<li><a href="staff_kswb.html">高雄中學管樂團</a></li>
												<li><a href="staff_teacher.html">高雄中學管樂團分部老師</a></li>
											</ul>"""

# 定義要替換成的新程式碼
new_text = """<span class="opener">團隊成員</span>
											<ul>
												<li><a href="staff_concert.html">音樂會籌備團隊</a></li>
												<li><a href="staff_production.html">節目製作團隊</a></li>
												<li><a href="staff_stage.html">現場工作人員</a></li>
												<li><a href="staff_ksawo.html">高雄中學校友管樂團</a></li>
												<li><a href="staff_kswb.html">高雄中學管樂團</a></li>
												<li><a href="staff_teacher.html">社團指導分部老師</a></li>
											</ul>"""

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