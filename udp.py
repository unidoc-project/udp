import sys
import executer

from colorama import init
from termcolor import colored
from tkinter import *
init()
gelistirici = colored("""
                   Udp Kullanım Eğitimi
         	Lisans: MIT Yazar: Kerem ATA
""", "red") + """
Udp Kullanırak Bir Sayfa (Döküman) hazırlama
Udp kullanarak bir Sayfa hazırlamak için ilk önce bir dosya oluşturmalısınız
sonra oluşturduğunuz dosyayı bir metin editöründe açın ve düzenlemeye başlayın.
Udp sayfanızı görüntülemek için xml kullanır. 

----------
Element nedir
element açılış etiketi, kapanış etiketi ve içerikten oluşan yapıdır.
örnek

Element Açıldı
  ↓
<udp></udp>: Bu bir elemet dir
		↑
Element Kapatıldı

----------
Element İçeriği
Element İçerği elementin içindeki metin vb. dir açılış ve kapanış etiketinin içine denir.

<content>Bu Bir içeriktir.</content>
----------
Element Niteliği
Element niteliği bir elementin içinde bulunan  açılış etiketinde ve elementeki verileri ayarlar

örnek
		Sayfa içerğinin Yazı tipi boyutu belirtildi
          ↓
<content font-size="50">Merhaba</content>

----------
Udp Elementi
<udp> elementi kodunuzun içinde bulunması zorunlu bir elementtir. Ana element işlevi görür
yazılacak diğer bütün elementler bu <udp> elementinin altına yazılmalıdır

----------
title Elementi
<title> Elementi sayfayı görüntüleyen udv tarayıcısının veya standart görüntüleyici pencerenin başlığını değiştirir

----------
Content Elementi
<content> Elementi sayfanın içerğini değiştirir 

Font büyüklüğünü değiştirmek için Element Niteliği kullanılır

kullanım
<content font-size="50">Test</content>

Metin hizasını değiştirmek için pack kullanılır

kullanım
<content pack="left">Test</content>
----------
Config Elementi
<config> Elementi sayfanın ayarlarını değiştirmek için kullanılır. Ayar değiştirmek için Element Niteliği gerekmektedir

set-win-size: Standart sayfa görüntüleyicisin pencere boyutunu değiştirir
kullanım
<config set-win-size="500x500">
""" + colored("""
Yukarıya Doğru Çıkarak Eğitime Başlayabilirsiniz
""" , "red")
try:
	if sys.argv[1] == "-h":
		print("""Udp Yardım Menüsü

-komutlar-
run <dosya> Dosyayı Çalıştırır
-h Yardım menüsü

-Sorun/SSS-
yardim gelistirici
""")
	elif sys.argv[1] == "yardim":
		try:
			if sys.argv[2] == "gelistirici":
				print(gelistirici)
		except IndexError:
			print("Ergüman Hatası yardım için -h")
	elif sys.argv[1] == "run":
		try:
			executer.Udp(sys.argv[2])
		except IndexError:
			print("Hata: 'run' için bir argüman gereklidir örnek run dosya.udp")
	else:
		print("Ergüman Hatası yardım için -h")
except IndexError:
	print("Ergüman Hatası yardım için -h")