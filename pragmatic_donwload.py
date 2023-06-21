import subprocess

def install(name):
    try:
        subprocess.call(['pip', 'install', name])
    except:
        subprocess.call(['pip3', 'install', name])



import io
import pickle

try:
    from googleapiclient.http import MediaIoBaseDownload
except ImportError:
    install('google-api-python-client')
    from googleapiclient.http import MediaIoBaseDownload


try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    install('google-auth-oauthlib')
    install('google-auth-httplib2')
    from google_auth_oauthlib.flow import InstalledAppFlow



from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from datetime import datetime
import os, time

def timestamp(date):
        return time.mktime(date.timetuple())

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

files_dir = {}

def process(filename):
    folder = ""
    working_on = 0.0
    total = 0
    file = open(filename)
    lines = file.readlines()
    for l in lines:

        if "folder" in l:
            folderName = l.split("folder:")[1].split("]")[0].split("\n")[0]
            if folderName not in files_dir:
                files_dir[folderName] = []
                folder = folderName

        if "https" in l and "id" in l:
            l = l.split("id=")[1].split("\n")[0]
            files_dir[folder].append(l)
            total = total + 1

    # Creating directories
    for key in files_dir:
        if "None" not in key:
            if not os.path.exists(key):
                os.makedirs(key)

    progress = "00.00"
    print ("Google Drive Downloader v2.0\n")
    print ("Files to download:", total)
    print ("Starting downloads ...\n")

    for key in files_dir:
        for l in files_dir[key]:
            file_id = l
            try:
                request = service.files().get_media(fileId=file_id)

                data = service.files().get(fileId=l, fields='*').execute()

                modtime = timestamp(datetime.strptime(data["modifiedTime"], '%Y-%m-%dT%H:%M:%S.%fZ'))
                #print(" ")
                #print("meta", data["modifiedTime"])

                fname = key + "/" + data['name']
                
                dodownload = not os.path.lexists(fname)
                if not dodownload:
                    modtimeondisk = os.path.getmtime(fname)
                    dodownload = modtimeondisk < modtime
                    if dodownload:
                        print("NEWER VERSION DETECTED")

                #modtimesource = os.path.getmtime(fh)
                #print("mod: ", modtimetarget, modtimesource)
                if dodownload:# or modtimetarget < modtimesource:
                    if "None" not in key:
                        fh = io.FileIO(os.path.join(key, data['name']), 'wb')
                    else:
                        fh = io.FileIO(os.path.join(key.split("/")[0], data['name']), 'wb')
                    print("[" + progress + "%] " + "Downlading: " + data['name'])

                    downloader = MediaIoBaseDownload(fh, request)
                    done = False
                    while done is False:
                        status, done = downloader.next_chunk()

                    os.utime(fname, (time.time(), modtime))

                else:
                    print("[" + progress + "%] " + "Skipping: " + data['name'])

            except Exception as e:
                print(e)

            working_on = working_on + 1
            val = round(float((working_on / total) * 100), 2)
            if val < 10:
                progress = "0{:0.2f}".format(val)
            else:
                progress = "{:0.2f}".format(val)



creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('drive', 'v3', credentials=creds)

for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        process(file)
        break

print ("[100.0%] Finished!\n\n\n")

try:
    input("All files are downloaded successfully! Press Enter to exit!")
except:
    pass
