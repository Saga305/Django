@echo off
REM This script navigates to the django_project directory, runs the Django development server,
REM and opens a specific page in Google Chrome

REM Navigate to the project directory
cd /d E:\django_project\my_project\Django

REM Run the Django development server
start python3.12.exe .\manage.py runserver

REM Give the server a few seconds to start
timeout /t 10 /nobreak

REM Open the specified URL in Google Chrome
start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://127.0.0.1:8000/rotate
start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://127.0.0.1:8000/ring
start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://127.0.0.1:8000/color
start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://127.0.0.1:8000/ball
start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://127.0.0.1:8000/stop_watch
start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://127.0.0.1:8000/bar
REM End of script
echo Django development server is running and the page is opened in Chrome.
pause
