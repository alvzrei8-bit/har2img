import os,sys
from datetime import datetime as dt

def ff(n): #shortened version
 p=n if os.path.isfile(n)else(lambda d,b:[os.path.join(d,f)for f in os.listdir(d)if f.startswith(b+".")][0]if"."not in b else None)(os.path.dirname(n)or".",os.path.basename(n))
 return p

def conv(i,o,dev="reiii"):
 d=open(i,"rb").read()
 with open(o,"w")as f:f.write(f"/*\n * file: {os.path.basename(o)}\n * src: {os.path.basename(i)}\n * dev: {dev}\n * generated: {dt.now().strftime('%y-%m-%d %H:%M:%S')}\n */\n\nconst unsigned char image[] = {{\n"+"\n".join("    "+"".join(f"0x{b:02X}, "for b in d[j:j+16])for j in range(0,len(d),16))+"\n};\n")

sys.argv[1:]and(lambda n:n and conv(n,sys.argv[2]+".h"if not sys.argv[2].endswith(".h")else sys.argv[2]))or print("[!] not found")(ff(sys.argv[1]))if len(sys.argv)>2 else print("usage: python3 harray.py <input> <output>")
