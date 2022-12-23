
import requests
from task.models import NewID,New

def runtime():
    url_token = 'http://localhost:8000/api/token/'
    response_token = requests.post(url_token, json={"username":"alimohseni", "password": "123456"},)
    access_token = response_token.json()["access"]
    print(access_token)

    url = 'http://localhost:8000/news/'
    header = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=header)
    data = response.json()

    id_object_database = list(NewID.objects.all())

    for new in data:
        if new["id"] not in id_object_database:
            NewID.objects.create(new_id = new["id"])
            
            New.objects.create(id_new=new["id"], title=new["title"], summary=new["summary"],
             date_published=new["date_published"], url=new["url"],
              content_html=new["content_html"])

        


    
    
    
    