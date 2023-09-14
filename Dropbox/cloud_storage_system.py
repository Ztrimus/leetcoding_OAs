'''
Author: Saurabh Zinjad
Created Date: Sunday, September 10th 2023, 6:22:55 pm
Filename: cloud_storage_system.py
Path: /home/saurabh/AAA/Focusing/Coding/intern-assessment-2023/Dropbox

Copyright (c) 2023 Ztrimus
'''



class CloudStorageSystem:
    def __init__(self):
        self.storage = {}
    
    def addFile(self, file: str, size: str):
        if file in self.storage:
            return "false"
        else:
            self.storage[file] = int(size)
            return "true"
        
    def getFileSize(self, file: str):
        if file in self.storage:
            return str(self.storage[file])
        return ''       
    
    def deleteFile(self, file: str):
        if file in self.storage:
            return self.storage.pop(file)
        else:
            return ''
    
    def getNLargest(self, file: str, n: int):
        print()
        pass
        
if __name__ == '__main__':
    # queries = [ 
    #     ["ADD_FILE", "/dir1/dir2/file.txt", "10"],
    #     ["ADD_FILE", "/dir1/dir2/file.txt", "5"],
    #     ["GET_FILE_SIZE", "/dir1/dir2/file.txt"], 
    #     ["DELETE_FILE", "/non-existing.file"], 
    #     ["DELETE_FILE", "/dir1/dir2/file.txt"],
    #     ["GET_FILE_SIZE", "/not-existing.file"]
    #     ]

    queries = [
        ["ADD_FILE", "/dir/file1.txt", "5"],
        ["ADD_FILE", "/dir/file2", "20"],
        ["ADD_FILE", "/dir/deeper/file3.mov", "9"],
        ["GET_N_LARGEST", "/dir", "2"],
        ["GET_N_LARGEST", "/dir/file", "3"],
        ["GET_N_LARGEST", "/another_dir", "file.txt"],
        ["ADD_FILE", "/big_file.mp4", "20"],
        ["GET_N_LARGEST", "/", "2"]
    ]
    storageObj = CloudStorageSystem()

    for query in queries:
        if query[0] == 'ADD_FILE':
            print(storageObj.addFile(query[1], query[2]))
        elif query[0] == 'GET_FILE_SIZE':
            print(storageObj.getFileSize(query[1]))
        elif query[0] == 'DELETE_FILE':
            print(storageObj.deleteFile(query[1]))
        elif query[0] == 'GET_N_LARGEST':
            print(storageObj.getNLargest(query[1], query[2]))