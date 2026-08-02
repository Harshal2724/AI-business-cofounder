import sqlite3

def connect_db():

    conn = sqlite3.connect("business_ai.db")

    conn.row_factory = sqlite3.Row

    return conn



def save_idea(
    business_idea,
    business_type,
    budget,
    extra_info,
    ai_response
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO idea_history(

            business_idea,
            business_type,
            budget,
            extra_info,
            ai_response

        )

        VALUES(?,?,?,?,?)

    """,(business_idea,
         business_type,
         budget,
         extra_info,
         ai_response))

    conn.commit()

    conn.close()


def save_problem(
    problem,
    business_type,
    budget,
    extra_info,
    ai_response
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO problem_history(

    problem,
    business_type,
    budget,
    extra_info,
    ai_response

    )

    VALUES(?,?,?,?,?)

    """,(problem,
         business_type,
         budget,
         extra_info,
         ai_response))

    conn.commit()

    conn.close()


def save_marketing(
    business_idea,
    business_type,
    marketing_budget,
    target_audience,
    business_goals,
    extra_info,
    user_marketing_idea,
    ai_response
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO marketing_history(

    business_idea,
    business_type,
    marketing_budget,
    target_audience,
    business_goals,
    extra_info,
    user_marketing_idea,
    ai_response

    )

    VALUES(?,?,?,?,?,?,?,?)

    """,(business_idea,
         business_type,
         marketing_budget,
         target_audience,
         business_goals,
         extra_info,
         user_marketing_idea,
         ai_response))

    conn.commit()

    conn.close()



def save_business_plan(
    additional_information,
    ai_response
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO business_plan_history(

    additional_information,
    ai_response

    )

    VALUES(?,?)

    """,(additional_information,
         ai_response))

    conn.commit()

    conn.close()



def get_idea_history():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM idea_history

    ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_problem_history():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM problem_history

    ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows



def get_marketing_history():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM marketing_history

    ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_business_plan_history():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM business_plan_history

    ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def save_memory(category, content):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO ai_memory(
        category,
        content
    )

    VALUES(?,?)

    """,(category,content))

    conn.commit()

    conn.close()



def get_memory():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT category, content

    FROM ai_memory

    ORDER BY id DESC

    LIMIT 15

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


