from database.db import MySQLDatabase
from repository.mahasiswa import MahasiswaRepo
from logic.mahasiswa import MahasiswaLogic
from entity.mahasiswa import MahasiswaEntity
import config

# Configuration
mysql_config = {
    "host": config.DB_HOST,
    "user": config.DB_USER,
    "password": config.DB_PASSWORD,
    "database": config.DB_DATABASE,
}

# Initialization
mysql_db = MySQLDatabase(**mysql_config)
mhs_repo = MahasiswaRepo(db=mysql_db)
mhs_logic = MahasiswaLogic(repo=mhs_repo)

# Usage
mhs = [
    MahasiswaEntity("1106050", "Gandana", "Garut"),
    MahasiswaEntity("1106051", "Haris", "Garut"),
    MahasiswaEntity("1106053", "Imam", "Garut"),
    MahasiswaEntity("1106069", "Robi", "Garut"),
    ]
#mhs_logic.creates(mhs)
#mhs_logic.delete("1106050")

mhs_logic.update("1106051","Tiara","Jepang",)