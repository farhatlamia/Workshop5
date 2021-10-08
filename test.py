import os
import glob
import xml.etree.ElementTree as ET
import csv

#declearing repository path
path = '/Users/USER/Downloads/FARMING_ANDROID_REPOS'

#parsing all directory
print("All Directories:")
arr = os.listdir(path)
print(arr)

#parsing all directory and subdirectory to find AndroidManifest.xml file
print("AndroidManifest.xml files")
files = glob.glob(path + '/**/AndroidManifest.xml', recursive=True)
print(files)

#line count function using path
def line_count(path):
    count = 0
    with open(path) as lines:
        for count, l in enumerate(lines, start=1):
            pass
    return count

print("xml files line count")
line_list = []
for n in files:
    line_list.append(line_count(n))
print(line_list)

#danger permission list
Permission = ["read_calendar", "write_calendar", "camera", "read_contacts", "write_contacts", "get_accounts", "access_fine_location", "access_coarse_location", "record_audio", "read_phone_state", "read_phone_numbers", "call_phone", "answer_phone_calls", "read_call_log", "write_call_log", "process_outgoing_calls", "add_voicemail", "use_sip", "body_sensors", "send_sms", "receive_sms", "read_sms", "receive_wap_push", "receive_mms", "read_external_storage", "write_external_storage"]

#case sencitivity
Permission1 = []
for i in range(len(Permission)):
    Permission1.append( "android.permission." + Permission[i].upper())
#print(Permission1)

print("Danger Permission in xml files")
for n in files:
    for j in range(len(Permission1)):
        with open(n) as f:
            if Permission1[j] in f.read():
                print(n + ',  ' + Permission1[j])


#print("java files")
files1 = glob.glob(path + '/**/*.java', recursive=True)
#print(files1)
#print(len(files1)) = 716

print("Java files and number of lines")
count = 0
for m in files1:
    with open(m, encoding="utf8") as f:
        for line in f:
            count += 1
        print(m + ", " + str(count))
        count = 0

print("Dangerous Permission in java files")
#case sencitivity
Permission2 = []
for i in range(len(Permission)):
    Permission2.append( "Manifest.permission." + Permission[i].upper())
#print(Permission2)

for m in files1:
    for k in range(len(Permission2)):
        with open(m,  encoding="utf8") as f:
            if Permission2[k] in f.read():
                print(n + ',  ' + Permission2[k])


header = ['Directory', 'Full_Path_To_File', 'Lines_Of', 'Code,Dangerous_Permission_Name']
with open('/Users/USER/PycharmProjects/Test-Task/venv/output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)


