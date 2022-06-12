/* leap.c
	Gary Wang
	Purpose - Returns YES or NO if year entered is a leap year
	gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0

*/
#include <stdio.h>
#include <stdlib.h>

int main(){
	int leap_year ;
	fprintf(stdout, "Enter a Year => ") ;
	scanf("%d", &leap_year) ;
	if (((leap_year % 4) == 0) && !((leap_year % 100) == 0)) {
		printf("YES\n") ;
		}	
	else if ((leap_year % 400) == 0) {
			printf("YES\n") ;
			}
	else {
		printf("NO\n") ;
		}
	return 0 ; 
}
