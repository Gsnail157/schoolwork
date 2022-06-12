/*
 * act8.c - implementations for list functions, Activity 8
 *
 * Kurt Schmidt
 * FEB 22
 *
 * gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0, on
 * 5.4.0-100-generic x86_64 GNU/Linux
 *
 */

#include <stdio.h>
#include <stdlib.h>

#include "act8.h"


void printList( List p, FILE* fout ) 
{
	fputs( "<", fout ) ;
	if( p!=NULL )
	{
		fprintf( fout, "%hd", p->data ) ;
		p = p->next ;
	}
	while( p!=NULL )
	{
		fprintf( fout, ", %hd", p->data ) ;
		p = p->next ;
	}
	fputs( ">", fout ) ;
}


List make_list( elem_t a[], size_t n )
{
	List rv = NULL ;

	if( n==0 )
		return rv ;
	
	rv = make_list( a+1, n-1 ) ;

	sNode* t = (sNode*) malloc( sizeof( sNode )) ;
	if( t==NULL ) return NULL ;

	t->data = a[0] ;	
	printf("%d ", t->data) ;	
	t->next = rv ;
	rv = t ;

	return rv ;
}


List rand_list( size_t n )
{
	if( n==0 )
		return NULL ;

	List rv = NULL ;
	sNode *t = NULL ;
	
	for( size_t i=0; i<n; ++i )	;
}

size_t size( sNode *node) {
	size_t i = 0 ;
	sNode *p = node ;
	while (p != NULL ) {
		i++ ;
		p = p->next ;
		}		
	free(p) ;
	p = NULL ;
	return i ;
}

size_t count( sNode *node, elem_t t ) {
	size_t i = 0 ;
	sNode *p = node ;
	while (p != NULL ){
		if (p->data = t){
			i++ ;
			}
		p = p->next ;
		}
	free(p) ;
	p = NULL ;
	return i ;
}

sNode* remove_first( sNode *node, elem_t t) {
	sNode *head = (sNode*) malloc(sizeof(sNode)) ;	
	sNode *p = NULL ;
	sNode *c = (sNode*) malloc(sizeof(sNode)) ;
	while (c != NULL ){
		if (c->data = t) {
			p = c->next ;	
			free(p) ;
			free(c) ;
			p = NULL ;
			c = NULL ;
			return head ;
			}
		p = c ;
		c = c->next ;
		}
}

sNode *remove_all( sNode *node, elem_t t ) {
	sNode *head = (sNode*) malloc(sizeof(sNode)) ;
	sNode *p = NULL ;
	sNode *c = (sNode*) malloc(sizeof(sNode)) ;
	while (c != NULL ){
		if (c->data = t) {
			p = c->next ;	
			}
		p = c ;
		c = c->next ;
		}
	free(p) ;
	free(c) ;
	p = NULL ;
	c = NULL ;
	return head ;
}

