grammar = {
    'S': [['A', 'B']],
    'A': [['a'], ['ε']],
    'B': [['b']]
}

terminals = ['a', 'b']
nonterminals = list(grammar.keys())
start_symbol = 'S'

def compute_first_sets(grammar, terminals):
    first = {nt: set() for nt in grammar}
    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for production in grammar[nt]:
                if production == ['ε']:
                    if 'ε' not in first[nt]:
                        first[nt].add('ε')
                        changed = True
                    continue
                add_epsilon = True
                for symbol in production:
                    if symbol in terminals:
                        if symbol not in first[nt]:
                            first[nt].add(symbol)
                            changed = True
                        add_epsilon = False
                        break
                    elif symbol == 'ε':
                        if 'ε' not in first[nt]:
                            first[nt].add('ε')
                            changed = True
                        add_epsilon = False
                        break
                    else:  # symbol is a nonterminal
                        before = len(first[nt])
                        first[nt].update(first[symbol] - {'ε'})
                        if 'ε' in first[symbol]:
                            add_epsilon = True
                        else:
                            add_epsilon = False
                            break
                        if len(first[nt]) > before:
                            changed = True
                if add_epsilon:
                    if 'ε' not in first[nt]:
                        first[nt].add('ε')
                        changed = True
    return first

def first_of_string(symbols, first, terminals):
    result = set()
    if not symbols:
        return {'ε'}
    add_epsilon = True
    for symbol in symbols:
        if symbol in terminals:
            result.add(symbol)
            add_epsilon = False
            break
        elif symbol == 'ε':
            result.add('ε')
            add_epsilon = True
        else:
            result.update(first[symbol] - {'ε'})
            if 'ε' in first[symbol]:
                add_epsilon = True
            else:
                add_epsilon = False
                break
    if add_epsilon:
        result.add('ε')
    return result

def compute_follow_sets(grammar, first, start_symbol, terminals):
    follow = {nt: set() for nt in grammar}
    follow[start_symbol].add('$')
    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for production in grammar[nt]:
                for i, symbol in enumerate(production):
                    if symbol in grammar:  # nonterminal
                        beta = production[i+1:]
                        beta_first = first_of_string(beta, first, terminals)
                        before = len(follow[symbol])
                        follow[symbol].update(beta_first - {'ε'})
                        if not beta or 'ε' in beta_first:
                            follow[symbol].update(follow[nt])
                        if len(follow[symbol]) > before:
                            changed = True
    return follow

def build_parse_table(grammar, first, follow, terminals):
    parse_table = {nt: {} for nt in grammar}
    for nt in grammar:
        for production in grammar[nt]:
            prod_first = first_of_string(production, first, terminals)
            for terminal in (prod_first - {'ε'}):
                parse_table[nt][terminal] = production
            if 'ε' in prod_first:
                for terminal in follow[nt]:
                    parse_table[nt][terminal] = production
    return parse_table

def parse_input(input_str, parse_table, start_symbol, terminals):
    tokens = input_str.split() + ['$']  # add end marker
    stack = ['$' , start_symbol]   
    print("\nParsing steps:")
    while stack:
        top = stack.pop()       # get top symbol
        current = tokens[0]    
        print("Stack:", stack, "-> Top:", top, "| Next token:", current)
        if top in terminals or top == '$':
            if top == current:
                tokens.pop(0)  
            else:
                print("Error: expected", top, "but found", current)
                return False
        else:  # top is a nonterminal
            if current in parse_table[top]:
                production = parse_table[top][current]
                print("Apply production:", top, "->", " ".join(production))
                if production != ['ε']:
                    for sym in reversed(production):
                        stack.append(sym)
            else:
                print("Error: no rule for", top, "with token", current)
                return False
        if stack == ['$'] and tokens[0] == '$':
            break
    return True

first_sets = compute_first_sets(grammar, terminals)
follow_sets = compute_follow_sets(grammar, first_sets, start_symbol, terminals)
parse_table = build_parse_table(grammar, first_sets, follow_sets, terminals)

test_string = "a b"  
if parse_input(test_string, parse_table, start_symbol, terminals):
    print("\nInput string is valid.")
else:
    print("\nInput string is invalid.")
