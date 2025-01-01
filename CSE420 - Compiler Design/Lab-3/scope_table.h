#include "symbol_info.h"
#include <vector>
#include <list>
#include <fstream>

class scope_table
{
private:
    int bucket_count;
    int unique_id;
    scope_table *parent_scope = nullptr;
    std::vector<std::list<symbol_info*>> table;

    int hash_function(const std::string& name)
    {
        int sum = 0;
        for (char c : name) {
            sum += static_cast<int>(c);
        }
        return sum % bucket_count;
    }

public:
    scope_table() : bucket_count(0), unique_id(0) {}
    scope_table(int bucket_count, int unique_id, scope_table* parent_scope) 
        : bucket_count(bucket_count), unique_id(unique_id), parent_scope(parent_scope) 
    {
        table.resize(bucket_count);
    }
    scope_table* get_parent_scope() { return parent_scope; }
    int get_unique_id() { return unique_id; }

    symbol_info* lookup_in_scope(symbol_info* symbol)
    {
        int index = hash_function(symbol->get_name());
        for (symbol_info* sym : table[index]) {
            if (sym->get_name() == symbol->get_name()) {
                return sym;
            }
        }
        return nullptr;
    }

    bool insert_in_scope(symbol_info* symbol)
    {
        if (lookup_in_scope(symbol) == nullptr) {
            int index = hash_function(symbol->get_name());
            table[index].push_back(symbol);
            return true;
        }
        return false;
    }

    bool delete_from_scope(symbol_info* symbol)
    {
        int index = hash_function(symbol->get_name());
        for (auto it = table[index].begin(); it != table[index].end(); ++it) {
            if ((*it)->get_name() == symbol->get_name()) {
                table[index].erase(it);
                return true;
            }
        }
        return false;
    }

    void print_scope_table(std::ofstream& outlog)
    {
        outlog << "ScopeTable #" << unique_id << std::endl;
        for (int i = 0; i < bucket_count; ++i) {
            outlog << i << " --> ";
            for (symbol_info* sym : table[i]) {
                outlog << "< " << sym->get_name() << " : " << sym->get_type() << " > ";
            }
            outlog << std::endl;
        }
        outlog << std::endl;
    }

    ~scope_table()
    {
        for (int i = 0; i < bucket_count; ++i) {
            for (symbol_info* sym : table[i]) {
                delete sym;
            }
        }
    }
};
