from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
import os,zipfile

def retrieve_file_paths(dirName):
  filePaths = []
  for root, directories, files in os.walk(dirName):
    for filename in files:
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)
  return filePaths

def zipFolder(dir_name):
  filePaths = retrieve_file_paths(dir_name)
  zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
  with zip_file:
    for file in filePaths:
      zip_file.write(file)

def deleteExistingFile(fileName,folderid):
    fileList = drive.ListFile({'q': "'{fid}' in parents and trashed=false".format(fid=folderid)}).GetList()
    for file in fileList:
        if(file['title'] == fileName):
            print ("Deleting {f} from gDrive".format(f=fileName))
            file.Delete()
            print ("Deleted {f} from gDrive".format(f=fileName))

def uploadFile(fileName,fid,path):
    deleteExistingFile(fileName,fid)
    file = drive.CreateFile({'parents': [{'id': fid}],
                                        'title': fileName})
    file.SetContentFile(os.path.join(path, fileName))
    file.Upload()
    file = None

def createRemoteFolder(folder_name, parent_folder_id = None):
        folder_metadata = {
        'title': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [{"kind": "drive#fileLink", "id": parent_folder_id}]
        }
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        return folder['id']

def recursiveFolder(directoryName,directoryPath,remoteDirParentId):
    currentFolderId = createRemoteFolder(directoryName,remoteDirParentId)
    for file in os.listdir(directoryPath):
        path = directoryPath + "\\" + file
        if(os.path.isdir(path)):
            recursiveFolder(file,path,currentFolderId)
        else:
            print ("uploading {f} from {p} to gDrive".format(f=file,p=path))
            uploadFile(file,currentFolderId,directoryPath)
            print ("uploaded {f} from {p} to gDrive".format(f=file,p=path))

def uploadZip(path,fid,zipFileName="AndroidStudioProjects"):
    zipExt = ".zip"
    print ("creating zip file")
    zipFolder(path)
    root_index = len(path) - len(zipFileName)
    root_path_for_zipped_file = path[0:root_index]
    print ("uploading zip file...")
    uploadFile(zipFileName+zipExt,fid,root_path_for_zipped_file)  
    print ("uploaded")
    print ("deleting local zip file...")
    os.remove( root_path_for_zipped_file + "\\" + zipFileName + zipExt )
    print ("deleted")

def saveData(path,folderName,fileName):
    folders = drive.ListFile(
            {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    i = 0
    if folders[0]['title'] == folderName:
        Fpath = path + "\\" + fileName
        if(i == 0 and path == dataPath[1]):
            uploadZip( path,folders[0]['id'])
            i = 1
        else:
            if(os.path.isdir(Fpath) and (not(fileName == fileNameInGdrive[2])) ):
                print(fileName)
                recursiveFolder(fileName,path+"\\"+fileName,folders[0]['id'])
            if(not(os.path.isdir(Fpath))):
                print ("uploading {f} from {p} to gDrive".format(f=fileName,p=path))
                uploadFile(fileName,folders[0]['id'],path)
                print ("uploaded {f} from {p} to gDrive".format(f=fileName,p=path))

dataTostore = [ "ui","AndroidStudioProjects","hp","main" ]
fileNameInGdrive = [ "ui","asp","java","asp" ]

dataPath = [ r"D:\OK\Mechanical Engg\udemy\Norton\ui",r"C:\Users\Ashish\AndroidStudioProjects",
    r"C:\Users\Ashish\AndroidStudioProjects\hp\app\src\main\java\com\example\hp",r"C:\Users\Ashish\AndroidStudioProjects\hp\app\src\main"]
dataStoreConsent = [ "n","n","n","n" ]
for i in range(0,len(dataTostore)):
    ans = input("Upload " + dataTostore[i] + " files? y/n: ")
    dataStoreConsent[i] = ans
    
os.system("start /B start cmd.exe @cmd /k clickChrome.bat")
gauth = GoogleAuth() 
gauth.LocalWebserverAuth()	 
drive = GoogleDrive(gauth) 

for i in range(0,len(dataTostore)):
    if(dataStoreConsent[i] == "y"):
        if(i != 2):
            print ("Starting upload procedure: {f}".format(f=fileNameInGdrive[i]))
            for fileName in os.listdir(dataPath[i]):
                saveData(dataPath[i] , fileNameInGdrive[i] , fileName)
