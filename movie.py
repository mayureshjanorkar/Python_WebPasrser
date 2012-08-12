#!/usr/bin/python

import urllib, re
url_base = "http://www.google.com/movies?hl=en&near=94089"
str = urllib.urlopen(url_base)

print "Content-type:text/html\n\n"
#print "Content-type:text/plain\n\n"

print "<HTML><HEAD><TITLE>Movies Near 90007</TITLE></HEAD>"
print "<BODY>"

#print "Content-type:text/plain\n\n"
#print (str.read())
#entries = re.split("id=link_1_theater_", str)
#entries = re.split("<span class=info>", str.read())
#entries = re.split("<div class=theater><div class=desc id=theater", str.read())

entries = re.split("id=link_1_theater_", str.read())

first_entry = 0

for entry in entries:
        if first_entry == 0:
                first_entry = 1
                continue

        theater_names = entry
        theater_names = re.split(">", theater_names)
        theater_name = theater_names[1]
        theater_names = re.split("<", theater_name)
        theater_name = theater_names[0]
        th_addr = entry
        th_addr_list = re.split("<div class=info>", th_addr)
        th_addr_list = re.split("<a href", th_addr_list[1])

        theater_address = th_addr_list[0]

        movies_list = re.split("<div class=movie><div class=name>", entry)

        first_enrty = 1
        first_url = 1
        movie_no = 1
        for m in movies_list:
                if first_entry == 1:
                        first_entry = 0
                        continue
                mov = re.split("</a></div>", m)
                #ovies_list[1])

                m_list = re.split(">", mov[0])
                movie = m_list[1]

                #print "\n Movie = %s " % movie
                url1 = re.split("Trailer</a> - <a href=\"/url?", m)
                #entry)

                #print "\n\n Length = url1 = %d " % len(url1)

                #print "url1[0] = %s " % url1[0]
                #print "url1[1] = %s " % url1[1]

                if (first_url == 1):
                        url11 = re.split("=", url1[1])
                        url111 = re.split("&", url11[1])
                        first_url = 0
                else:
                        if (len(url1) == 1):
                                url11 = re.split(" - <a href=\"", url1[0])
                        else:
                                url11 = re.split(" - <a href=\"", url1[1])

                        i = 0
                        while (i < 10):
                                r = re.split("imdb", url11[i])
                                #print "\n r len is %d, i is %d : %s " % (len(r), i, url11[i])
                                if (len(r) == 1):
                                        #print "\n i is = %d " % i
                                        i = i + 1
                                else:
                                        break

                        #print "\n i = %d " % i
                        #print "\n url11[i] = %s " % url11[i]
                        url1 = re.split("=", url11[i])
                        #print "\n ::url1[0] = %s " % url1[0]
                        #print "\n ::url1[1] = %s " % url1[1]
                        url111 = re.split("&sa", url1[1])
                        #print "\n url111 %s " % url111[0]

                imdb_url = url111[0]

                #print "imdb_url = %s \n" % imdb_url

                imdb_content = urllib.urlopen(imdb_url)
                image_link11 = re.split("id=\"img_primary\"", imdb_content.read())

                image_link1 = re.split("src=\"", image_link11[1])
                image_link1 = re.split("\"", image_link1[1])

                image_link = image_link1[0]
                print "11111111111111111111111111111111111111111111111\n"

                print "<H1>Theater Name = %s" % theater_name
                print "</H1>\n<H2> Theater Address = %s " % theater_address

                print "</H2>\n<Table border=2><TR>"
                print "\n<TH>Image</TH> <TH>Movie Name</TH> <TH>IMDB</TH>"

                print "\n</TR><TR>"
                print "\n<TD><img src=\"%s" % image_link
                print "\" width=100 height=150></img></TD>\n<TD> %s" % movie
                print "</TD>\n<TD> <a href=\"%s" % imdb_url
                print "\" target=__blank>%s</a></TD>\n" % imdb_url

                #print "\n ================== \n"
        break

print "\n<HR><HR>\n"

