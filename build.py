import os

if not os.path.exists("build"): os.mkdir("build")
with open("build/.gitignore", 'w') as f:
    f.write("*")

for fn in os.listdir():
    if fn.endswith(".svg"):
        os.system(f'ffmpeg -i {fn} build/{fn[:-4]}.png')
