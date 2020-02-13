import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", help="the path of your md file")

if __name__ == '__main__':
    os.system("sh up.sh")

    args = ap.parse_args()

    infile = args.path
    outfile = infile.split('.md')[0] + '_gitpic.md'

    with open(infile, 'r', encoding='utf-8') as f: # 需要手动指定解码的格式
        lines = f.readlines()

    old = 'E:\\我的坚果云\\我的坚果云\\博客图床\\One-click-picgo\\imgs\\'
    rep = "https://raw.githubusercontent.com/Simon717/One-click-picgo/master/imgs/"
    out = [l.replace(old, rep) for l in lines]
    with open(outfile, 'w', encoding='utf-8') as f:
        f.writelines(out)
