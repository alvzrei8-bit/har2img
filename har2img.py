import sys, re, os

def grab_hex(path):
    with open(path, "r") as f: txt = f.read()
    hexs = re.findall(r'0x([0-9A-Fa-f]{2})', txt)
    return bytes(int(h, 16) for h in hexs) if hexs else None

def guess_ext(d):
    if d.startswith(b'\x89PNG'): return ".png"
    if d.startswith(b'\xFF\xD8'): return ".jpg"
    if d.startswith(b'GIF8'): return ".gif"
    if d.startswith(b'BM'): return ".bmp"
    return ".bin"

def fix_name(p, ext):
    return p if os.path.splitext(p)[1] else p + ext

def main():
    if len(sys.argv) < 3:
        print("usage: python3 harray_reverse.py <input.h> <output>")
        return
    data = grab_hex(sys.argv[1])
    if not data:
        print("no hex data found")
        return
    ext = guess_ext(data)
    out = fix_name(sys.argv[2], ext)
    with open(out, "wb") as f: f.write(data)
    print(f"reconstructed: {out}")

if __name__ == "__main__":
    main()
# yes jablowski 
