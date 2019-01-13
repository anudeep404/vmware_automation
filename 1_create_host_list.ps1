#Start-Transcript .\Powerclilogging.txt
$username = 'administrator@vsphere.local'
$passwd = 'VMware1!'
Add-PSSnapin vmware*
Connect-VIServer -Server 192.168.110.20 -Protocol https -User $username -Password $passwd
Connect-VIServer -Server 192.168.210.20 -Protocol https -User 'administrator@vsphere.local' -Password 'VMware1!'
Get-VMHostNetworkAdapter | Where-Object {$_.Name -eq "vmk0"}
#Saving the output of the above command to a directory:
Get-VMHostNetworkAdapter | Where-Object {$_.Name -eq "vmk0"} > .\mgmtinterfaces.txt
#Filter the IP from the above Output
Get-Content .\mgmtinterfaces.txt | %{ $_.Split(' ')[15]; }
#Saves the IPs to a text file.
Get-Content .\mgmtinterfaces.txt | %{ $_.Split(' ')[15]; } > .\iplist.txt
(gc iplist.txt) | ? {$_.trim() -ne "" } | set-content iplist.txt
