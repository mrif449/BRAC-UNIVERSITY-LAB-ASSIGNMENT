#include "scope_table.h"

class symbol_table
{
private:
    scope_table *current_scope;
    int bucket_count;
    int current_scope_id;

public:
    symbol_table(int bucket_count);
    ~symbol_table();
    void enter_scope();
    void exit_scope();
    bool insert(symbol_info* symbol);
    bool remove(symbol_info* symbol);
    symbol_info* lookup(symbol_info* symbol);
    void print_current_scope(std::ofstream& outlog);
    void print_all_scopes(std::ofstream& outlog);
};

symbol_table::symbol_table(int bucket_count)
    : current_scope(nullptr), bucket_count(bucket_count), current_scope_id(0) {}

symbol_table::~symbol_table()
{
    while (current_scope != nullptr) {
        exit_scope();
    }
}

void symbol_table::enter_scope()
{
    scope_table* new_scope = new scope_table(bucket_count, current_scope_id++, current_scope);
    current_scope = new_scope;
}

void symbol_table::exit_scope()
{
    if (current_scope != nullptr) {
        scope_table* parent_scope = current_scope->get_parent_scope();
        delete current_scope;
        current_scope = parent_scope;
    }
}

bool symbol_table::insert(symbol_info* symbol)
{
    if (current_scope == nullptr) return false; 
    return current_scope->insert_in_scope(symbol);
}

bool symbol_table::remove(symbol_info* symbol)
{
    if (current_scope == nullptr) return false; 
    return current_scope->delete_from_scope(symbol);
}

symbol_info* symbol_table::lookup(symbol_info* symbol)
{
    scope_table* scope = current_scope;
    while (scope != nullptr) {
        symbol_info* found = scope->lookup_in_scope(symbol);
        if (found != nullptr) return found;
        scope = scope->get_parent_scope();
    }
    return nullptr; 
}

void symbol_table::print_current_scope(std::ofstream& outlog)
{
    if (current_scope != nullptr) {
        current_scope->print_scope_table(outlog);
    }
}

void symbol_table::print_all_scopes(std::ofstream& outlog)
{
    outlog << "################################" << std::endl << std::endl;
    scope_table* temp = current_scope;
    while (temp != nullptr)
    {
        temp->print_scope_table(outlog);
        temp = temp->get_parent_scope();
    }
    outlog << "################################" << std::endl << std::endl;
}
