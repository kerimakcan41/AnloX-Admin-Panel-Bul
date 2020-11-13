# -*- coding: UTF-8 -*-
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	linkler = open("Link.txt","r");
	link = raw_input("Lütfen Bir Site İsmi Girin \n (Örnek: 'örnek.com' Ya Da 'www.örnek.com'): ")
	print "\n Admin Panel Linkleri: \n"
	while True:
		admin_link = linkler.readline()
		if not admin_link:
			break
		bulunan_link = "http://"+link+"/"+admin_link
		req = Request(bulunan_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Bulundu: ",bulunan_link

def Credit():
	Space(10); print "Anlo'X - Admin Panel Bulucu"
	Space(1); print ""
	Space(5); print "Kodlayan: Anlo'X"
	Space(5); print "Instagram: @kerimakcan_"
	Space(5); print "GitHub: kerimakcan41"
	Space(5); print "WebSite: https://anloks.glitch.me"
	Space(1); print ""
	Space(1); print ""
	Space(1); print ""
	Space(10); print "Anlo'X Admin Panel Bulucu Nedir"
	Space(1); print ""
	Space(3); print "Bu Zamana Kadar Bütün Sitelerde Admin Panel Bulunmaktadır"
	Space(3); print "Genellikle Admin Panel Site Kurucuları Tarafından Oluşturuluyor"
	Space(3); print "Admin Panel Bütün Site İşlemlerini İçinde Yer Almaktadır"
	Space(3); print "Admin Panel Gizli Olduğu İçin Sadece Kurucular Tarafından Erişilmektedir"
	Space(3); print "Bende Bunun İçin Admin Panel Bulucu Geliştirdim"
	Space(1); print ""
	Space(10); print "Anlo'X Saygılarla Sunar"
	Space(1); print ""
	Space(1); print ""
	

Credit()
findAdmin()