from flask import Flask, redirect, url_for, request, jsonify, Response
import mysql.connector
import json


def get():
    cnx = mysql.connector.connect(user='root', password='', host='db', database='db')
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM words')
    row_headers = [x[0] for x in cursor.description]
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json.dumps(json_data, 200)
    cursor.close()
    cnx.close()
