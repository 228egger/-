def parse(tree, has_black = 0):
    if tree.count(',') == 0:
        line = tree.lstrip('(').rstrip(')')
        return int(line[0] == 'w' and has_black)
    else:
        res = 0
        tree = tree[1:-1]
        ans = []
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
        for line in ans:
            if ans[0] == 'b':
                res += parse(line, 1)
            else:
                res += parse(line, has_black)
        return res
                

                
        
        
        





tree = input()
print(parse(tree))