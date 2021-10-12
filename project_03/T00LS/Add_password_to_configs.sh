#!/bin/bash


files=$(ls NORD_CONFIG/ovpn_udp)
for i in $files
do
	echo  $i
	sed -i 's/auth-user-pass/auth-user-pass nord_pass.txt/' NORD_CONFIG/ovpn_udp/$i
	
done
