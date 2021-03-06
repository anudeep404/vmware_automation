$iplist = Get-Content .\iplist.txt

$root = "root"
$passwd = "VMware1!"

foreach ($esx in $iplist) {
Connect-VIServer $esx -User $root -Password $passwd
Write-Host -Object "Stopping ssh services on $esx" -ForegroundColor Green
$sshstatus= Get-VMHostService -VMHost $esx| where {$psitem.key -eq "tsm-ssh"}
if ($sshstatus.Running -eq $True) {
Get-VMHostService | where {$psitem.key -eq "tsm-ssh"} | Stop-VMHostService }
}
