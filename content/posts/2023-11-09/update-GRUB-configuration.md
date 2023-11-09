---
title: "Update GRUB Configuration"
date: 2023-11-09T13:47:05-05:00
tags: ['Ubuntu', 'Linux']
draft: false
---

## Edit GURB configuration file
```
sudo nano /etc/default/grub
```

## Change the Timeout
```
GRUB_TIMEOUT=5
```

## Update GRUB
```
sudo update-grub
```

## Reboot
```
sudo reboot
```