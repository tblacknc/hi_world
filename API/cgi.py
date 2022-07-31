#!C:\Users\tblac\AppData\Local\Programs\Python\Python39\python.exe

import mysql.connector
from datetime import datetime

import cgitb; cgitb.enable()
import cgi
args = cgi.FieldStorage()


def sqlGet(sql):
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    return myresult
   

def getDetail(genre):
    #print("<form action='cgi.cgi' method='put'>\n")
    
    sql = f'''select re.rental_id
            from 
                rental as re
            inner join
                inventory as iv on iv.inventory_id = re.inventory_id
            inner join 
                film as fi on fi.film_id = iv.film_id
            inner join
                film_category as fc on fc.film_id = fi.film_id
            inner join
                category as ca on ca.category_id = fc.category_id
            where 
                ca.name = '{genre}'
            and 
                re.returned is null'''
                
    rent_id = sqlGet(sql)
    loop = 0
    outp1 = ""
    outp = ""
    #print(f"rent id = {rent_id}")
    for rental_id in rent_id:
        
        sql = f'''SELECT re.inventory_id, cu.email, cu.first_name, cu.last_name, 
                        ad.address, ad.address2, ad.district, ad.postal_code, ad.phone, 
                        ci.city, co.country, fi.title, fi.replacement_cost, re.return_date
                    FROM 
                        rental as re
                    inner join
                        customer as cu on cu.customer_id = re.customer_id
                    inner join
                        address as ad on ad.address_id = cu.address_id
                    inner join
                        city as ci on ci.city_id = ad.city_id
                    inner join 
                        country as co on co.country_id = ci.country_id
                    inner join
                        inventory as iv on iv.inventory_id = re.inventory_id
                    inner join 
                        film as fi on fi.film_id = iv.film_id
                    where
                        re.rental_id = {rental_id[0]} '''
        #print(f"<br><br>SQL====== {sql}<br>")
        info = sqlGet(sql)
        
        email = info[0][1]
        name = f"{info[0][2]} {info[0][3]}"
        address = info[0][4]
        address2 = info[0][5]
        district = info[0][6]
        postalcode = info[0][7]
        phone = info[0][8]
        city = info[0][9]
        country = info[0][10]
        title = info[0][11]
        cost = info[0][12]
        rtndate = info[0][13]
        now = datetime.now()
        
        
        if rtndate:
            lateDays = now - rtndate
            due = lateDays.days
        else:
            due = 15
        
        if due > 7:

            

            loop += 1
            if loop % 2 == 1:
                #print("<div class='container p-5 my-5 border border-4'>")    
                #print("<div class='row-lg-6 border border-2'>")
                print("<div class='container mt-5'>\n")
                print("<div class='row '>\n")
                
                
                outp1 = "<span class='col-sm-1 align-right'>\n"
                outp1 += f"<input class='align-right' type='radio' name='email' value='{email}' onclick='submit();'>"
                outp1 += "</span>"
            
            
                outp1 += f"<span class='col-sm-5 border border-1'>\n"
                outp1 += f"<h6>{title} due = {rtndate} </h6>\n"
                outp1 += f"{name} ({email})\n"
                outp1 += f"<br>{address}\n"
                if address2 : outp1 += f"<br>{address2}\n"
                outp1 += f"<br>{city}, {district}\n"
                outp1 += f"<br>{country} - {postalcode}\n"
                outp1 += f"<br>phone number - {phone} - {loop}- {rental_id}\n"
                outp1 += "</span>"
                

                
               
                #print("</div>")
            elif loop %2 == 0:


                #print("<div class='container mt-5'>\n")
                #print("<div class='row '>\n")


                outp = "<span class='col-sm-1 align-right'>\n"
                outp += f"<input type='radio' name='email' value='{email}' onclick='submit();'>"
                outp += "</span>"
            
            
                outp += f"<span class='col-sm-5 border border-1'>\n"
                outp += f"<h6>{title} due = {rtndate} </h6>\n"
                outp += f"{name} ({email})\n"
                outp += f"<br>{address}\n"
                if address2 : outp += f"<br>{address2}\n"
                outp += f"<br>{city}, {district}\n"
                outp += f"<br>{country} - {postalcode}\n"
                outp += f"<br>phone number - {phone} - {loop} - {rental_id}\n"

                outp += f"</span>\n"
                #print(outp)
                #print("</div>")
                #if rental_id[0] == 12213 : print(rental_id, title, outp1)

                print(outp1)
                print(outp)
                outp1 = ""
                outp = ""
            else:
                print("fgxfxg")
            
    if outp == "" : print(f"{outp1}")
    if outp1 == "" : print(f"{outp}")
    #print("</div there>\n")
    print("</div row>\n")
    
    print("</div container>\n")
    print("</div row-lg-12>\n")


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sakila"
)
mycursor = mydb.cursor()
   
print("Content-Type: text/html; charset=UTF- 8\n\n")



head = '''<!DOCTYPE html>
		<html>
		<head>

		<meta charset='utf-8'>
		<meta name='viewport' content='width=device-width, initial-scale=1'>
		<title>playing with sql</title>
		<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet'>
		<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js'></script>

		</head>
		<body>\n'''
print(head)

print("<body>")


page = args.getvalue('page')
genre = args.getvalue('genre')

if page is None:
    print(f"------->{page}<---------")


    print("<div class='container p-5 my-5 border border-2'>")    
    print("<div class='row col-sm-6 border border-2'>")
    print("<form action='cgi.cgi' method='put'>")
    print("<br><input type='submit' value='Submit'>\n\r")
    print("<input type='hidden' id='page' name='page' value='2'>\n")
    print("</form>")
    print("<div class='float-right'>test</div>")
    print("<p>test</p>")
    print("<p>test</p>")
    print("</div>")

    
    print("</div>")
    print("</div>")

    import matplotlib.pyplot as plt
    import numpy as np
    import os

    os.environ['HOME'] = 'C:/Python'


    y = np.array([35, 25, 25, 15])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

    plt.pie(y, labels = mylabels)
    plt.show()


elif (page == '2'):
    print("<div class='container p-5 my-5 border border-2'>")    
    print("<div class='row-lg-12 border border-2'>")
    print(f"------->{page}<---------")
    
    sql = ''' select distinct inventory_id from rental '''
    rentals = sqlGet(sql)

    category = []
    catVal = []

    for x in range(1,18,1):
        catVal.append("")
        category.append(0)
        
    catCount = 1
    sql = '''select name, category_id from category order by category_id'''
    categories = sqlGet(sql)
    for cat in categories:
        #print(f"cat ====={cat}")
        catVal[catCount] = cat[0]
        catCount += 1

    #sql = '''select count(rental_id) from rental'''
    #totl = sqlGet(sql)

    total = 0

    for rental in rentals:
        sql=f'''SELECT i.inventory_id, fc.category_id, f.title, c.name
            FROM film_category as fc 
            inner join category as c on c.category_id=fc.category_id 
            inner join film as f on f.film_id=fc.film_id 
            inner join inventory as i on f.film_id=i.film_id 
            inner join rental as re
            where i.inventory_id = {rental[0]}
            and re.returned is not null
            limit 1'''

        movie = sqlGet(sql)

        category[movie[0][1]] += 1

    loop = 0
    for cat in catVal:
        # print(f"<br>{catVal[loop]} has {category[loop]} films")
        total += int(category[loop])
        loop += 1
    
    catVal2 = []
    category2 = []
    for x in range(1,18,1):
        catVal2.append("")
        category2.append(0)
        
    catCount = 1
    sql = '''select name, category_id from category order by category_id'''
    categories = sqlGet(sql)
    for cat in categories:
        
        
        catVal2[catCount] = cat[0]
        catCount += 1
    cost = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for rent in rentals:
        sql = f'''SELECT fi.title, fi.film_id, ca.name, fc.category_id, fi.rental_rate  
                FROM rental as re
                    inner join
                inventory as iv on iv.inventory_id = re.inventory_id
                    inner join 
                film as fi on iv.film_id = fi.film_id
                    inner join
                film_category as fc on fc.film_id = fi.film_id
                    inner join 
                category as ca on ca.category_id = fc.category_id
                    where  iv.inventory_id = {rent[0]}
                    and returned is null
                    limit 1 '''

        out = sqlGet(sql)        
        if out:
            category2[out[0][3]] += 1  
            money = out[0][4]
            
            cost[out[0][3]] += money
    
    loop = 0
    total2 = 0
    pcnt = 0
    totcost = 0
    print("<form action='cgi.cgi' method='put'>")

    for cat in catVal:
        if category[loop] != 0 : pcnt = 100 * (category2[loop] / category[loop])
        pcnt = '{:.2f}'.format(pcnt)
        
        print(f"<br><input type='radio' name='genre' value='{catVal[loop]}' onclick='submit();'><b>{catVal[loop]}</b> has a total of <b>{category[loop]}</b> films with <b>{category2[loop]}</b> currently out <b>{pcnt}%</b> and cost <b><i>${cost[loop]}</i></b>\n")
        
        total2 += category2[loop]
        loop += 1
        totcost += cost[loop]
    print(f"<br>for a total of <b>{total}</b> films and <b>{total2}</b> out at total cost of <b><i>${totcost}</b></i>")
    print("<input type='hidden' id='page' name='page' value='3'>\n")
    print("</form>")

    print("</div></div>")
elif (page == '3'):
    print("<div class='container p-5 my-5 border border-2'>")    
    print("<div class='row-lg-12 border border-2'>")
    print("<form action='cgi.cgi' method='put'>")
    
    print(f"------->{page}<---------")
    
    sql = ''' select distinct inventory_id from rental '''
    rentals = sqlGet(sql)

    category = []
    catVal = []

    for x in range(1,18,1):
        catVal.append("")
        category.append(0)
        
    catCount = 1
    sql = '''select name, category_id from category order by category_id'''
    categories = sqlGet(sql)
    for cat in categories:
        #print(f"cat ====={cat}")
        catVal[catCount] = cat[0]
        catCount += 1

    #sql = '''select count(rental_id) from rental'''
    #totl = sqlGet(sql)

    total = 0

    for rental in rentals:
        sql=f'''SELECT i.inventory_id, fc.category_id, f.title, c.name
            FROM film_category as fc 
            inner join category as c on c.category_id=fc.category_id 
            inner join film as f on f.film_id=fc.film_id 
            inner join inventory as i on f.film_id=i.film_id 
            inner join rental as re
            where i.inventory_id = {rental[0]}
            and re.returned is not null
            limit 1'''

        movie = sqlGet(sql)

        category[movie[0][1]] += 1

    loop = 0
    for cat in catVal:
        # print(f"<br>{catVal[loop]} has {category[loop]} films")
        total += int(category[loop])
        loop += 1
    
    catVal2 = []
    category2 = []
    for x in range(1,18,1):
        catVal2.append("")
        category2.append(0)
        
    catCount = 1
    sql = '''select name, category_id from category order by category_id'''
    categories = sqlGet(sql)
    for cat in categories:
        
        
        catVal2[catCount] = cat[0]
        catCount += 1
    cost = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for rent in rentals:
        sql = f'''SELECT fi.title, fi.film_id, ca.name, fc.category_id, fi.rental_rate  
                FROM rental as re
                    inner join
                inventory as iv on iv.inventory_id = re.inventory_id
                    inner join 
                film as fi on iv.film_id = fi.film_id
                    inner join
                film_category as fc on fc.film_id = fi.film_id
                    inner join 
                category as ca on ca.category_id = fc.category_id
                    where  iv.inventory_id = {rent[0]}
                    and returned is null
                    limit 1 '''

        out = sqlGet(sql)        
        if out:
            category2[out[0][3]] += 1  
            money = out[0][4]
            
            cost[out[0][3]] += money
    
    loop = 0
    total2 = 0
    #cost = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    pcnt = 0
    totcost = 0
    print("<form action='cgi.cgi' method='post'>")
    
    
    genre = args.getvalue('genre')

    for cat in catVal:
        if category[loop] != 0 : pcnt = 100 * (category2[loop] / category[loop])
        pcnt = '{:.2f}'.format(pcnt)
        
        print(f"<br><input type='radio' name='genre' value='{catVal[loop]}' onclick='submit();'><b>{catVal[loop]}</b> has a total of <b>{category[loop]}</b> films with <b>{category2[loop]}</b> currently out <b>{pcnt}%</b> and cost <b><i>${cost[loop]}</i></b>\n")
        #print(f"<br>GENRE ==>{genre}<---->{catVal[loop]}<---")
        if genre == catVal[loop]:
            getDetail(genre)
            pass
        total2 += category2[loop]
        loop += 1
        totcost += cost[loop]
    print(f"<br>for a total of <b>{total}</b> films and <b>{total2}</b> out at total cost of <b><i>${totcost}</b></i>")
    print(f"<input type='hidden' id='genre' name='genre' value='{genre[0]}'>\n")
    print("<input type='hidden' id='page' name='page' value='4'>\n")
    print("</form>")

    #print("</div></div>")



elif (page == '4'):
    print("<div class='container p-5 my-5 border border-2'>")    
    print("<div class='row-lg-12 border border-2'>")
    print("<form action='cgi.cgi' method='put'>")

    email = args.getvalue('email')
    
    sql = f'''SELECT cu.first_name, cu.last_name, cu.customer_id, re.rental_id, re.inventory_id,       re.return_date, re.returned, ad.address, ad.address2, ad.district, ad.postal_code, ad.phone, ci.city, co.country, fi.title, fi.rental_rate, fi.replacement_cost
    from rental as re
    inner join 
    customer as cu on cu.customer_id = re.customer_id	
    inner join
    address as ad on ad.address_id = cu.address_id
    inner join 
    city as ci on ci.city_id = ad.city_id
    inner join 
    country as co on co.country_id = ci.country_id
    inner join
    inventory as iv on iv.inventory_id = re.inventory_id
    inner join 
    film as fi on fi.film_id = iv.film_id
    where 
    cu.email = '{email}' 
    order by 
    re.returned '''
    
    print(f"<br>sql = {sql}<br>")
    outs = sqlGet(sql)
    
    name = f"{outs[0][0]} {outs[0][1]}"
    print(f"<br> {name}")
    print(f"<br>{outs[0][7]}")
    if outs[0][8] : print(outs[0][8])
    print(f"<br>{outs[0][9]} {outs[0][12]}") 
    print(f"<br>{outs[0][14]}    {outs[0][10]}")
    print(f"<br>{outs[0][11]}")
    print(f"<br>")
    
    rtndate = outs[0][5]
    now = datetime.now()
        
        
    lateDays = now - rtndate
    due = lateDays.days
            
            
    for out in outs:
        print(f"<br>{out[14]} per rental {out[15]} replacement {out[16]}")
        if out[6] == '1':
            print(f"  returned")
        else:
            
            print(f"  still out! - {due} days late!")