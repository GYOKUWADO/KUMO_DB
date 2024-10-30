@ECHO OFF
TITLE BlockChainHash
IF "%1"=="" GOTO :HELP0
IF "%1"=="/s" GOTO :ZERO
IF NOT "%1"=="" GOTO :ONE
GOTO :EOF

:HELP0
echo This Programs is Sign to ./Product_IMG.json file 
ECHO SIGN.BAT [Seed]
ECHO SIGN.BAT /s
echo ##############
echo [Seed] 署名を検証(Sign.txtと比較してください。)
echo /s     SEEDを入力してSign.txtに署名
GOTO :EOF

:ZERO

CALL SET_SEED.bat
node md5sign ./Product_IMG.json %SEED% > Sign.txt
set SEED=
GOTO :EOF

:ONE
node md5sign ./Product_IMG.json %1
GOTO :EOF