# GreatApple.db

A lightweight, portable terminal-based Bad Apple!! player powered entirely by a single SQLite database file. No heavy frameworks, no video servers, and no application-side loops—just relational algebra, recursive SQL, and raw terminal output.

---

## How It Works

1. video_to_sqlite.py: Uses ffmpeg to process your .mp4 video, downscaling frames into a 64x24 ASCII grayscale grid and packing them sequentially into greatapple.db.
2. playthesql.py: Leverages a Recursive Common Table Expression (CTE) directly inside SQLite to handle all playback sequence logic natively, while Python acts purely as a terminal conduit streaming frames at ~30 FPS.

---

## Requirements

* Python 3.x (uses the built-in sqlite3 module—no external packages required)
* FFmpeg (required for generating the database from an .mp4 file)

---

## Usage

1. Place your source video as greatapple.mp4 in the project directory.
2. Generate the SQLite database:
python video_to_sqlite.py
3. Run the player to stream the recursive SQL query:
python playthesql.py

---

## License

This project is open-source and available under the terms of the MIT License (LICENSE).
