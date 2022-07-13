#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "265inventory.h"

struct itemNode {
   char id[16] ;
   unsigned short qty ;
   char desc[31] ;
   itemNode *next ;
} ;

struct db {
   itemNode *top ;
} ;

db create(void){
   db database = malloc(sizeof(db)) ;
   if (database == NULL){
      printf("Could not create database") ;
   }
   database->top = NULL ;
   return database ;
}

void addToDB(db database, char id[], unsigned short qty, char desc[]){
   itemNode *node = (itemNode*) malloc(sizeof(itemNode)) ;
   if (node == NULL){
      printf("Stack if Full!") ;
      return ;
   }
   strcpy(node->id, id) ;
   node->qty = qty ;
   strcpy(node->desc, desc) ;
   node->next = database->top ;
   database->top = node ;
}
void readData(db database, FILE* f){
   char *line = NULL ;
   size_t len ;
   char id[16] ;
   char desc[32] ;
   signed short qty ;
   while( getline ( &line, &len, f ) != -1){
      sscanf( line,"%[^:]:%hu:%[^:]", id, &qty, desc) ;
      addToDB(database, id, qty, desc) ;
		}
}

void add(db database, char id[], unsigned short qty){
   itemNode *node = (itemNode*) malloc(sizeof(itemNode)) ;
   node = database->top ;
   while (node != NULL){
      if (strcmp(node->id, id) == 0){
         node->qty += qty ;
         return ;
      }
   node = node->next ;
   }
   printf("NAK Unknown Item\n") ;
}

void rm(db database, char id[], unsigned short qty){
   itemNode *node = (itemNode*) malloc(sizeof(itemNode)) ;
   node = database->top ;
   while (node != NULL){
      if ((strcmp(node->id, id) == 0) && (node->qty >= qty)){
         node->qty -= qty ;
         return ;
      }
      else{
         printf("NAK Insufficient Quantity\n") ;
         return ;
      }
   node = node->next ;
   }
}
void print(db database){
   printf(" DESC                  QTY      ID\n") ;
   printf("--------------------  -------  -----------\n");
   itemNode *node = (itemNode*) malloc(sizeof(itemNode)) ;
   node = database->top ;
   while(node != NULL){
      printf("%s %d %s\n", node->desc, node->qty, node->id) ;
      node = node->next ;
   }
   free(node) ;
   node = NULL ;
}




