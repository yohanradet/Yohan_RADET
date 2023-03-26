#!/bin/bash


while true; do

price=$(curl -s "https://fr.finance.yahoo.com/quote/EURUSD%3DX?p=EURUSD%3DX" | grep -o 'data-test="qsp-price" data-fie>


if [ -n "$price" ]; then

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

echo "$TIMESTAMP,$price" >> historical_data.csv

sleep 60

else

sleep 5

fi

done
