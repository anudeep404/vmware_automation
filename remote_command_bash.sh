#!/bin/bash
sshpass -p 'VMware1!VMware1!' ssh -o StrictHostKeyChecking=no admin@192.168.110.190 "show status"
sshpass -p 'VMware1!VMware1!' ssh -o StrictHostKeyChecking=no admin@192.168.110.191 "show status"
sshpass -p 'VMware1!VMware1!' ssh -o StrictHostKeyChecking=no admin@192.168.110.192 "show status"
