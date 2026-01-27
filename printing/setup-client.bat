@echo off
echo 🖨️  Setting up Print Client for Windows...

REM Install required Python packages
echo 📦 Installing required packages...
pip install requests

REM Get the script directory
set SCRIPT_DIR=%~dp0

REM Create printfile.bat command wrapper
echo 📝 Creating printfile command...
(
echo @echo off
echo if "%%~1"=="" ^(
echo     echo Usage: printfile ^<filename^>
echo     exit /b 1
echo ^)
echo python "%SCRIPT_DIR%rpc-client.py" "%%~1"
) > "%SCRIPT_DIR%printfile.bat"

echo.
echo ✅ Setup complete!
echo.
echo You can now use: printfile ^<filename^>
echo.
echo Example:
echo   printfile solution.cpp
echo.
echo Print jobs will be sent to: http://192.168.17.111:9000/
echo.
echo Note: Add %SCRIPT_DIR% to your PATH to use 'printfile' from anywhere.
echo Or run: setx PATH "%%PATH%%;%SCRIPT_DIR%"
pause
