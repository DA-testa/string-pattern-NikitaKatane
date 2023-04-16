import sys
import threading

def read_input():
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    positions = []
    p_len = len(pattern) 
    t_len = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                positions.append(i)
        if i < t_len - p_len:
            t_hash = hash(text[i+1:i+p_len+1])
    return positions

if __name__ == '__main__':
    text_type = input()
    if "F" in text_type:
        filename = "06"
        file_path = f"./tests/{filename}"
        try:
            with open(file_path) as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
        except Exception as e:
            print("Error:", str(e))
            sys.exit()
    elif "I" in text_type:
        pattern, text = read_input()
    
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
