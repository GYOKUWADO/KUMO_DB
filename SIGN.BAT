@ECHO OFF
TITLE BlockChainHash
IF "%1"=="" GOTO :HELP0
IF "%1"=="/s" GOTO :ZERO
IF "%1"=="/v" GOTO :ONE
GOTO :EOF

:HELP0
echo This Programs is Sign to ./Product_IMG.json file 
ECHO SIGN.BAT /s
ECHO SIGN.BAT /v
echo ##############
echo /s SEEDを入力してSign.txtに署名
echo /v ./Product_IMG.jsonの検証(Sign.txtと比較してください。)
GOTO :EOF

:ZERO

CALL SET_SEED.bat
node md5sign ./Product_IMG.json %SEED% > Sign.txt
set SEED=
GOTO :EOF

:ONE
CALL SET_SEED.bat
node md5sign ./Product_IMG.json %SEED%
GOTO :EOF