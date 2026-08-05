import configparser
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent.parent

"""#Originally intended to import Error
if str(base_dir) not in sys.path:
    sys.path.insert(0, str(base_dir))

from library.Error import Error_List
"""

def read_sql_user_data() -> tuple[str,str,str,str]:
    sql_config_path = base_dir / "config" / "SQL_Config.ini"
    sql_config = configparser.ConfigParser()

    sql_config.read(str(sql_config_path),encoding="utf-8")
    sql_user = sql_config.get("SQL_Setting","User")
    sql_password = sql_config.get("SQL_Setting","Password")
    sql_host = sql_config.get("SQL_Setting", "Host")
    sql_database = sql_config.get("SQL_Setting", "Database")

    return sql_user, sql_password, sql_host, sql_database

"""
# Normal open txt Example
def read_sql_user_data1():
    sql_config_path = base_dir / "config" / "SQL_Config.ini"

    with open(str(sql_config_path), "r") as f:
        print(f.read())
"""