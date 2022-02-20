#! /usr/bin/env python3
import sys
import os
import platform
import sqlite3
from .os_provider import OSProvider
from .sql_ddl import DDL
from config import CFG
from .app_provider import db


class device(db.Model):
    uuid = db.Column(
        db.String(36),
        unique=True,
        primary_key=True
    )
    serial_number = db.Column(
        db.String(256),
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return f"{self.uuid}"


# db.create_all()
#d = device(
#    uuid="a636a6bd-eca4-43e0-9180-ce6f904d8a171",
#    serial_number="11204"
#)
#db.session.add(d)
#db.session.commit()


class DBProvider:
    ROOT_DIR = ".ppo"
    DB_NAME = "database.sql"

    def __init__(self):
        self._os = OSProvider()
        self.__init_database()
        self._conn = None

    def __del__(self):
        if self._conn is not None:
            self._conn.close()

    def __init_database(self):
        if not os.path.isfile(CFG["database"]["path"]):
            self._conn = sqlite3.connect(CFG["database"]["path"])
            self._conn.executescript(DDL)


database_provider = DBProvider()


__all__ = ["DBProvider", "database_provider"]
