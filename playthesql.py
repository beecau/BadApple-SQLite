import sqlite3
import time

conn = sqlite3.connect("greatapple.db")

pure_sql_payload = """
    WITH RECURSIVE frame_sequence(id) AS (
        SELECT 0
        UNION ALL
        SELECT id + 1 
        FROM frame_sequence 
        WHERE id < (SELECT MAX(frame_id) FROM bad_apple)
    )
    SELECT b.frame_data 
    FROM frame_sequence f 
    JOIN bad_apple b ON f.id = b.frame_id;
"""

print("\033[2J", end="")
start_time = time.time()
#no comments except this
for i, (frame_text,) in enumerate(conn.execute(pure_sql_payload)):
    print("\033[H" + frame_text, end="")
    
    target_time = start_time + (i / 30.0)
    sleep_duration = target_time - time.time()
    if sleep_duration > 0:
        time.sleep(sleep_duration)

conn.close()
