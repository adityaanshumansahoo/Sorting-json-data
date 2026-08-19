import json

def load_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data.get("pages")
    
def save_sort_pages(data,file_name):
    with open (file_name,'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)