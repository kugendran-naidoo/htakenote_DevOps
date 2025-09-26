
printf "\nCreate Procfile => \"web gunicorn --pythonpath src app:app\"\n"
printf "\nCreate runtime.txt => \"python-3.9.4\"\n"

printf "\nSetup CI/CD Pipeline in Bitbucket\n"
printf "\nCheck valid Bitbucket repository variables\n"

printf "\nSetting up Heroku ... use unique global name\n"
heroku create htakenote

printf "Start Heroku console\n"
printf "heroku run bash\n"

printf "\nChecking Heroku git remote repositories\n"
git remote -v

printf "\nPushing to Heroku git - automatic build\n"
git push heroku master

printf "Restart Heroku Dyno - heroku ps:restart --app\n"

printf "Run heroku apps:info --app=\n"

printf "heroku apps:destroy htakenote --confirm htakenote\n"

printf "Run URL https://takenote.herokuapp.com/\n"
