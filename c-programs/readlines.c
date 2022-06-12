/*********************************************************
 * readlines.c - reads until blank line or EOF
 *
 *******************************************************/

#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *buff = NULL ;
	size_t len ;
	int cnt = 0 ;
	double num , min = num, max = num , total ;
	while( getline( &buff, &len, stdin ) > 1 )
	{
	 	sscanf(buff,"%lf",&num)	;
		min = (num < min) ? num : min ;
		max = (num > max) ? num : max ;
		total += num ;	
		++cnt ;
	}
	printf( "Min = %.2lf\n", min) ;
	printf( "Max = %.2lf\n", max) ;	
	printf( "Mean = %.2lf\n", (total/cnt))	;
	free( buff ) ;
	return 0 ;
}
