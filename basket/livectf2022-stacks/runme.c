#include <unistd.h>
#include <stdio.h>

int main() {
	setuid(0);
	setgid(0);
	execl("/challenge/challenge", "/challenge/challenge", NULL);
	return 0;
}
