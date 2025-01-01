#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
/*
This program provides a possible solution using mutex and semaphore.
use 5 Farmers and 5 ShopOwners to demonstrate the solution.
*/
#define MaxCrops 5 // Maximum crops a Farmer can produce or a Shpoowner can take
#define warehouseSize 5 // Size of the warehouse
sem_t empty;
sem_t full;
int in = 0;
int out = 0;
char crops[warehouseSize]={'R','W','P','S','M'}; //indicating room for different crops
char warehouse[warehouseSize]={'N','N','N','N','N'}; //initially all the room is empty
pthread_mutex_t mutex;

void *Farmer(void *far)
{
   /*
   1.Farmer harvest crops and put them in particular room. For example, room 0 for Rice(R).
   2.use mutex and semaphore for critical section.
   3.print which farmer is keeping which crops in which room inside the critical section.
   4.print the whole warehouse buffer outside of the critical section
   */
    int i;
    int id = (*(int *)far);
    for (i = 0; i < MaxCrops; i++)
    {
        sem_wait(&empty);
        pthread_mutex_lock(&mutex);
        warehouse[in] = crops[id];
        in = (in + 1) % warehouseSize;
        printf("Farmer %d: Insert crops %c at %d\n", id, crops[id], in);
        pthread_mutex_unlock(&mutex);
        sem_post(&full);
    }

}
void *ShopOwner(void *sho)
{
/*
   1.Shop owner takes crops and makes that particular room empty.
   2.use mutex and semaphore for the critical section.
   3.print which shop owner is taking which crops from which room inside the critical section.
   4.print the whole warehouse buffer outside of the critical section
   */
    int i;
    int id = *(int *)sho;
    for (i = 0; i < MaxCrops; i++)
    {
        sem_wait(&full);
        pthread_mutex_lock(&mutex);
        out = (out + 1) % warehouseSize;
        printf("Shop owner %d: Remove crops %c from %d\n", id, warehouse[out], out);
        pthread_mutex_unlock(&mutex);
        sem_post(&empty);
    }
}
int main()
{
    /*initializing thread,mutex,semaphore
    */
    pthread_t Far[5],Sho[5];
    pthread_mutex_init(&mutex, NULL);
    sem_init(&empty,0,warehouseSize);//when the warehouse is full thread will wait
    sem_init(&full,0,0);//when the warehouse is empty thread will wait

    int a[5] = {1,2,3,4,5}; //Just used for numbering the Farmer and ShopOwner

    /*create 5 thread for Farmer 5 thread for ShopOwner
    -------------------------------------------------
    -------------------------------------------------
    */
    int b[5] = {6, 7, 8, 9, 10};
    int i;
    for (i = 0; i < 5; i++)
    {
        pthread_create(&Far[i], NULL, Farmer, &a[i]);
        pthread_create(&Sho[i], NULL, ShopOwner, &b[i]);
    }
    for (i = 0; i < 5; i++)
    {
        pthread_join(Far[i], NULL);
        pthread_join(Sho[i], NULL);
    }

    //  Closing or destroying mutex and semaphore
    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);


    return 0;

}
