#include <stdio.h>
#include <string.h>

struct process
{
    int wt, at, bt, tat, priority;
};
struct process array[10];
int main()
{
    int n, temp[10], t, count = 0, prior;
    float total_wt = 0, total_tat = 0, average_wt, average_tat;
    printf("Total Process Count\n");
    scanf("%d", &n);
    printf("at  bt  priority\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d%d%d", &array[i].at, &array[i].bt, &array[i].priority);
        temp[i] = array[i].bt;
    }
    array[9].priority = 10000;

    for (t = 0; count != n; t++)
    {
        prior = 9;
        for (int i = 0; i < n; i++)
        {
            if (array[prior].priority > array[i].priority && array[i].at <= t && array[i].bt > 0)
            {
                prior = i;
            }
        }
        array[prior].bt = array[prior].bt - 1;
        if (array[prior].bt == 0)
        {
            count++;
            array[prior].wt = t+1-array[prior].at-temp[prior];
            array[prior].tat = t + 1 - array[prior].at;

            total_wt = total_wt + array[prior].wt;
            total_tat = total_tat + array[prior].tat;
        }
    }
    average_wt = total_wt / n;
    average_tat = total_tat / n;
    printf("WT TAT\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t%d\n", i + 1, array[i].wt, array[i].tat);
    }
    printf("Average Waiting Time of the process  is %f\n", average_wt);
    printf("Average turn around time of the process is %f\n", average_tat);
    return 0;
}