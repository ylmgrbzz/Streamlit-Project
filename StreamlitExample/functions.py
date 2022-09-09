import sqlite3
import pandas as pd
import streamlit as st
import datetime


conn=sqlite3.connect("serviscrm.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS modeller(
    marka TEXT,
    isim TEXT,
    yil INTEGER
    )""")
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS randevular(
    isim TEXT,
    soyisim TEXT,
    model TEXT,
    plaka TEXT,
    tarih TEXT,
    fiyat REAL,
    detay TEXT,
    telefon TEXT
)
""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS urunler(
    isim TEXT,
    model TEXT,
    fiyat REAL
)""")
conn.commit()


def modelekle(marka,isim,yil):
    conn=sqlite3.connect("serviscrm.db")
    c=conn.cursor()
    c.execute("INSERT INTO modeller VALUES(?,?,?)",(marka,isim,yil))
    conn.commit()
def randevuekle(isim,soyisim,model,plaka,tarih,fiyat,detay,telefon):
    conn=sqlite3.connect("serviscrm.db")
    c=conn.cursor()
    c.execute("INSERT INTO randevular VALUES(?,?,?,?,?,?,?,?)",
              (isim,soyisim,model,plaka,tarih,fiyat,detay,telefon))
    conn.commit()
def urunekle(isim,model,fiyat):
    conn=sqlite3.connect("serviscrm.db")
    c=conn.cursor()
    c.execute("INSERT INTO urunler VALUES(?,?,?)",(isim,model,fiyat))
    conn.commit()

def listele(tablo):
    conn=sqlite3.connect("serviscrm.db")
    c=conn.cursor()
    c.execute("SELECT * FROM "+tablo)
    sonuc=c.fetchall()
    return sonuc

def tabloyap(tablo,sutunlar):
    conn=sqlite3.connect("serviscrm.db")
    c=conn.cursor()
    c.execute("SELECT * FROM "+tablo)
    sonuc=c.fetchall()
    df=pd.DataFrame(sonuc)
    df.columns=sutunlar
    st.table(df)

def gununrandevu():
    conn = sqlite3.connect("serviscrm.db")
    c = conn.cursor()
    bugun=datetime.date.today()
    c.execute("SELECT * FROM randevular WHERE tarih=? ",(bugun,))
    sonuc=c.fetchall()
    tablo=pd.DataFrame(sonuc)
    tablo=st.table(tablo)
    return tablo

