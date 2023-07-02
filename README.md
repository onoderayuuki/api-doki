# api-doki
python3 -m venv venv

### 起動
source venv/bin/activate
functions-framework --target hello_http --debug


## ローカル用の認証情報の設定
export GOOGLE_APPLICATION_CREDENTIALS="key/doki-391416-ede3b39bd2ac.json"


## pythonで
chmod +x test.py
./test.py