import sys

def construct_tm_dictionary(fname):
    with open(fname) as f:
        content = f.read().splitlines()
    d = {}
    for line in content:
        if line.startswith('%'):
            continue
        s = line.split(',')
        if s[0] not in d:
            d[s[0]] = {}
        d[s[0]][s[2]] = (s[1], s[3], s[4])
    f.close()
    return d

def print_tape(tape, state):
    print(tape[0], state)
    print((' ' * tape[1]) + '^')

def run_TM(tm_dictionary,state,tape,debug):
    
    while True:

        if debug:
            print_tape(tape,state)
            input()
        
        if state == 'h':
            break

        if state not in tm_dictionary:
            break

        
        
        content = tape[0]
        rwheadPosition = tape[1]
        read_symbol =content[rwheadPosition]

        tape[1] = rwheadPosition

        if read_symbol not in tm_dictionary[state]:
            break

        action = tm_dictionary[state][read_symbol]

        state = action[0]

        tape[0] = content[:rwheadPosition] + action[1] + content[rwheadPosition + 1:]

        if action[2] == 'l':
            if rwheadPosition == 0:
                tape[0] = "#" + action[1] + content[1:]
                tape[1] += 1
            else:
                tape[0] = content[:tape[1]] + action[1] + content[tape[1]+1:]
                tape[1] -= 1

        elif action[2] == 'r':
            if rwheadPosition == len(tape[0]) - 1:
                tape[0] = content[:tape[1]] + action[1] + "#"
                tape[1] -= 1
            else:
                tape[0] = content[:tape[1]] + action[1] + content[tape[1]+1:]
                tape[1] += 1

    return state


def main():
    if sys.argv[1] == '-d':
        fname = sys.argv[2]
        content = sys.argv[3]
        debug = True
    else:
        fname = sys.argv[1]
        content = sys.argv[2]
        debug = False
    state = '1'
    tape = [content, 0]
    tm_dictionary = construct_tm_dictionary(fname)
    print('Initial Tape:')
    print_tape(tape, state)

    state = run_TM(tm_dictionary, state, tape, debug)

    print('Final Tape:')
    print_tape(tape,state)

    if state == 'h':
        print('ACCEPT')
    else:
        print('REJECT')



main()
