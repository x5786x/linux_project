#!/bin/bash

Ping()
{
	
	for i in {1...3};do
		ping -c 1 -W 1 nginx1.server >& /dev/null # 利用ping傳送ICMP回應請求
		if [ $? -eq 0 ];then # 若有回應則回傳1
			exit 0 
		fi
	done
}

Ping
exit 1 # 無回應回傳0
