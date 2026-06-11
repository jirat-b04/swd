## Question
![](/assets/q_idempotency.png)
## Response Section

Idempotency คือ การส่ง Request ด้วยข้อมูลชุดเดิมซ้ำกี่ครั้งก็ตาม ผลลัพธ์ที่ได้จะต้องมีค่าเท่ากับการส่ง Request นั้นเพียงครั้งเดียวเสมอ

``` python
import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"

for i in range(3):
    res = requests.post(f"{BASE_URL}/schools/", json={
        "name": "โรงเรียนตัวอย่าง",
        "abbreviation": "รร.ตย.",
        "address": "123 ถนนตัวอย่าง"
    })
    print(f"POST #{i+1}: id={res.json().get('id')}")

print("---")

for i in range(3):
    res = requests.put(f"{BASE_URL}/schools/1/", json={
        "name": "โรงเรียนใหม่",
        "abbreviation": "รร.ใหม่",
        "address": "456 ถนนใหม่"
    })
    print(f"PUT #{i+1}: name={res.json().get('name')}")
```