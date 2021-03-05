#include <iostream>

using namespace std;

double eval(int *pj);
void initializeSolution(int vec[]);
void alter(int oldSolution[], int newSolution[], int currentIndex);
void array_copy(int copyFrom[], int copyTo[]);

int main()
{
    int bestSolution[100];
    int notChangedCount = 0;
    int currentIndex = 0;

    // seed the random function so we don't get the same
    // sequence of random numbers each time the program executes
    srand(time(0));

    initializeSolution(bestSolution);

    double bestFitness = eval(bestSolution);

    while (true)
    {
        int newSolution[100];

        alter(bestSolution, newSolution, currentIndex);

        double newFitness = eval(newSolution);

        if (newFitness > bestFitness)
        {
            array_copy(newSolution, bestSolution);
            bestFitness = newFitness;
            notChangedCount = 0;
        }
        else
        {
            currentIndex++;
        }

        if (currentIndex == 100)
        {
            currentIndex = 0;
            notChangedCount++;
        }

        if (notChangedCount > 100 || bestFitness == 100)
        {
            break;
        }
    }

    std::cout << "Best fitness found = " << bestFitness << std::endl;
}

void initializeSolution(int vec[])
{
    for (int i = 0; i < 100; i++)
    {
        // set each index to a random value of 0 or 1
        vec[i] = rand() % 2;
    }
}

void alter(int oldSolution[], int newSolution[], int currentIndex)
{
    // copy the old array into the new one
    for (int i = 0; i < 100; i++)
    {
        newSolution[i] = oldSolution[i];
    }

    newSolution[currentIndex] = 1 - oldSolution[currentIndex];
}

void array_copy(int copyFrom[], int copyTo[])
{
    for (int i = 0; i < 100; i++)
    {
        copyTo[i] = copyFrom[i];
    }
}