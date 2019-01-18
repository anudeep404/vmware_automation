#Disclaimer: Please test this script in lab environment before testing on any production system.
Start-Transcript .\logging.txt
$root = "root"
$Passwd = "VMware1!"
$esxlist = Get-Content .\iplist.txt
$cmd = "net-vdr -l -R default+edge-11"

#Download plink from http://the.earth.li/~sgtatham/putty/0.63/x86/

$plink = "echo y | .\plink.exe"
$remoteCommand = '"' + $cmd + '"'

foreach ($esx in $esxlist) {
Connect-VIServer $esx -User $root -Password $Passwd
Write-Host -Object "starting ssh services on $esx" -ForegroundColor Green
$sshstatus= Get-VMHostService -VMHost $esx| where {$psitem.key -eq "tsm-ssh"}
if ($sshstatus.Running -eq $False) {
Get-VMHostService | where {$psitem.key -eq "tsm-ssh"} | Start-VMHostService }
Write-Host -Object "Executing Command on $esx" -ForegroundColor Green
$output = $plink + " " + "-ssh" + " " + $root + "@" + $esx + " " + "-pw" + " " + $Passwd + " " + $remoteCommand
$message = Invoke-Expression -command $output
$message
}
foreach ($esx in $esxlist) {
Connect-VIServer $esx -User $root -Password $Passwd
Write-Host -Object "Stopping ssh services on $esx" -ForegroundColor Green
$sshstatus= Get-VMHostService -VMHost $esx| where {$psitem.key -eq "tsm-ssh"}
if ($sshstatus.Running -eq $True) {
Get-VMHostService | where {$psitem.key -eq "tsm-ssh"} | Stop-VMHostService }
}
Stop-Transcript
Write-Host "Collected the route information from $esxlist and saved it at .\logging.txt" -ForegroundColor Yellow
