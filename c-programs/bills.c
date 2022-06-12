/*****************************************************
# * bills.c -- represent that amount with the fewest number of $20, $10, $5, and $1 bills.
# *
# * Gary Wang
# *
# * May 2022
# *
# * gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
# * 5.4.0-105-generic x86_64 GNU/Linux
# *****************************************************/
#include <stdio.h>
#include <stdlib.h>

int main(){

	int cash ;
	printf("Enter a dollar amount => ") ;	
	scanf( "%d", &cash) ;
	printf("$20 bills: %4d\n", cash / 20);
   cash = cash % 20;
   printf("$10 bills: %4d\n", cash / 10);
   cash = cash % 10;
   printf("$ 5 bills: %4d\n", cash / 5);
   cash = cash % 5;
   printf("$ 1 bills: %4d\n", cash);
   return 0;
}
