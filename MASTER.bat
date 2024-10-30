@echo off

TITLE GoogleSearh in cmd
IF "%1"=="" GOTO :HELP
IF "%1"=="/a" GOTO START1
IF "%1"=="/b" GOTO START5
IF "%1"=="/i" GOTO START4
IF "%1"=="/r" GOTO START3
IF "%1"=="/s" GOTO START2

IF NOT "%1"=="" GOTO START0
GOTO :NULL

:HELP
echo /a レコードの追加
echo /b SIGN.BATでProduct_IMG.jsonに署名(Sign.txtに出力)
echo /i イメージの検索
echo /r ランクの検索
echo /s 在庫の修正
GOTO :NULL

:START1
set /p IMG="Product_IMGフォルダのイメージのファイル名を入力してください。:"
node Md5Sign.js Product_IMG\%IMG% > TMP.MD5SBH
FOR /F "tokens=1,2" %%i in (TMP.MD5SBH) do IF %%i==MD5SimpleBlockchainHash: set MD5SBH=%%j
REM echo %MD5SBH%
python DB_Add.py %MD5SBH%
GOTO :NULL

:START2
python stock_update.py
GOTO :NULL

:START3
python PRSearch.py
GOTO :NULL

:START4
python Psearch.py
GOTO :NULL

:START5
SIGN.BAT
GOTO :NULL