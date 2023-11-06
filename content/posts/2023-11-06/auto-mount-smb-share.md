---
title: "Auto Mount Smb Share"
date: 2023-11-06T05:04:03-05:00
tags: ['ubuntu', 'SMB']
draft: false
---

## Install cifs-utils 
```
sudo apt-get update
sudo apt-get install cifs-utils
```

## Creae folder and mount
```
mkdir ~/smbshare
sudo mount -t cifs -o username=your_username,password=your_password //mycloudex2ultra.local/yyh/Audio /media/yyh/Audio
sudo mount -t cifs -o username=your_username,password=your_password //mycloudex2ultra.local/yyh/Book /media/yyh/Book
sudo mount -t cifs -o username=your_username,password=your_password //mycloudex2ultra.local/yyh/Photo /media/yyh/Photo
sudo mount -t cifs -o username=your_username,password=your_password //mycloudex2ultra.local/yyh/Video /media/yyh/Video
```

