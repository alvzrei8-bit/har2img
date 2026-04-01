import os, sys
from datetime import datetime

def ff(name):
    if os.path.isfile(name): return name
    if "." not in os.path.basename(name):
        d = os.path.dirname(name) or "."
        b = os.path.basename(name)
        for f in os.listdir(d):
            if f.startswith(b + "."): return os.path.join(d, f)
    return None

def mkh(p):
    return p if p.endswith(".h") else p + ".h"

def conv(inp, out, dev="reiii"):
    with open(inp, "rb") as f: data = f.read()
    ts = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    src = os.path.basename(inp)
    dst = os.path.basename(out)
    
    with open(out, "w") as f:
        f.write(f"/*\n * file: {dst}\n * src: {src}\n * dev: {dev}\n * generated: {ts}\n */\n\n")
        f.write("const unsigned char image[] = {\n")
        for i, b in enumerate(data):
            if i % 16 == 0: f.write("    ")
            f.write(f"0x{b:02X}, ")
            if i % 16 == 15: f.write("\n")
        f.write("\n};\n")
    print(f"generated: {out}")

def main():
    if len(sys.argv) < 3:
        print("usage: python3 harray.py <input> <output>")
        return
    inp = ff(sys.argv[1])
    if not inp:
        print("[!] not found")
        return
    conv(inp, mkh(sys.argv[2]))

if __name__ == "__main__":
    main()

# yea... idk 
# yes jablowski
