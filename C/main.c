#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int mFibModQ(int n, int m, int q)
{
    if (n <= 1)
        return n;

    int a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++)
    {
        temp = (m * b + a) % q;
        a = b;
        b = temp;
    }
    return b;
}

int *PisanoPeriod(int m, int q, int *length)
{
    if (q <= 0)
        return NULL;
    if (q == 1)
    {
        *length = 1;
        int *sequence = malloc(sizeof(int));
        sequence[0] = 0;
        return sequence;
    }

    int *sequence = malloc(100000000 * sizeof(int)); // Allocate large enough space
    sequence[0] = 1;
    sequence[1] = m % q;
    int i;

    for (i = 2; i < 100000000; i++)
    {
        sequence[i] = (m * sequence[i - 1] + sequence[i - 2]) % q;
        if (sequence[i] == sequence[1] && sequence[i - 1] == sequence[0])
        {
            *length = i - 1;
            return sequence;
        }
    }
    *length = i;
    return sequence;
}

int checkMidyPropertyMatrix(int m, int n)
{
    int length;
    int *period = PisanoPeriod(m, n, &length);
    if (!period)
        return 0;

    for (int i = 1; i < length; i++)
    {
        if (period[i] == 0 && period[i - 1] == n - 1)
        {
            free(period);
            return 1;
        }
    }

    free(period);
    return 0;
}

int *getMidyNumbersMatrix(int m, int N, int *count)
{
    int *numbers = malloc((N - 2) * sizeof(int));
    *count = 0;

    for (int n = 3; n <= N; n++)
    {
        if (checkMidyPropertyMatrix(m, n))
        {
            numbers[*count] = n;
            (*count)++;
        }
    }

    return numbers;
}

int main()
{
    int m_start, m_end;
    printf("Enter range of m (start end): ");
    scanf("%d %d", &m_start, &m_end);

    FILE *file = fopen("midy_results.txt", "a");
    if (file == NULL)
    {
        printf("Error opening file!\n");
        return 1;
    }

    for (int m = m_start; m <= m_end; m++)
    {
        clock_t start, end;
        double cpu_time_used;
        start = clock();

        int count;
        int *midyNumbers = getMidyNumbersMatrix(m, 100000, &count);

        end = clock();
        cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;

        fprintf(file, "Midy numbers for m = %d:\n", m);
        for (int i = 0; i < count; i++)
        {
            fprintf(file, "%d ", midyNumbers[i]);
        }
        fprintf(file, "\nExecution time: %f seconds\n\n", cpu_time_used);

        printf("Results for m = %d appended to midy_results.txt\n", m);
        free(midyNumbers);
    }

    fclose(file);
    return 0;
}