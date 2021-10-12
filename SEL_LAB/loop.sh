#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT



while true
do
	echo "NEW ..............."
	timeout 5m python3 capability_firefox_test.py
done
