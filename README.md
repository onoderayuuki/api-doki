# api-doki
python3 -m venv venv

### 起動
source venv/bin/activate
functions-framework --target hello_http --debug
functions-framework --target list_danmens --debug
http://127.0.0.1:8080/?doki=20230514-J01-02

https://us-west1-doki-391416.cloudfunctions.net/list_danmens/?doki=20230514-J01-02

http://127.0.0.1:8080/htmls?doki=20230506-J02-01&param1=00_pcd_file.html&param2=60_mesh.html

## ローカル用の認証情報の設定
export GOOGLE_APPLICATION_CREDENTIALS="key/doki-391416-ede3b39bd2ac.json"


## pythonでtest
chmod +x test.py
./test.py

## requirement.txt
pip freeze > requirement.txt
