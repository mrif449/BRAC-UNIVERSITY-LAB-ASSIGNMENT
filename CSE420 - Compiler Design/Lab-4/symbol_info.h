#include<bits/stdc++.h>
using namespace std;

class symbol_info
{
private:
    string name;
    string type;
    string symbol_type; // variable, array, or function
    string return_type; // return type of function or type of variable
    vector<string> parameters; // parameters of a function
    int array_size; // size of array if symbol is an array

public:
    symbol_info(string name, string type, string symbol_type = "variable", string return_type = "", const vector<string>& parameters = {}, int array_size = -1)
    {
        this->name = name;
        this->type = type;
        this->symbol_type = symbol_type;
        this->return_type = return_type;
        this->parameters = parameters;
        this->array_size = array_size;
    }

    string getname()
    {
        return name;
    }

    string gettype()
    {
        return type;
    }

    string get_symbol_type()
    {
        return symbol_type;
    }

    string get_return_type()
    {
        return return_type;
    }

    vector<string> get_parameters()
    {
        return parameters;
    }

    int get_array_size()
    {
        return array_size;
    }

    void set_name(string name)
    {
        this->name = name;
    }

    void set_type(string type)
    {
        this->type = type;
    }

    void set_symbol_type(string symbol_type)
    {
        this->symbol_type = symbol_type;
    }

    void set_return_type(string return_type)
    {
        this->return_type = return_type;
    }

    void set_parameters(const vector<string>& parameters)
    {
        this->parameters = parameters;
    }

    void set_array_size(int array_size)
    {
        this->array_size = array_size;
    }

    ~symbol_info()
    {
        // No deallocation needed here as we don't have dynamic memory allocation.
    }
};
