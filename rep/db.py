#Скрипт добавляет данные в БД
import mysql.connector
import os

def create_database():
    sql = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="kikekike"
    )

    cursor = sql.cursor()
    cursor.execute("CREATE DATABASE disconnections")
    return(cursor)