import sqlite3

DB_PATH = "database/ai_compass.db"


def get_connection():

    return sqlite3.connect(DB_PATH)

def get_connected_topics(topic):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT connected_topic

    FROM topic_connections

    WHERE source_topic = ?

    """, (topic,))

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def get_learning_content(topic_key):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

   SELECT
    t.title,
    lc.definition,
    lc.example,
    lc.importance,
    lc.bridge,
    lc.reflection

    FROM learning_content lc

    JOIN topics t
    ON lc.topic_key = t.topic_key

    WHERE lc.topic_key = ?
                   
    """, (topic_key,))

    result = cursor.fetchone()

    conn.close()

    return result


def get_micro_quiz(topic_key):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT
        question,
        option_a,
        option_b,
        option_c,
        correct_answer,
        explanation

    FROM micro_quizzes

    WHERE topic_key = ?

    ORDER BY RANDOM()

    LIMIT 1

    """ , (topic_key,))

    result = cursor.fetchone()

    conn.close()

    return result

def get_quiz_questions():

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            question,
            option_a,
            option_b,
            option_c,
            correct_answer,
            explanation

        FROM quiz_questions

        ORDER BY RANDOM()

        LIMIT 5

        """)

        rows = cursor.fetchall()

        conn.close()

        questions = []

        for row in rows:

            questions.append({

                "question": row[0],
                "option_a": row[1],
                "option_b": row[2],
                "option_c": row[3],
                "correct_answer": row[4],
                "explanation": row[5]

            })

        return questions
