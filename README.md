# 日文五十音複習網站

## 本地執行

```bash
pip install -r requirements.txt
streamlit run app.py
```

瀏覽器開啟 http://localhost:8501

## 部署到 Streamlit Community Cloud（免費）

1. 將整個資料夾推送到 GitHub
2. 前往 https://share.streamlit.io 登入
3. 點 **New app**
4. 選擇你的 repo 和 `app.py`
5. 點 **Deploy**

## 檔案說明

| 檔案 | 說明 |
|------|------|
| `app.py` | Streamlit 入口 |
| `japanese_study.html` | 主要網頁內容 |
| `requirements.txt` | Python 套件需求 |
