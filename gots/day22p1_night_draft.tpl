#include "iostream"
//#include "utility"
#include "vector"
#include "sstream"
#include "cassert"
#include "set"//map"
#include "cstdarg"//"initializer_list"
using namespace std;
//using pii = pair<int, int>;
//using ppii = pair<pii, pii>;
using vi = vector<int>;
using vvi = vector<vector<int>>;
void vvvi_printer(vector<vvi>&);
void vi_printer( vi & );
void vvi_printer(vvi & );

int main ()
{
    vector<string> lines;
    string s;
    while (cin >> s) lines.push_back(s);
    vector<vector<vector<int>>> Beams;
    for (string & line: lines)
    {
        cout << line << endl;
        vector<int> temp;
        stringstream ss(line);
        string xyz;
        while (getline(ss, xyz, '~'))
        {
            string symbol;
            stringstream sub(xyz);
            while (getline(sub, symbol, ','))
                temp.push_back(stoi(symbol));
        }
        vi S(temp.begin(), temp.begin() + 3);
        vi E(temp.begin() + 3, temp.end() );
        vvi bricks ;
        if (S[1] == E[1] && S[2] == E[2])
        {
            int len = E[0] - S[0] + 1;
            int i = -1;
            while (++i < len)
                bricks.push_back(vector<int>{S[0] + i, E[1], E[2]});

        }
        else if (S[0] == E[0] && S[2] == E[2])
        {
            int len = E[1] - S[1] + 1;
            int i = -1;
            while (++i < len)
                bricks.push_back(vector<int>{E[0], S[1] + i, E[2]});

        }
        else if (S[0] == E[0] && S[1] == E[1])
        {
            int len = E[2] - S[2] + 1;
            int i = -1;
            while (++i < len)
                bricks.push_back(vector<int>{E[0], E[1], S[2] + i});

        }
        Beams.push_back(bricks);
    }

    // now we got all bricks w/ theirs lengths
    vvvi_printer(Beams);

    set<vector<int>> seen;
    for (vvi & beam : Beams) for (vi& brick: beam) seen.insert(brick);
    // assert(seen.size() == 20);

}

void vvvi_printer(vector<vvi> & VVVI)
{
    for (vvi & block : VVVI) vvi_printer( block );
    cout << "(end print)\n";
}

void vvi_printer(vvi & VVI)
{
    for (vi& line: VVI) vi_printer( line );
    cout << '\n';
}

void vi_printer(vi & VI)
{
    for (int n : VI) cout << n << ' ';
    cout << ":: ";
}

