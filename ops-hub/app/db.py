import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "hub.sqlite3"

SCHEMA = """
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    business_line TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'New',
    next_action TEXT,
    deadline TEXT,                 -- ISO date YYYY-MM-DD, nullable
    estimated_value REAL,
    notes TEXT,
    contact_name TEXT,
    contact_phone TEXT,
    contact_email TEXT,
    au_state TEXT,                 -- NSW/VIC/QLD/... nullable, relevant to several lines
    source TEXT DEFAULT 'manual',  -- manual | webhook | referral | import
    extra_json TEXT DEFAULT '{}',  -- business-line-specific fields, see app/config.py
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_leads_business_line ON leads(business_line);
CREATE INDEX IF NOT EXISTS idx_leads_deadline ON leads(deadline);
CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);

CREATE TABLE IF NOT EXISTS webhook_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    received_at TEXT NOT NULL DEFAULT (datetime('now')),
    source TEXT,
    payload_json TEXT,
    lead_id INTEGER,
    note TEXT
);
"""


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_connection()
    try:
        conn.executescript(SCHEMA)
        conn.commit()
    finally:
        conn.close()
