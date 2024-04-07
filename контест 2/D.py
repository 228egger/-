def parse(tree):
    if tree.count(',') == 0:
        reverse = 0
        while tree[-1] == "R":
            reverse = (reverse + 1) % 2
            tree = tree[:-1]
        lines = tree.split(',')
        for i in range(len(lines)):
            lines[i] = lines[i].lstrip('(').rstrip(')')
        line = ''.join(lines)
        if reverse:
            return line[::-1]
        return line
    else:
        reverse = 0
        ans = []
        while tree[-1] == "R":
            reverse = (reverse + 1) % 2
            tree = tree[:-1]
        tree = tree[1:-1]
        count = 0
        prev_pos = 0
        for i in range(len(tree)):
            if tree[i] == '(':
                count += 1
            elif tree[i] == ')':
                count -= 1
            if count == 0 and (tree[i] == ','):
                ans.append(tree[prev_pos:i])
                prev_pos = i + 1
        ans.append(tree[prev_pos:])
        if reverse:
            ans = ans[::-1]
        res = ""
        for line in ans:
            if reverse:
                res += parse(line + "R")
            else:
                res += parse(line)
        return res
                

                
        
        
        





tree = input()
print(parse(tree))