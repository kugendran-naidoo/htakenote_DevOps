
# Environment Setup 

printf "\nCheck \"python3\" available ...\n"

{
python3 >/dev/null 2>&1 <<_@@
print("Snafu\n")
_@@
} || 
{
printf "\"python3\" is missing - install it first!\n"
exit 5
}

printf "\nCheck \"virtualenv\" installed ...\n"
{
pip3 list |
grep virtualenv >/dev/null 2>&1 
} || 
{
printf "\"virtualenv\" is missing - pip3 install it first!\n"
exit 5
}

printf "\nSetup \"env\" virtual environment ...\n"
virtualenv venv ||
{
printf "Failed to create virtualenv \"env\" - quiting\n"
exit 5
}

printf "From the repo root, run \"source venv/bin/activate\"\n"
printf "Run locally cd src: python app.py\n"
printf "Start browser: http://127.0.0.1:5000/\n"

printf "Remember: pip3 install -r requirements.txt\n"
printf "pip3 install sqlalchemy\n"
printf "Then pip3 freeze> requirements.txt\n"
printf "export PYTHONPATH=src\n"
printf "pytest -v tests/test_app.py\n"
printf "Basics working: https://www.youtube.com/watch?v=WTofttoD2xg\n"

printf "Install Heroku CLI\n"
printf "Run: heroku login\n"
printf "Run: git remote -v\n"
# initialize credentials
printf "Run: git push heroku\n" 
# see url
# https://htakenote.herokuapp.com/
printf "Run: heroku apps:info\n" 
# generate a new APP token - update Bitbucket Repository Variables
# HEROKU_APP_TOKEN
printf "Run: heroku auth:token\n" 

printf "Create Procfile and runtime.txt\n"
printf "Finish Heroku setup\n"
