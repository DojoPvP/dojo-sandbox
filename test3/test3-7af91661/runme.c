#include <unistd.h>
#include <stdio.h>

int main() {
	setuid(0);
	setgid(0);
	execl("/challenge/run.sh", "/challenge/run.sh", NULL);
	return 0;
}
