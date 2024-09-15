@echo off
rem Change directory to the parent directory
cd ..\

cd .
rem Extract version information
for /f "delims=" %%i in ('python .\windows\get_version.py') do set VERSION=%%i

rem Copy the spec file
copy .\windows\autoUpdater.spec

rem Build the executable with PyInstaller
pyinstaller -y --clean autoUpdater.spec

rem Delete the spec file
del autoUpdater.spec

rem Optionally, use the version information here
echo Version Information: %VERSION%
