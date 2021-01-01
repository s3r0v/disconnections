# Скрипт добавляет данные в БД
import sqlite3


def create_table():
    conn = sqlite3.connect("disconnections.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE disconnections 
        (region, distict, location, object, startdate, starttime,enddate,endtime,branch,restitle)"""
    )
    conn.commit()
    conn.close()


def send_data_to_db(results, sent_data_db):
    conn = sqlite3.connect("disconnections.db")
    c = conn.cursor()
    for disconnection in results:
        if disconnection not in sent_data_db:
            c.execute('INSERT INTO disconnections VALUES (?,?,?,?,?,?,?,?,?,?)',
                (disconnection['region'],
                disconnection['district'],
                disconnection['location'],
                disconnection['object'],
                disconnection['disconn-start-date'],
                disconnection['disconn-start-time'],
                disconnection['disconn-end-date'],
                disconnection['disconn-end-time'],
                disconnection['branch'],
                disconnection['res_title'])
                )
            sent_data_db.append(disconnection)
    conn.commit()
    conn.close()
    return sent_data_db
