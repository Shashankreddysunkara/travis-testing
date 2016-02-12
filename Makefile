lib: clean
	gcc -shared -fPIC -o thing/test_lib/libtest.so thing/test_lib/test.c

clean:
	rm -f thing/test_lib/libtest.so
