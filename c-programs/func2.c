#include <stdio.h>
#include <stdlib.h>


void int2string( int n, char answer[] ){
	char temp[50] ;
	int num = n ;
	int cnt = 0 ;	
	// Convert int into string and store in temp array	
	while ( num != 0 ) {
      temp[cnt] = (char)((num % 10) + '0') ;
		num /= 10 ;
		cnt++ ;
	}
	temp[cnt] = '\0' ;
	// Reverse the temp array
	for (int j = 0; j < cnt; j++){
		temp[j] = temp[cnt - j] ;
	}
	// If the array answer is empty 	
	if (*answer == '\0'){
		for (int r = 0; r < cnt; r++){
			answer[r] = temp[r] ; 	
		}
	answer[cnt] = '\0' ;
	return ;
	}
	// Add new digit to the existing answer array	
	else{	
		int i = 0, k = 0 ;
		while (*answer != '\0') {
			i++ ;
			*answer++ ;
		}
		for (k; k < cnt; k++){
			answer[i] = temp[k] ;
			i++ ;
			}
		answer[i] = '\0' ;
	}
}

int main (){
	char string[100] ;
	int nums[10] ;	
	int cnt = 0 ;
	char *buff = NULL ;
	size_t len ;
	printf("Enter Numbers => ") ;
	while( getline(&buff, &len, stdin) > 1){
		sscanf(buff, "%d", &nums[cnt]) ;
		cnt++ ;	
		}	
	// Convert each integer number the user entered into a char type	
	for (int i = 0; i < cnt; i++){
		int2string( nums[i], string ) ;	
	}
	// Print the result	
	int k = 0 ;	
	while ( string[k] != '\0' ){
		printf("%d", string[k]) ;
		k++ ;
	}
	printf("\n") ;	
	free(buff) ;
	return 0 ;
}
