import sqlite3


conn = sqlite3.connect("database/ai_compass.db")

cursor = conn.cursor()


# ==========================================
# MODULES TABLE
# ==========================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS modules (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    module_name TEXT UNIQUE NOT NULL

)

""")


# ==========================================
# TOPICS TABLE
# ==========================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS topics (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    module_id INTEGER NOT NULL,

    topic_key TEXT UNIQUE NOT NULL,

    title TEXT NOT NULL,

    FOREIGN KEY (module_id)
    REFERENCES modules(id)

)

""")


# ==========================================
# LEARNING CONTENT TABLE
# ==========================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS learning_content (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    topic_key TEXT UNIQUE NOT NULL,

    definition TEXT NOT NULL,

    example TEXT,

    importance TEXT,

    bridge TEXT,

    reflection TEXT,

    FOREIGN KEY (topic_key)
    REFERENCES topics(topic_key)

)

""")


# ==========================================
# MICRO QUIZZES TABLE
# ==========================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS micro_quizzes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    topic_key TEXT NOT NULL,

    question TEXT NOT NULL,

    option_a TEXT NOT NULL,

    option_b TEXT NOT NULL,

    option_c TEXT NOT NULL,

    correct_answer TEXT NOT NULL,

    explanation TEXT,

    FOREIGN KEY (topic_key)
    REFERENCES topics(topic_key)

)

""")


# ==========================================
# FULL QUIZ QUESTIONS TABLE
# ==========================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS quiz_questions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    topic_key TEXT NOT NULL,

    question TEXT NOT NULL,

    option_a TEXT NOT NULL,

    option_b TEXT NOT NULL,

    option_c TEXT NOT NULL,

    correct_answer TEXT NOT NULL,

    explanation TEXT,

    FOREIGN KEY (topic_key)
    REFERENCES topics(topic_key)

)

""")


# ==========================================
# TOPIC CONNECTIONS TABLE
# ==========================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS topic_connections (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    source_topic TEXT NOT NULL,

    connected_topic TEXT NOT NULL,

    relationship_type TEXT NOT NULL,

    FOREIGN KEY (source_topic)
    REFERENCES topics(topic_key),

    FOREIGN KEY (connected_topic)
    REFERENCES topics(topic_key)

)

""")


conn.commit()

conn.close()


print("AI Compass database setup complete.")