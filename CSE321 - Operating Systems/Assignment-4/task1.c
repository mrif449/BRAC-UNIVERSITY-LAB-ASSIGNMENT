#include <stdio.h>
#include <string.h>

struct process
{
    int wt, at, bt, tat;
};
struct process array[10];
int main()
{
    int value, temp[10];
    int counter = 0, t = 0, idx;
    float total_wt = 0, total_tat = 0, average_wt, average_tat;
    printf("Total Process Count\n");
    scanf("%d", &value);
    printf("Enter the arrival time and burst time of the process\n");
    printf("at   wt\n");
    for (int x = 0; x < value; x++)
    {
        scanf("%d%d", &array[x].at, &array[x].bt);
        temp[x] = array[x].bt;
    }
    array[9].bt = 10000;
    for (t = 0; counter != value; t++)
    {
        idx = 9;
        for (int x = 0; x < value; x++)
        {
            if (array[x].bt < array[idx].bt && (array[x].at <= t && array[x].bt > 0))
            {
                idx = x;
            }
        }
        array[idx].bt = array[idx].bt - 1;
        if (array[idx].bt == 0)
        {
            counter++;
            array[idx].wt = t+1-array[idx].at - temp[idx];
            array[idx].tat = t+1-array[idx].at;
            total_wt = total_wt+array[idx].wt;
            total_tat = total_tat+array[idx].tat;
        }
    }
    average_wt = total_wt / value;
    average_tat = total_tat / value;
    printf("wt    tat\n");
    for (int x = 0; x < value; x++)
    {
        printf("%d\t%d\n", x + 1, array[x].wt, array[x].tat);
    }
    printf("Avg waiting time of the process is %f\n", average_wt);
    printf("Avg turn around time of the process %f\n", average_tat);
}