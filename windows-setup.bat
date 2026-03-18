@echo off
echo Starting setup...

:: ----------------------------
:: 1. Download SWI-Prolog
:: ----------------------------
echo Downloading SWI-Prolog...

powershell -Command "Invoke-WebRequest -Uri https://www.swi-prolog.org/download/stable/bin/swipl-9.2.4-1.x64.exe -OutFile %TEMP%\swipl_installer.exe"

:: ----------------------------
:: 2. Install SWI-Prolog
:: ----------------------------
echo Installing SWI-Prolog...
start /wait %TEMP%\swipl_installer.exe /SILENT

:: ----------------------------
:: 3. Set Environment Variables
:: ----------------------------
echo Setting environment variables...

setx SWI_HOME_DIR "C:\Program Files\swipl" /M

setx PATH "%PATH%;C:\Program Files\swipl\bin" /M

:: ----------------------------
:: 4. Install pyswip
:: ----------------------------
echo Installing pyswip...
pip install pyswip

echo Setup complete!
echo Please restart your terminal.
pause