import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")


def insert(item, quan, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('Wine glass', 4,10.5)")
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quan, price))
    conn.commit()
    conn.close()


def view_data():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    row = cur.fetchall()
    conn.close()
    return row


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update(quan, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE  store SET quantity=?,price=? WHERE item=?",
                (quan, price, item))
    conn.commit()
    conn.close()


insert('plates', 18, 5.5)
# delete('plates')

update(4, 2, 'Wine glass')

print(view_data())
