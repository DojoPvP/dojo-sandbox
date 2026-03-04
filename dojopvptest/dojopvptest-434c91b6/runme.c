#include <unistd.h>
#include <stdio.h>

int main() {
	setuid(0);
	setgid(0);
	execl("/run/dojo/bin/python", "python", "/challenge/challenge.py", NULL);
	return 0;
}
