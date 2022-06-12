#include <stdio.h>
#include <stdlib.h>

/* arrAvg - Returns the mean of all doubles in a given array
* Inputs - Array, Size of Array
* Ouputs - Arithmetic Mean
* Side Effects - None
*/

double arrAvg( double *arr, int size){
	double sum ;
	for (int i = 0; i < size; i++){
		sum += *arr++ ;
		}	
	return sum / size ;
}

int main(){
	char *buff = NULL ;
	size_t len ;
	int cnt = 0 ;
	double nums[100], avg ;
	// User enters int digits and is stored in nums[] 	
	printf("Enter Number => \n") ;	
	while ( getline( &buff, &len, stdin) > 1){
		printf("Enter Number => \n") ;	
		sscanf( buff, "%lf", &nums[cnt] ) ;
		cnt++ ;
		}
	
	avg =	arrAvg( nums, cnt ) ;	
	printf("Average of array: %.2lf\n", avg) ;
	free(buff) ;
	return 0 ;
}


