from format_json import sort_by_date,sort_by_facility_name,sort_by_name
from storage import load_json
file_name = "page_map.json"
pages = load_json(file_name)

print("-------Enter your opertion for sorting--------")
print("Enter '1' for sort the json_data according to Date!")
print("Enter '2' for sort the json_data according to Name !")
print("Enter '3' for sort the json_data according to Facility Name!")

if __name__=="__main__":
    operation=input("Enter Your Opertion: ")
    if operation=="1":
        sort_by_date(pages,sort_by_date="sorted_by_date.json")
    elif operation=="2":
        sort_by_name(pages,sort_by_namae="sorted_by_name.json")
    elif operation=="3":
        sort_by_facility_name(pages,sort_by_facility_name="sorted_by_facility_name.json")
    else:
        print("---Invalid Opertion !---")
    
