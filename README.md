# TodoApp
Django学習用個人開発

---
## 🚀使用技術
- **フロントエンド**：HTML, CSS, Bootstrap
- **バックエンド**：Python（Django）, MySQL
- **インフラ**：Docker

---
## ▶️  起動方法
```bash
# 環境変数ファイルの作成
cp .env.example .env

# 🔑SECRET_KEY生成方法
python -c "import secrets; print(secrets.token_urlsafe(50))"

# ビルド
docker compose build

# 起動
docker compose up

# ブラウザで確認
http://localhost:8000/login/
```

---
## 📸起動イメージ
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/08ea62cb-d7e2-4f40-926c-d9720ca6ab33" />
