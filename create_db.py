import sqlite3

conn = sqlite3.connect('app.db')
c = conn.cursor()

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    job_title TEXT,
    workplace TEXT
)
''')


conn.commit()


c.execute('''
    INSERT INTO users (name, job_title, workplace)
    VALUES ("Paul Okopnyi", "PhD Candidate", "UiB")
''')

c.execute('''
    ALTER TABLE users
    ADD COLUMN login TEXT
''')
conn.commit()

c.execute('''
    UPDATE users
    SET login="paul"
    WHERE name="Paul Okopnyi"
''')
conn.commit()


c.execute('''
    ALTER TABLE users
    ADD COLUMN photo TEXT
''')
conn.commit()

users = [
    {
        'login': 'igor',
        'name': 'Igor Novikov',
        'job_title': 'Designer',
        'workplace': 'ArtLebedev'
    },
    {
        'login': 'boris',
        'name': 'Boris Ivanov',
        'job_title': 'Cat',
        'workplace': 'HSE Sedova'
    }
]

for user in users:
    c.execute("INSERT INTO users "
              "(login, name, workplace, job_title) "
              "VALUES "
              "('{login}','{name}','{workplace}','{job_title}')".format(**user))
    conn.commit()


c.execute('''
    CREATE TABLE events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        desc TEXT,
        date DATETIME
    )
''')
conn.commit()

c.execute('''
    INSERT INTO events (name, desc, date)
    VALUES
    ("Tusa","HSE Party Hard", "2019-01-10 21:00:00")
''')
conn.commit()

c.execute('''
    CREATE TABLE users_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        event_id INTEGER
    )
''')

conn.commit()

c.execute("INSERT INTO users_events (user_id, event_id) VALUES (1, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (3, 1)")
conn.commit()


c.execute("SELECT u.* "
          "FROM users_events ue "
          "JOIN users u ON (u.id=ue.user_id) "
          "WHERE ue.event_id=1")

conn.close()



