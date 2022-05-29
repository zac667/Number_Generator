import requests
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import os
import xlsxwriter
import mysql.connector
from mysql.connector import errorcode
import uuid
from random import randint

appFlask = Flask(__name__)
appFlask.secret_key = "27eduCBA09"
@appFlask.route("/telgen_full_aleatoire", methods = ['POST','GET'])
def login():

    if request.method == 'POST':
        
        prefix = request.form['prefix']
        nb_num = int(request.form['nb_num'])
        filename = str(request.form['filename'])


        
        country_code = "+33" #Type your country code here
        row = 0
        s = 0
        
        workbook = xlsxwriter.Workbook(filename+'.xlsx')
        worksheet = workbook.add_worksheet()
        def random_with_N_digits(n):
            range_start = 10**(n-1) 
            range_end = (10**n)-1
            return randint(range_start, range_end)

        while s <= nb_num:
            
            print(str(country_code)+str(prefix)+str(random_with_N_digits(8)))
            full = str(country_code)+str(prefix)+str(random_with_N_digits(8))#Choose range of your number here
            value = (full, 0, )
            
            
            worksheet.write(row, 0, full)
            s = s + 1
            row = row + 1
            

        workbook.close()

        #File is downloaded automatically in source folder
        return" <p>Fichier télécharger dans le dossier source</p>"
        #return "<a href = 'http://127.0.0.1/telgen_full_aleatoire/"+ filename +".xlsx'>Télecharger le fichier</a>"
        

    return '''<form enctype="multipart/form-data" method = "post">
    <p>Générateur de numéro</p>
    <p><input enctype="multipart/form-data" placeholder="saisissez 1 chiffes ex: 6 pour un 06 ou 1 pour 01" type="textarea" name="prefix"></p>
    <p><input enctype="multipart/form-data" placeholder="Quantité (999 999 max)" type="textarea" id="nb_num" name="nb_num"></p>
    <p><input enctype="multipart/form-data" placeholder="saisissez le nom du fichier" type="textarea" id="filename" name="filename"></p>
    <p><input enctype="multipart/form-data" type="submit" name="send_data" id="send_data" value="Générer le Fichier"></p>
    </form>'''


if __name__ == "__main__":
    appFlask.run(debug=True)
