build: 265inventory.o 265func.o
	gcc 265inventory.o 265func.o -o build

265inventory.o: 265inventory.c 265inventory.h
	gcc -c 265inventory.c

265func.o: 265func.c 265inventory.h
	gcc -c 265func.c
view: 
	cat 265inventory.h | less
	cat 265func.c | less
	cat 265inventory.c | less

clean: 
	rm *.o build

