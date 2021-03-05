#include <cmath>

double eval(int vec[])
{
    double total;
    for (int i = 0; i < 100; i++)
    {
        if (vec[i] == 1)
        {
            total += (cos(i) + sin(i)) * (cos(i) * sin(i));
        }
        else
        {
            total += (cos(i) - sin(i)) * (cos(i) * sin(i));
        }
    }

    return total;
}