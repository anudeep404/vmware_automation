#Finding ServerGUID
import os
import re

def chdir():
        new_dir=input("Please enter the new directory:")
        os.chdir(new_dir)
chdir()

file = input("Enter the filename:")
Agency_list=[]
Agent_list=[]
def eam_analysis():
        file_content = open(file).read()
        First_Line = open(file).readline()
        server_guid = First_Line.split(',')[2]
        print('\nThe server GUID is:\n')
        print(server_guid)
        pattern = r'EsxAgentManager:agency['
        pattern1 = r'agent['
        pattern2 = r'host-'
        print('\nThe list of Agencies under the Server GUID are as follows:\n')
        for line in open(file):
                if pattern in line:
                        Agency = line.split(',')[2].split(':')[3]
                        print(Agency)
                        Agency_list.append(Agency)
        for Agency in Agency_list:
                print('##################################')
                print('\nThe Agents that are part of %s\n' %Agency)
                for line in open(file):
                        if Agency in line:
                                if pattern1 in line:
                                        Agent = line.split(',')[2].split(':')[3]
                                        print(Agent)
                                        Agent_list.append(Agent)
        print('##################################')
        print('##################################')
        for Agent in Agent_list:
                for line in open(file):
                        if Agent in line:
                                if pattern2 in line:
                                        HostID = line.split(',')[2].split(':')[3]
                                        print('\nThe host IDs of the Agent %s %s\n' % (Agent,HostID))
eam_analysis()

def main():
        chdir()
        eam_analysis()
main()

if __name__ == '__main__':
    main()
