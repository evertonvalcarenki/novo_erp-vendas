@echo off
echo 🔧 Gerando executável .exe...
pyinstaller --onefile --windowed --add-data "templates;templates" --icon=icon.ico inicio.py
echo Pronto! O executável está em: dist\inicio.exe
pause