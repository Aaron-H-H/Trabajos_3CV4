//Hernandez Hernandez Aaron
//3CV4
#include <iostream>
#include <fstream>
#include <queue>
#include <map>
#include <bitset>
using namespace std;
 
struct Node {
    char ch;
    int freq;
    Node *left, *right;
    Node(char c, int f) : ch(c), freq(f), left(nullptr), right(nullptr) {}
};
 
struct Compare {
    bool operator()(Node* a, Node* b) { return a->freq > b->freq; }
};
 
void generateCodes(Node* root, string code, map<char, string>& codes) {
    if (!root) return;
    if (!root->left && !root->right) codes[root->ch] = code;
    generateCodes(root->left, code + "0", codes);
    generateCodes(root->right, code + "1", codes);
}
 
Node* buildHuffman(map<char, int>& freq) {
    priority_queue<Node*, vector<Node*>, Compare> pq;
    for (auto& p : freq) pq.push(new Node(p.first, p.second));
    while (pq.size() > 1) {
Node *left = pq.top(); pq.pop();
Node *right = pq.top(); pq.pop();
        Node* parent = new Node('\0', left->freq + right->freq);
        parent->left = left; parent->right = right;
        pq.push(parent);
    }
return pq.top();
}
 
void compress(string inputFile, string outputFile, map<char, string>& codes) {
    ifstream in(inputFile, ios::binary);
    ofstream out(outputFile, ios::binary);
    
    char c;
    string bitStr;
    while (in.get(c)) bitStr += codes[c];
    
    while (bitStr.size() % 8 != 0) bitStr += "0";
    
    for (size_t i = 0; i < bitStr.size(); i += 8) {
        bitset<8> bits(bitStr.substr(i, 8));
        out.put(char(bits.to_ulong()));
    }
}
 
void decompress(string inputFile, string outputFile, Node* root) {
    ifstream in(inputFile, ios::binary);
    ofstream out(outputFile, ios::binary);
    
    Node* current = root;
    char byte;
    while (in.get(byte)) {
        for (int i = 7; i >= 0; i--) {
            bool bit = byte & (1 << i);
            current = bit ? current->right : current->left;
            if (!current->left && !current->right) {
                out.put(current->ch);
                current = root;
            }
        }
    }
}
 
int main() {
    string input = "input.txt";
    string compressed = "codificado.txt";
    string decompressed = "decodificado.txt";
    
    ifstream in(input);
    map<char, int> freq;
    char c;
    while (in.get(c)) freq[c]++;
    in.close();

    Node* root = buildHuffman(freq);
    map<char, string> codes;
    generateCodes(root, "", codes);

    cout << "Códigos Huffman:\n";
    for (auto& p : codes)
        cout << "'" << p.first << "': " << p.second << "\n";

    compress(input, compressed, codes);
    ifstream orig(input, ios::binary | ios::ate);
    ifstream comp(compressed, ios::binary | ios::ate);
    cout << "\nTasa compresión: "
         << 100 - (comp.tellg()*100.0/orig.tellg()) << "%\n";

    decompress(compressed, decompressed, root);
    cout << "Archivo descomprimido en: " << decompressed << endl;
    
    return 0;
}