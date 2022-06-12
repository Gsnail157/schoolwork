#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

int binSearch(int arr[], int n, int target){
	int low = 0 ;	
	while (low <= n){
	int mid = low + (n - 1) /2 ;
	if (arr[mid] == target){
		return mid ;
		}
	if (arr[mid] < target){
		low = mid + 1 ;
		}
	else{
		n = mid - 1 ;
		}
	}
	return -1 ;
}
void arrStats( double *arr, size_t size, double *mean, double *min, double *max){
	double sum ;
	double pmin = *arr, pmax = *arr ;	
	while ( *arr > 1 ){
		sum += *arr ;
		pmin = (*arr < pmin) ? *arr : pmin ;
		pmax = (*arr > pmax) ? *arr : pmax ;
		*arr++ ;	
		}
	*min = pmin ;
	*max = pmax ;
	*mean = sum / size ;
}
int *arrFind(int *arr, size_t size, int target){
	int *r ;	
	for (int i = 0; i < size; i++){
		if (*arr == target){
			r = &*arr ;	
			return r ;
			}
		else{
			*arr++ ;
		}
	}
	return NULL;
}

void capitalise( char *string){
	char c;	
	while (*string){
	  	c = *string ;
		putchar(toupper(c)) ;
		*string++ ;
	}
	printf("\n") ;
}


int main(){
	double arr[5] = { 4,6,2,10,8 } ;
	int arr2[5] = { 4,6,2,10,8 } ;
	char name[] = "gary" ;	
	int size = 5 ;
	double min, max, mean ;
	double *pmin, *pmax, *pmean ;
	int *p;
	p = arrFind( arr2, size, 2 ) ;
	pmin = &min ;
	pmax = &max ;
	pmean = &mean ;
	arrStats(arr, size, pmean, pmin, pmax) ;
	printf("Mean: %.2lf\n", mean) ;
	printf("Min: %.2lf\n", min) ;
	printf("Max: %.2lf\n", max) ;
	printf("Target: %d\n", *p) ;
	capitalise(name) ;	
	return 0 ;	
}


