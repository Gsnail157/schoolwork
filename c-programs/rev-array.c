/* rev-array.s
	Gary Wang
	Purpose - Reads input until EOF, reverse numbers in a new array
	gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
*/
#include <stdlib.h>
#include <stdio.h>

int main()
{
	char *buff = NULL;
	size_t len;
	int cnt = 0;
	int numbers[100];
	while (getline(&buff, &len, stdin) > 1)
	{
		sscanf(buff, "%d", &numbers[cnt]);
		cnt++;
	}
	int new_list[cnt];
	for (int i = 0; i < cnt; i++)
	{
		new_list[i] = numbers[cnt - 1 - i];
	}
	for (int i = 0; i < cnt; i++)
	{
		printf("%d\n", new_list[i]);
	}
	free(buff);
	return 0;
}
