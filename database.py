import sqlite3

def init_db():
    con = sqlite3.connect("sites.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            url TEXT,
            login TEXT,
            senha TEXT,
            tipo TEXT
        )
    """)
    con.commit()
    con.close()

def add_site(nome, url, login, senha, tipo):
    con = sqlite3.connect("sites.db")
    cur = con.cursor()
    cur.execute("INSERT INTO sites (nome, url, login, senha, tipo) VALUES (?, ?, ?, ?, ?)", 
                (nome, url, login, senha, tipo))
    con.commit()
    con.close()

def get_all_sites():
    con = sqlite3.connect("sites.db")
    cur = con.cursor()
    cur.execute("SELECT nome, url, login, senha, tipo FROM sites")
    rows = cur.fetchall()
    con.close()
    return rows
