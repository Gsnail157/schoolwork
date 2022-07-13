#ifndef DATABASE_H
#define DATABASE_H

typedef struct itemNode itemNode ;
typedef struct db *db ;

//Creates a new database
db create(void) ;
//Adds new node to database
void addToDB( db database, char id[], unsigned short qty, char desc[] ) ;
//Reads each line in file and adds info to database
void readData(db database, FILE *f) ;
//Adds qty if ID exists in database
void add(db database, char id[], unsigned short qty) ;
//Removes qty if ID exists in database
void rm(db database, char id[], unsigned short qty) ;
//Prints Database
void print(db database) ;

#endif
