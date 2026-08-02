import sqlite3

conn = sqlite3.connect("business_ai.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS idea_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    business_idea TEXT,

    business_type TEXT,

    budget TEXT,

    extra_info TEXT,

    ai_response TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS problem_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    problem TEXT,

    business_type TEXT,

    budget TEXT,

    extra_info TEXT,

    ai_response TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS marketing_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    business_idea TEXT,

    business_type TEXT,

    marketing_budget TEXT,

    target_audience TEXT,

    business_goals TEXT,

    extra_info TEXT,

    user_marketing_idea TEXT,

    ai_response TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")



cursor.execute("""
CREATE TABLE IF NOT EXISTS business_plan_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    additional_information TEXT,

    ai_response TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")




cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_memory(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    category TEXT,

    content TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")


conn.commit()
conn.close()