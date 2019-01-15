#Prequisites
#Download plink and put it in same directory as script https://the.earth.li/~sgtatham/putty/latest/w32/plink.exe
#VMware PowerCLI 6 or greater.

Add-PSSnapin vmware*
Start-Transcript .\Powerclilogging.log
$username = 'administrator@vsphere.local' #change this field to customer's vCenter Username.
$passwd = 'VMware1!' #change this field to customer's vCenter password.

####################vCenter IP addresses,multiple IPs if it is multi-site############
Connect-VIServer -Server 192.168.110.20 -Protocol https -User $username -Password $passwd
Connect-VIServer -Server 192.168.210.20 -Protocol https -User $username -Password $passwd
#####################################################################################

Get-VMHostNetworkAdapter | Where-Object {$_.Name -eq "vmk0"} #####Considering vmk0 is Management kernal port.
Get-VMHostNetworkAdapter | Where-Object {$_.Name -eq "vmk0"} > .\mgmtinterfaces.txt
Get-Content .\mgmtinterfaces.txt | %{ $_.Split(' ')[15]; }
Get-Content .\mgmtinterfaces.txt | %{ $_.Split(' ')[15]; } > .\iplist.txt
(Get-Content iplist.txt) | Where-Object {$_.trim() -ne "" } | set-content iplist.txt

$root = "root"  #HOST login ID
$Passwd = "VMware1!" # Host password
$cmd1 = "/etc/init.d/vShield-Stateful-Firewall status" #Check the status of vsfwd service, change this if you want to restart any other service.
$cmd2 = "/etc/init.d/vShield-Stateful-Firewall start"  #command to restart the service, change accordingly.
$notrunning = "vShield-Stateful-Firewall is not running" #example output if vsfwd isn't running change it as per required service.
$plink = ".\plink.exe"
$remoteCommand1 = '"' + $cmd1 + '"'
$remoteCommand2 = '"' + $cmd2 + '"'
$iplist = Get-Content .\iplist.txt
foreach ($esx in $iplist) {
Connect-VIServer $esx -User $root -Password $Passwd
#Write-Host -Object "Checking ssh services on $esx" -ForegroundColor Green
$sshstatus= Get-VMHostService -VMHost $esx| where {$psitem.key -eq "tsm-ssh"}
    if ($sshstatus.Running -eq $False)
    {
    Write-Host -Object "Starting ssh services on $esx" -ForegroundColor Green
    Get-VMHostService | where {$psitem.key -eq "tsm-ssh"} | Start-VMHostService
    }
Write-Host -Object "Checking vsfwd status on $esx" -ForegroundColor Yellow
$service_status = $plink + " " + "-ssh" + " " + $root + "@" + $esx + " " + "-pw" + " " + $Passwd + " " + $remoteCommand1
$service_status_output = Invoke-Expression -command $service_status
#$service_status_output
if ($service_status_output -eq $notrunning){
Write-Host -Object "Starting vsfwd service on $esx" -ForegroundColor Green
$start_service = $plink + " " + "-ssh" + " " + $root + "@" + $esx + " " + "-pw" + " " + $Passwd + " " + $remoteCommand2
$output = Invoke-Expression -command $start_service
$output
}
else {
    Write-Host -Object "vsfwd service is already RUNNING on $esx" -ForegroundColor Red
}
}
