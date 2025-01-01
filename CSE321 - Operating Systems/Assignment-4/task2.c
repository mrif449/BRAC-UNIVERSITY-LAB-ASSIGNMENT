#include <stdio.h>
#include <conio.h>

void main()
{
    int x, process_number, count = 0, count = 0, y, tq, wt = 0, tat = 0, at[10], bt[10], flag[10];
    float avg_waiting_time, avg_tat;
    printf("Total Process Count: ");
    scanf("%d", &process_number);
    y = process_number;
    for (x = 0; x<process_number; x++)
    {
        printf("\nArrival and Burst time[%d]\n", x + 1);
        printf(" Arrival time is: \t");
        scanf("%d", &at[x]);
        printf(" \nBurst time is: \t");
        scanf("%d", &bt[x]);
        flag[x] = bt[x];
    }
    printf("Enter the Time Quantum: \t");
    scanf("%d", &tq);
    printf("\n Process No \t\t Burst Time \t\t TAT \t\t Waiting Time ");
    for (count = 0, x = 0; y != 0;)
    {
        if (flag[x] <= tq && flag[x] > 0)
        {
            count = count + flag[x];
            flag[x] = 0;
            count = 1;
        }
        else if (flag[x] > 0)
        {
            flag[x] = flag[x] - tq;
            count = count + tq;
        }
        if (flag[x] == 0 && count == 1)
        {
            y--;
            printf("\nProcess No[%d] \t\t %d\t\t\t\t %d\t\t\t %d", x + 1, bt[x], count - at[x], count - at[x] - bt[x]);
            wt = wt + count - at[x] - bt[x];
            tat = tat + count - at[x];
            count = 0;
        }
        if (x == process_number - 1)
        {
            x = 0;
        }
        else if (at[x + 1] <= count)
        {
            x++;
        }
        else
        {
            x = 0;
        }
    }
    avg_waiting_time = wt * 1.0 / process_number;
    avg_tat = tat * 1.0 / process_number;
    printf("\n Average Turn Around Time: \t%f", avg_waiting_time);
    printf("\n Average Waiting Time: \t%f", avg_tat);
    getch();
}