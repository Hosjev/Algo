// C++ program of the above approach 
// with the addition of the && stops -1, we get correct number of stops but now we don't account for cycles, ie--we GO thru dest city 4 once/then end
// with watching for current city = dest, we stop processing dest edges
// BUT this still doesn't work when there is NO path for k stops that don't exist
//  maybe the above is a sanity check. the ONLY way to do this is track edges
// this takes me BACK to my orig idea. build new adjacency list THEN relax
#include <bits/stdc++.h> 
#include <iostream> 
#include <queue> 
#include <tuple> 
#include <unordered_map> 
  
using namespace std; 
// BSF Memoization 
typedef tuple<int, int, int> tupl; 
  
// Function to implement BFS 
int findCheapestPrice(int cities, vector<vector<int> >& flights, int src, int dst, int stops) { 
    unordered_map<int, vector<pair<int, int> >> adjList; 
  
    // Traverse flight[][] 
    for (auto flight : flights) { 
        // Create Adjacency Matrix 
        adjList[flight[0]].push_back( { flight[1], flight[2] }); 
    } 
  
    // < city, distancefromsource > pair 
    queue<pair<int, int>> q; 
    q.push({ src, 0 }); 
    // Store the Result 
    int srcDist = INT_MAX; 

    // Traversing the Matrix 
    // HOW do we calc steps from current node to edges?
    // maybe the solution is both only caring about while stop -1 AND do NOT process dest edges
    // the way this works (not sexy) is process ONLY what is in Q. which means layer 1 is edges from 
    //  source, (first run), then source edges (2nd run), then 3rd edges, or we end if only 1 stop and
    //  eval layer 1's edges only
    while (!q.empty() && stops-- >= 0) { 
        cout << "Inside Q, stop #: " << stops << "\n";
        int qSize = q.size(); 
        for (int i = 0; i < qSize; i++) { 
            pair<int, int> curr = q.front(); 
            cout << "...processing curr.first: " << curr.first << "\n";
            q.pop(); 
            // Do NOT process destination edges
            if (curr.first == dst) { continue; }
            for (auto next : adjList[curr.first]) { 
                cout << "...processing dest: " << next.first << "\n";
                q.push({ next.first, curr.second + next.second }); 
                if (dst == next.first && stops == -1) { 
                    srcDist = min( srcDist, curr.second + next.second); 
                    cout << "...calc SD: " << srcDist << "\n";
                } 
            } 
        } 
    } 
  
    // Returning the Answer 
    return (srcDist == INT_MAX) ? -1 : srcDist; 
} 
  
// Driver Code 
int main() 
{ 
    // Input flight : {Source, 
    // Destination, Cost} 
    vector<vector<int> > flights 
        = { { 4, 1, 1 },
            { 1, 2, 3 },
            { 0, 3, 2 },
            { 0, 2, 1 },
            { 0, 4, 1 },
            { 3, 1, 1 },
            { 3, 4, 4 },
            { 0, 5, 2 },
            { 5, 2, 3 },
            { 2, 4, 2 },
            { 1, 4, 3 } }; 
  
    // vec, n, stops, src, dst 
    int stops = 4; 
    int totalCities = 6; 
  
    // Given source and destination 
    int sourceCity = 0; 
    int destCity = 4; 
  
    // Function Call 
    long ans = findCheapestPrice( 
        totalCities, flights, 
        sourceCity, destCity, 
        stops); 
    cout << ans << "\n"; 
    return 0; 
} 
