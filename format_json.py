from storage import load_json,save_sort_pages
from datetime import datetime

file_name = "page_map.json"
sort_by_date="sort_by_date.json"
pages = load_json(file_name)
def sort_by_date(pages,sort_by_date):
    results = []
    dated_pages = []

    for page in pages:
        candidate_dates = page["metadata"]["candidate_dos_dates"]

        if not candidate_dates:
            results.append(page)
        else:
            date_str = candidate_dates[0]["value"]
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")

            dated_pages.append((date_obj, page))

    dated_pages.sort(key=lambda x: x[0])

    for date_obj, page in dated_pages:
        results.append(page)
    save_sort_pages(results,sort_by_date)
    return results

    
def sort_by_name(pages,sort_by_namae):
    result = []
    name_pages = []
    
    for page in pages:
        candidate_name = page.get("metadata", {}).get("provider")
        
        if not candidate_name or not candidate_name.get("value"):
            result.append(page)
        else:
            name = candidate_name["value"]
            name_pages.append((name, page))
    
    name_pages.sort(key=lambda x: x[0])
    
    for name, page in name_pages:
        result.append(page)
        
    save_sort_pages(result,sort_by_namae)
    return result
def sort_by_facility_name(pages,sort_by_facility_name):
    result = []
    facility_name_pages = []
    
    for page in pages:
        facility_name = page.get("metadata", {}).get("facility_name")
        
        if not facility_name or not facility_name.get("value"):
            result.append(page)
        else:
            name = facility_name["value"]
            facility_name_pages.append((name, page))
    
    facility_name_pages.sort(key=lambda x: x[0])
    
    for name, page in facility_name_pages:
        result.append(page)
        
    save_sort_pages(result,sort_by_facility_name)
    return result

if __name__=="__main__":
    page=sort_by_name(pages,sort_by_namae="sorted_by_name.json")
    print(len(page))
    page2=sort_by_facility_name(pages,sort_by_facility_name="sorted_by_facility_name.json")
    print(len(page2))
    page1=sort_by_date(pages,sort_by_date="sort_by_date.json")
    print(len(page1))

# for idx,pag in enumerate(page,start=1):
#     print(f"sl_{idx}: {pag}\n")