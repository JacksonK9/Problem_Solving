#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    
    for (int i=0; i<T; i++)
    {
        int a, b;
        cin >> a >> b;
        // cout << a << b << endl;
        a %= 10;
        // cout << a << endl;
        int result = a;
        
        for (int j=1; j<b; j++)
        {
            result *= a;
            result %= 10;
        }
        if (result == 0) {
            cout << 10 << endl;
        }
        else {
            cout << result << endl;
        }
    }
    
    return 0;
}