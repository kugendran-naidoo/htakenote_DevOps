# DB Setup 
printf "Creating DB ...\n"

python3<<_@@
import sys
sys.path.append("src")
from app import db
db.create_all()
exit
_@@
