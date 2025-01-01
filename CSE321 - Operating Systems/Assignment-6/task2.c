#include <stdio.h>
int main()
{
    int x, y, z, m, n;
    n = 6;
    m = 4;
    char sequence[1000];
    int alloc[6][4] =
    {
        {0, 1, 0, 3},
        {2, 0, 0, 3},
        {3, 0, 2, 0},
        {2, 1, 1, 5},
        {0, 0, 2, 2},
        {1, 2, 3, 1}
    };

    int max[6][4] =
    {
        {6, 4, 3, 4},
        {3, 2, 2, 4},
        {9, 1, 2, 6},
        {2, 2, 2, 8},
        {4, 3, 3, 7},
        {6, 2, 6, 5}
    };

    int temp[n], result[n], counter = 0;
    int avail[4] = {2, 2, 2, 1};

    for (z = 0; z < n; z++)
    {
        temp[z] = 0;
    }
    int need[n][m];
    for (x = 0; x < n; x++)
    {
        for (y = 0; y < m; y++)
        {
            need[x][y] = max[x][y] - alloc[x][y];
        }
    }
    int a = 0;
    for (z = 0; z < 5; z++)
    {
        for (x = 0; x < n; x++)
        {
            if (temp[x] == 0)
            {
                int flag = 0;
                for (a = 0; a < m; a++)
                {
                    if (need[x][a] > avail[a])
                    {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0)
                {
                    result[counter] = x;
                    for (a = 0; a < m; a++)
                    {
                        avail[a] += alloc[x][a];
                    }
                    temp[x] = 1;
                    counter++;
                }
            }
        }
    }
    int flag = 1;
    for (x = 0; x < n; x++)
    {
        if (temp[x] == 0)
        {
            flag = 0;
            printf("DEADLOCK AHEAD!\n");
            break;
        }
    }
    if (flag == 1)
    {
        printf("Safe Sequence:\n");
        for (x = 0; x < n; x++)
        {
            if (x==n-1)
            {
                printf("P%d", result[x]+1);
            }
            else
            printf("P%d --> ", result[x]+1);
        }
    }
    return 0;
}
