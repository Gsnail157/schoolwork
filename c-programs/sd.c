#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
	double data[100];
	char *buff = NULL ;
	size_t len ;
	int k = 0 ;
	double total ;
	double num ;	

	while( getline( &buff, &len, stdin ) > 1 )
	{
		sscanf(buff, "%lf", &data[k]) ;
		k++ ;	
	}
	for( size_t i = 0; i<k; i++)
	{
		total += data[i] ;	
		printf("%.2lf\n", data[i]) ;		
	}
	for ( size_t i = 0; i<k; i++)
	{
		num += pow(data[i] - (total/k), 2 );
	}

	printf("Mean: %.2lf\n", total/k) ;
	printf("Standard Deviation: %.2lf\n", sqrt(num/k)) ;

	free(buff) ;
	return 0 ;
}
