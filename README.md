"# vmware_automation"
There are two ways to complete the task.

Using PowerCLI (File extension .ps1)
Using Python    (File extension .py)
Note: Use Python script ONLY if you have a list of hosts saved in the iplist.txt file and SSH is enabled on all the hosts.



Steps to run PowerCLI script:

Make sure the PowerCLI script and plink (tool, download it from https://the.earth.li/~sgtatham/putty/latest/w32/plink.exe) are in the same directory(referred as script directory here on).
Open PowerCLI and navigate to the script directory.
Run 1_alpha.ps1
This would log in vCenter, get the list of all the host management IPs, considering mgmt kernel port is vmk0.
Enable SSH on them.
Check for respective service(in this case, VSFWD)
Start VSFWD if it is STOPPED on any host.
Once the task is complete, you may have to disable SSH on all the hosts, execute 3_delta.ps1
Steps to run Python script:

For any reason, if the customer doesn't have PowerCLI and would like to use Python.
Run the script 2_omega.py
Tested with:

Python 3.5 or 3.7
VMware vSphere PowerCLI 6.3 Release 1 build 3737840
VMware ESXi 6.5.0 build-4887370
vCenter 6.5 Build-5178943
