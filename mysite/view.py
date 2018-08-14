import json
from django.http import HttpResponse
from django.shortcuts import render
# import psycopg2
from  django.db import connection
import json
import sys
def hello(request):
    a=request.GET['a'];
    return HttpResponse("hello,"+a)
def haha(request):
	return HttpResponse(request.GET['jsoncallback']+"(13132131)")
def test(request):
    context          = {}
    context['hello'] = '123123'
    return render(request, 'hello.html', context)
def con(request):
    # con = psycopg2.connect(database='postgres', user='postgres',password="root")
    cur = connection.cursor()
    # cur.execute('insert into user_tbl name values("1231")')         
    cur.execute('SELECT  *  FROM   company')         
    ver = cur.fetchall()
    context = {}
    context['data']=ver
    return HttpResponse(request.GET['jsoncallback']+"("+context+")")
def sqltest(request):
    cur = connection.cursor()   
    cur.execute('select * from company')
    res = cur.fetchall()
    return HttpResponse(request.GET['jsoncallback']+"("+json.dumps(res)+")", content_type="application/json")