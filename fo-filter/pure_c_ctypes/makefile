
all : clean lib_fofilter.so
.PHONY: all

lib_fofilter.so : fofilter.o
	gcc -shared -Wl,-soname,lib_fofilter.so -o lib_fofilter.so fofilter.o

fofilter.o : filter_pure_c.c
	gcc -c -O3 -fPIC filter_pure_c.c -o fofilter.o

clean :
	rm -f libcos_doubles.so cos_doubles.o cos_doubles.pyc