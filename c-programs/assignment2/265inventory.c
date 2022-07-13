/* 
1). Read DB file
2). sperate data from each line
3). input each data into a node and form a linked list
4). greet user with prompt until quit
5). Have 4 commands a user can input. quit,add,remove,print
6). Implement error handling
7). MakeFile setup
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "265inventory.h"

int main( int argc, char *argv[] ){

	// Open file for reading
	FILE *fin = stdin ;
	if (argc > 1){
		fin = fopen( argv[1], "r" ) ;
		if ( fin == NULL ){
			exit(1) ;
			}
	}
	//Create Database	
	db info = create() ;
	readData(info, fin) ;

	//User input loop
	char *buff = NULL ;
	size_t len ;
	char response[7] ;
	char id[16] ;
	unsigned short qty ;
	printf("%% ") ;	
	while ( getline( &buff, &len, stdin) != -1 ){ 
		sscanf(buff, "%s%[^:]:%hu", response, id, &qty) ;
		if (strcmp( response, "quit" ) == 0 ){
			printf("ARK\n") ;
			break ;	
			}
		else if ( strcmp( response, "add" ) == 0 ){
			if (sscanf(buff, "%s%[^:]:%hu", response, id, &qty) > 2){	
				printf("ARK\n") ;
				add(info, id, qty) ;	
				}	
			else{
				printf("NAK Incorrect syntax\n") ;
				}
			}
		else if ( strcmp( response, "remove" ) == 0 ){
			if (sscanf(buff, "%s%[^:]:%hu", response, id, &qty) > 2){	
				printf("ARK\n") ;
				rm(info, id, qty) ;	
				}	
			else{
				printf("NAK Incorrect syntax\n") ;
				}
			}
		else if ( strcmp( response , "print" ) == 0 ){
			printf("ARK\n") ;
			print(info) ;	
			}
		else{
			printf("Unrecognised command\n") ;
			}
		printf("%% ") ;	
		}
	return 0 ;
}
