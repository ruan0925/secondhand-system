import json
import os

def load_data(filename):
    # 路径改为data目录下
    path = f"data/{filename}.json"
    # 如果data文件夹不存在，自动创建（防止报错）
    if not os.path.exists("data"):
        os.mkdir("data")
        
    if not os.path.exists(path):
        # users用字典{}，商品/订单用列表[]
        if filename == "users":
            data = {}
        else:
            data = []
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return data
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(filename, data):
    path = f"data/{filename}.json"
    # 兜底建文件夹
    if not os.path.exists("data"):
        os.mkdir("data")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)