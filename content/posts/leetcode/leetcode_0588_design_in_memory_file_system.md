---
title: 588. Design In-Memory File System
date: '2022-04-08'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 0588. Design In-Memory File System
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={588}/>
 
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.

List ls(String path)If path is a file path, returns a list that only contains this file's name.If path is a directory path, returns the list of file and directory names in this directory.The answer should in lexicographic order.

void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.

void addContentToFile(String filePath, String content)

If filePath does not exist, creates that file containing given content.

If filePath already exists, appends the given content to original content.

String readContentFromFile(String filePath) Returns the content in the file at filePath.

 > Example 1:

 > Input
 > ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
 > [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
 > Output
 > [null, [], null, null, ["a"], "hello"]

 > Explanation
 > FileSystem fileSystem <TeX>=</TeX> new FileSystem();
 > fileSystem.ls("/");                         // return []
 > fileSystem.mkdir("/a/b/c");
 > fileSystem.addContentToFile("/a/b/c/d", "hello");
 > fileSystem.ls("/");                         // return ["a"]
 > fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"

**Constraints:**

 > 1 <TeX>\leq</TeX> path.length, filePath.length <TeX>\leq</TeX> 100

 > path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".

 > You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.

 > You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.

 > 1 <TeX>\leq</TeX> content.length <TeX>\leq</TeX> 50

 > At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.

## Solution
Solution: We will use Trie to solve this problem. Each node will store a folder name or file name. The file content will also save in the node. 
### Python
```python
class TrieNode:
    def __init__(self, name):
        self.name = name
        self.isFile = False
        self.fileContent = ""
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")
    def insert(self, path, isFile):
        node = self.root
        folders = path[1:].split("/")
        for i in range(len(folders)):
            if folders[i] in node.children:
                node = node.children[folders[i]]
            else:
                new_node = TrieNode(folders[i])
                node.children[folders[i]] = new_node
                node = new_node
        if isFile:
            node.isFile = True
        return node
    def query(self, path):
        node = self.root
        folders = path[1:].split("/")
        for i in range(len(folders)):
            if folders[i] in node.children:
                node = node.children[folders[i]]
        if node.isFile:
            return [node.name]
        filesFolders = list(node.children.keys())
        filesFolders.sort()
        return filesFolders
        
class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def ls(self, path: str) -> List[str]:
        #print("ls: {}".format(path))
        return self.trie.query(path)

    def mkdir(self, path: str) -> None:
        self.trie.insert(path, False)        

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.trie.insert(filePath, True)
        node.fileContent += content 

    def readContentFromFile(self, filePath: str) -> str:
        node = self.trie.insert(filePath, False)
        return node.fileContent
```
