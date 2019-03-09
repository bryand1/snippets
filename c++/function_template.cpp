#include <iostream>

template <typename T>
void swap(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

int main()
{
    int i = 10;
    int j = 20;
    swap(i, j);
    std::cout << "compiler generated int swapper:\n";
    std::cout << "i: " << i << " j: " << j << "\n\n";

    double x = 27.1;
    double y = 81.3;
    swap(x, y);
    std::cout << "compiler generated double swapper:\n";
    std::cout << "x: " << x << " y: " << y << "\n\n";

    float u = 0.99;
    float v = 0.38;
    swap(u, v);
    std::cout << "compiler generated float swapper:\n";
    std::cout << "u: " << u << " v: " << v << "\n\n";

    return 0;
}
