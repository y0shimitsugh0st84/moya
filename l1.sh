#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT



while true
do
	echo "NEW ..............."
	python3 ouo_last_jeday3.py
done
