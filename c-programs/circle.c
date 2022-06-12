#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main( int argc, char *argv[]){
	if (argc < 2) {
		fprintf( stderr, "Need 2 arguments, a name and radius.\n") ;
		return 0 ;
	}
	double radius, area ;
	char *ptr ;
	radius = strtod(argv[2], &ptr) ;
	area = M_PI * pow(radius, 2) ;	
	printf("%s, your area is %.4e units square\n", argv[1], area) ;	
	return 0 ;
}
