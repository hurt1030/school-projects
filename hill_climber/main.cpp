#include <iostream>

using namespace std;

double eval(int *pj);

int main()
{
    int vec[100];

    for (int i = 0; i < 100; i++)
    {
        vec[i] = 1;
    }
    double fitness = eval(vec);
    cout << "fitness = " << fitness << endl;
}