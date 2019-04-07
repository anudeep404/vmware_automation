import os
def chdir():
        new_dir=input("Please enter the new directory:")
        os.chdir(new_dir)
chdir()
file = input("Enter the filename:")
Agency_list=[]
Agent_list=[]
pattern = r'EsxAgentManager:agency['
pattern1 = r'agent['
pattern2 = r'host-'
pattern3 = r'baseOvfEnvironment'
pattern4 = r'controlNicKeyToIp'
pattern5 = r'config'
pattern6 = r'isUpgrading'
pattern7 = r'wasUpgrading'
pattern8 = r'rebootHostAfterVibUninstall'
pattern9 = r'goalState'
def eam_analysis():
        file_content = open(file).read()
        First_Line = open(file).readline()
        server_guid = First_Line.split(',')[2]
        print('\nThe server GUID is:\n')
        print(server_guid)
        print('\nThe list of Agencies under the Server GUID are as follows:\n')
def Find_Agency(file_content_to_check):
    for line in open(file_content_to_check):
        if pattern in line:
            Agency = line.split(',')[2].split(':')[3]
                        print(Agency)
                        Agency_list.append(Agency)
        for Agency in Agency_list:
                print('###################################################################')
                print('#The Agents that are part of %s' %Agency)
                print('###################################################################')
                for line in open(file):
                        if Agency in line:
                                if pattern1 in line:
                                        Agent = line.split(',')[2].split(':')[3]
                                        print(Agent)
                                        Agent_list.append(Agent)
        print('#########################################')
        print('###Fetching the Host-ID for each Agent###')
        print('#########################################')
        for Agent in Agent_list:
                for line in open(file):
                        if Agent in line:
                                if pattern2 in line:
                                        HostID = line.split(',')[2].split(':')[3]
                                        print('%s %s' %(Agent,HostID))
        print('########################################')
        print('##Fetching the Data Key foe each Agent##')
        print('########################################')
        for Agent in Agent_list:
                for line in open(file):
                        if Agent in line:
                                if pattern3 in line:
                                        data_key = line.split(',')[2]
                                        print('%s %s' %(Agent,data_key))
        print('#################################################')
        print('##Fetching the ControlNicKeyToIp for each Agent##')
        print('#################################################')
        for Agent in Agent_list:
                for line in open(file):
                        if Agent in line:
                                if pattern4 in line:
                                        data_key = line.split(',')[2]
                                        print('%s %s' %(Agent,data_key))
        print('#################################################')
        print('########Fetching the config for each Agent#######')
        print('#################################################')
        for Agent in Agent_list:
                for line in open(file):
                        if Agent in line:
                                if pattern5 in line:
                                        data_key = line.split(',')[2]
                                        print('%s %s' %(Agent,data_key))
        print('#################################################')
        print('#####Fetching the isUpgrading for each Agent#####')
        print('#################################################')
        for Agent in Agent_list:
                for line in open(file):
                        if Agent in line:
                                if pattern6 in line:
                                        data_key = line.split(',')[2]
                                        print('%s %s' %(Agent,data_key))
        print('#################################################')
        print('####Fetching the wasUpgrading for each Agent#####')
        print('#################################################')
        for Agent in Agent_list:
                for line in open(file):
                        if Agent in line:
                                if pattern7 in line:
                                        data_key = line.split(',')[2]
                                        print('%s %s' %(Agent,data_key))
        print('#################################################')
        print('##Fetching if reboot is required for each Agent##')
        print('#################################################')
        for Agent in Agent_list:
                for line in open(file):
                        if Agent in line:
                                if pattern8 in line:
                                        data_key = line.split(',')[2]
                                        print('%s %s' %(Agent,data_key))
        print('#################################################')
        print('######Fetching if goalstate for each Agent#######')
        print('#################################################')
        for Agent in Agent_list:
                for line in open(file):
                        if Agent in line:
                                if pattern9 in line:
                                        data_key = line.split(',')[2]
                                        print('%s %s' %(Agent,data_key))
eam_analysis()

def main():
        chdir()
        eam_analysis()
main()

if __name__ == '__main__':
    main()
