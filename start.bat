@echo off
echo Starting Movie Tracking System...
echo.
echo Step 1: Starting server (this window)
start "Movie Server" cmd /k "python server.py"
echo.
echo Step 2: Starting client (new window)
timeout /t 5 /nobreak > nul
start "Movie Client" cmd /k "python client.py"
echo.
echo Started! Use the client window to interact with the system.
echo Type 'help' in the client window to see available commands.
