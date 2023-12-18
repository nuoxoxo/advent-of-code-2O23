#include "iostream"
#include "vector"
#include "sstream"
using namespace std;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using ll = long long;

void DBG ( vector<string> & );
ll Shoelace (vector<string> &, bool);

int main ()
{
    vector<string> A;
    string s;
    while (cin >> s)
    {
        stringstream ss(s);
        A.push_back(s);
    }

    DBG(A);

    int p1 = Shoelace (A, false);
    cout << "Part 1: " << p1 << endl;

    int p2 = Shoelace (A, true);
    cout << "Part 2: " << p2 << endl;

}

ll Shoelace (vector<string> & A, bool part2 )
{
    ll res = 0;
    return res;
}

void DBG( vector<string> & A) { for ( string & s: A) { cout << s << '\n'; }}
void print(int total,...) {
    va_list args;
    int n, i = total;
    va_start( args, total );
    while (--i > -1) { n = va_arg(args, int); cout << n << ' '; }
    va_end( args );
    cout << '\n';
}

