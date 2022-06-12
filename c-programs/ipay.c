/*****************************************************
# * ipay.c -- Given an amount, the subtotal of what the user consumed, compute the tax, tip, and print the portion of the bill for the user
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
	double cash ;
 	double tip ;
	double tax ;
 	printf("Enter subtotal => ") ;
   scanf( "%lf", &cash) ;
  	tax = cash * 0.07 ;
	tip = cash * .22 ;
	printf("%-12s %-12.2lf\n","Subtotal:", cash) ;
	printf("%-12s %-12.2lf\n","Tax:", tax) ;
	printf("%-12s %-12.2lf\n","Tip:", tip) ;
	printf("%-12s %-12.2lf\n","Total:", cash + tax + tip) ;

	return 0;
}
