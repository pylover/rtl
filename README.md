rtl
===

Right-to-Left text reshaper, useful for reading rtl text on the terminal, or any naive text renderrer



    $ sudo apt-get install python-pip
    $ sudo pip install rtl
    $ rtl < file-in.txt > file-out.txt
    $ echo 'متن فارسی' | rtl
    $ cat file.txt | rtl | less
    $ iconv -f windows-1256 -t utf8 | rtl | less


PyPi
----

https://pypi.python.org/pypi/rtl



Change log
----------

[0.4.2] Optional bidi and or reshape parameters for rtl function
