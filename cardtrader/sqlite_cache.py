"""
The SQLiteCache module.

This module provides the following classes:

- SQLiteCache
"""
import json
import sqlite3
from datetime import date, timedelta
from typing import Any, Dict, Optional

from cardtrader import get_cache_root


class SQLiteCache:
    """
    The SQLiteCache object to cache search results from ComicVine.

    Args:
        path: Path to database.
        expiry: How long to keep cache results.

    Attributes:
        expiry (Optional[int]): How long to keep cache results.
        con (sqlite3.Connection): Database connection
        cur (sqlite3.Cursor): Database cursor
    """

    def __init__(
        self,
        path: str = get_cache_root() / "cache.sqlite",
        expiry: Optional[int] = 14,
    ):
        self.expiry = expiry
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS queries (query, response, expiry);")
        self.delete()

    def select(self, query: str) -> Dict[str, Any]:
        """
        Retrieve data from the cache database.

        Args:
            query: Search string

        Returns:
            Empty dict or select results.
        """
        if self.expiry:
            self.cur.execute(
                "SELECT response FROM queries WHERE query = ? and expiry > ?;",
                (query, date.today().isoformat()),
            )
        else:
            self.cur.execute("SELECT response FROM queries WHERE query = ?;", (query,))
        if results := self.cur.fetchone():
            return json.loads(results[0])
        return {}

    def insert(self, query: str, response: Dict[str, Any]):
        """
        Insert data into the cache database.

        Args:
            query: Search string
            response: Data to save
        """
        if self.expiry:
            expiry = date.today() + timedelta(days=self.expiry)
        else:
            expiry = date.today()
        self.cur.execute(
            "INSERT INTO queries (query, response, expiry) VALUES (?, ?, ?);",
            (query, json.dumps(response), expiry.isoformat()),
        )
        self.con.commit()

    def delete(self):
        """Remove all expired data from the cache database."""
        if not self.expiry:
            return
        self.cur.execute("DELETE FROM queries WHERE expiry < ?;", (date.today().isoformat(),))
        self.con.commit()
