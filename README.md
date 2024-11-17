# 4Doszer tool
Ini ialah tool yang menyerang dengan menghantar Denial of Service (DOS) ke pelayan dengan mebanjiri pada port-port udp si server.

# New features
- Hostname(domain) into ip
- Server ddos

# Screenshot
<img src="img/IMG_20241117_103309.jpg">
<img src="img/IMG_20241117_103252.jpg">

# Use as Termux
- Update package, upgrade package, install git, install python.
```bash
pkg update && pkg upgrade -y && pkg install git -y && pkg install python -y
```


- Git clone tool and run
```bash
git clone https://github.com/mika259/4doszer
cd 4doszer
python 4doszer.py
```

- Unix-Like user mesti dah tahu cara pasang sendiri.

# Info
- Tool ini dicompile kerana saya sedang belajar dalam obfuscating scripting.

- saya compile file python ke binary dengan :

```bash
python -m py_compile dos.py
```

- output file binary dalam folder '__pycache__' boleh run terus compiled file tu.

# Source Code of file
<a href="https://gist.github.com/Mika259/832e0b155c1ed9b1179a185a78db906d">see here</a>
