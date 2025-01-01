#include <stdio.h>

/*Sample Input:
Number of processes:
5
Number of recources:
4
Allocation Matrix:
0 1 0 3
2 0 0 0
3 0 2 0
2 1 1 5
0 0 2 2
Maximum Matrix:
6 4 3 4
3 2 2 1
9 1 2 6
2 2 2 8
4 3 3 7
Available Matrix:
10 5 7 11
*/

int maxArray[100][100];
int alloc[100][100];
int need[100][100];
int avail[100][100];
int n, m;

void user_data()
{
    int x, y;
    printf("Number of processes:\n");
    scanf("%d", &n);
    printf("Number of recources:\n");
    scanf("%d", &m);
    printf("Allocation Matrix:\n");

    for (x = 0; x < n; x++)
    {
        for (y = 0; y < m; y++)
        {
            scanf("%d", &alloc[x][y]);
        }
    }
    printf("Maximum Matrix:\n");
    for (x = 0; x < n; x++)
    {
        for (y = 0; y < m; y++)
        {
            scanf("%d", &maxArray[x][y]);
        }
    }
    printf("Available Matrix:\n");
    for (x = 0; x < m; x++)
    {
        scanf("%d", &avail[0][x]);
    }
}

void calculation()
{
    int finish[100], temp, need[100][100], flag = 1, k, count = 0;
    int dead[100];
    int safe[100];
    int x, y;
    for (x = 0; x < n; x++)
    {
        finish[x] = 0;
        dead[x] = 0;
        safe[x] = 0;
    }
    for (x = 0; x < n; x++)
    {
        for (y = 0; y < m; y++)
        {
            need[x][y] = maxArray[x][y] - alloc[x][y];
        }
    }
    while (flag)
    {
        flag = 0;
        for (x = 0; x < n; x++)
        {
            int c = 0;
            for (y = 0; y < m; y++)
            {
                if (finish[x] == 0 && need[x][y] <= avail[0][y])
                {
                    c++;
                    if (c == m)
                    {
                        for (k = 0; k < m; k++)
                        {
                            avail[0][k] = avail[0][k] + alloc[x][k];
                            finish[x] = 1;
                            flag = 1;
                        }
                        if (finish[x] == 1)
                        {
                            x = n;
                        }
                    }
                }
            }
        }
    }
    y = 0;
    flag = 0;
    for (x = 0; x < n; x++)
    {
        if (finish[x] == 0)
        {
            dead[y] = x;
            y++;
            flag = 1;
        }
    }
    if (flag == 1)
    {
        printf("DEADLOCK AHEAD!\n");
    }
    else
    {
        printf("SAFE HERE!\n");
    }
}
int main()
{
    int x, y;
    user_data();
    calculation();
    return 0;
}

