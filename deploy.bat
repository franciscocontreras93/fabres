@echo off
echo =================================================
echo Updating and deploying the application to heroku 
echo =================================================
git add .
git commit -m 'auto update'
git push origin main
echo ==================================================
echo               Updated Github repo
echo ==================================================
echo               Updating Heroku app
echo ==================================================
git push heroku main
echo ==================================================
echo                Process Finished
echo ==================================================
start https://fabres2.herokuapp.com

