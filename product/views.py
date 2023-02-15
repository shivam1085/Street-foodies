from django.shortcuts import render
import sqlite3
from .models import Vendor

# Create your views here.
def show(request):
    objs=Vendor.objects.all()
    #print(objs,"chal rha hai")
    return render(request,"explore.html",{'objs':objs})

def search(request):
    
    # conn = sqlite3.connect("db.sqlite3")
    # cur = conn.cursor()
    # print(cur)
    query=request.GET['q']
    result = Vendor.objects.filter(title__contains=query )
    print(result)
    # query="'%"+query+"%'"
    # #params = (query)
    # cur.execute("""SELECt Title,location,f_img,time,rating FROM product_food WHERE category LIKE"""+query+ """;""")
    # # cur.execute("SELECT * FROM ebook WHERE name MATCH query;")

    # rows = cur.fetchall()
    # print(rows)
    return render(request,"search.html",{'objs':result})
    