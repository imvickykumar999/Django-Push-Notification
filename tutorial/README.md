
># `SCRCPY` : *Screen Share*
>
>![20240728_123218-COLLAGE](https://github.com/user-attachments/assets/ed47de53-b4b9-494a-ae39-095c3110c164)

    Step 1: Connect via USB

```bash
>>> adb usb
    restarting in USB mode

>>> adb tcpip 5555
    restarting in TCP mode port: 5555
```

    Step 2: Disconnect USB

```bash
>>> adb devices
    List of devices attached
    RZ8N60JN0EE     device

>>> adb shell "ip addr show wlan0 | grep -e wlan0$ | cut -d\" \" -f 6 | cut -d/ -f 1"
    192.168.0.103 (phone's IPV4 Address)

>>> adb connect 192.168.0.103:5555
    connected to 192.168.0.103:5555
```

    Step 3: Testing

```bash
>>> adb shell input keyevent 26
    (simulates power button click)

>>> scrcpy --tcpip=192.168.0.103
    (screen share stared)
```
