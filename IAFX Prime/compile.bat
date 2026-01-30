@echo off
"C:\Program Files\Trinota Markets MetaTrader 5 Terminal\MetaEditor64.exe" /compile:"C:\Users\jp\AppData\Roaming\MetaQuotes\Terminal\80B36EDEA062B4F58188D1BC3831473F\MQL5\Experts\IAFX Prime v7.mq5" /log
timeout /t 2 >nul
dir "IAFX Prime v7.ex5"
