import bisect

class BTreeNode:
    def __init__(self, keys, children, is_leaf):
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode([], [], True)
        self.t = t

    def search(self, key):
        return self._search_key(key, self.root)

    def _search_key(self, key, node):
        # 이진 검색으로 하한 인덱스를 얻는다
        # 현재 노드에 키가 존재하면 반환한다
        # 현재 노드에 키가 존재하지 않고 리프 노드라면 False를 반환한다
        # 현재 노드가 리프 노드가 아니라면, child[lower_bound]에 대해 재귀 호출한다
        i = bisect.bisect_left(node.keys, key)
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
        elif node.is_leaf:
            return None
        else:
            return self._search_key(key, node.children[i])

    def insert(self, key):
        # 루트 노드가 꽉 찼다면, 루트 노드를 자식으로 만든다
        # 새로운 루트를 분할하여 자식으로 만든다 -> 새로운 루트는 이전 루트에서 중간 값을 가져온다
        # 루트에서 리프 노드까지 재귀적으로 삽입 루틴을 호출한다
        if len(self.root.keys) == 2 * self.t - 1:  # 루트가 꽉 찼다면
            self.root = BTreeNode([], [self.root], False)
            self._split_child(self.root, 0)
        self._insert_key(key, self.root)

    def _insert_key(self, key, node):
        # 하한 인덱스를 얻는다 -> keys[i] > key
        # 현재 노드가 리프 노드라면, 해당 인덱스에 키를 삽입한다
        # 그렇지 않다면, i번째 자식이 꽉 찼는지 확인한다. 꽉 찼다면, i번째 자식을 분할한다
        # i번째 자식을 분할한 후, 현재 노드의 키에 i번째 자식의 중간 값을 추가한다
        # 값을 확인하고 키에 대한 하한 인덱스를 변경한다
        # i번째 자식에 삽입 루틴을 호출한다
        i = bisect.bisect_left(node.keys, key)
        if node.is_leaf:
            node.keys.insert(i, key)
        else:
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i = i + 1
            self._insert_key(key, node.children[i])

    def _split_child(self, node, i):
        # node에서 i번째 자식을 가져온다
        # 키와 자식을 반으로 나누되, 중간 값은 제외한다
        # 중간 값을 가져와서 node에 삽입한다
        # i번째 자식을 중간 값보다 작은 왼쪽 부분으로 변경한다
        # 중간 값보다 큰 오른쪽 부분을 i + 1번째 인덱스에 삽입한다
        c = node.children[i]
        c_l = BTreeNode(c.keys[0:self.t - 1], c.children[0:self.t], c.is_leaf)
        c_r = BTreeNode(c.keys[self.t:2 * self.t - 1],
                        c.children[self.t:2 * self.t], c.is_leaf)
        median = c.keys[self.t - 1]
        node.keys.insert(i, median)
        node.children[i] = c_l
        node.children.insert(i + 1, c_r)

    def delete(self, key):
        # 루트 키의 개수가 1개이고 모든 자식 노드의 키 개수가 t - 1이라면
        # B-트리는 높이가 h - 1로 줄어들 것이다
        # 따라서 삭제 작업 전에 루트를 전처리해야 한다
        if len(self.root.keys) == 1:
            root = self.root
            t = self.t
            left, right = root.children[0], root.children[1]
            if len(left.keys) == t - 1 and len(right.keys) == t - 1:
                self.root = BTreeNode([], [], False)
                self.root.keys.extend(left.keys)
                self.root.keys.extend(root.keys)
                self.root.keys.extend(right.keys)
                self.root.children.extend(left.children)
                self.root.children.extend(right.children)
                if len(self.root.children) == 0:
                    self.root.is_leaf = True
        self._delete_key(key, self.root)

    def _delete_key(self, key, node):
        i = bisect.bisect_left(node.keys, key)
        # 현재 노드에서 키가 일치하는 경우
        if i < len(node.keys) and node.keys[i] == key:
            if node.is_leaf:
                node.keys.pop(i)
                return
            else:
                successor = self._find_successor(node.children[i + 1])
                node.keys[i], successor.keys[0] = successor.keys[0], node.keys[i]
                self._delete_key(key, node.children[i + 1])
        # 키가 일치하지 않는 경우 다음 노드 상태를 확인한다
        else:
            if len(node.children[i].keys) == self.t - 1:
                self._delete_balancing(node.children[i], node, i)
            i = bisect.bisect_left(node.keys, key)
            self._delete_key(key, node.children[i])

    def _delete_balancing(self, node, parent, i):
        # 다음 목적지 인덱스가 마지막 위치인 경우
        # 다음 목적지는 왼쪽 형제만 있다
        if i == len(parent.children) - 1:
            if len(parent.children[i - 1].keys) > self.t - 1:
                node.keys.insert(0, parent.keys.pop())
                parent.keys.append(parent.children[i - 1].keys.pop())
                if len(parent.children[i - 1].children) > 0:
                    node.children.insert(
                        0, parent.children[i - 1].children.pop())
            else:
                parent.children[i - 1].keys.append(parent.keys.pop())
                parent.children[i - 1].keys.extend(node.keys)
                parent.children.pop()
        # 다음 목적지 인덱스가 첫 번째 위치인 경우
        # 다음 목적지는 오른쪽 형제만 있다
        elif i == 0:
            if len(parent.children[i + 1].keys) > self.t - 1:
                node.keys.append(parent.keys.pop(0))
                parent.keys.insert(0, parent.children[i + 1].keys.pop(0))
                if len(parent.children[i + 1].children) > 0:
                    node.children.append(
                        parent.children[i + 1].children.pop(0))
            else:
                parent.children[i + 1].keys.insert(0, parent.keys.pop(0))
                for k in node.keys:
                    parent.children[i + 1].keys.insert(0, k)
                parent.children.pop(0)
        else:
            if len(parent.children[i - 1].keys) > self.t - 1:
                node.keys.insert(0, parent.keys[i])
                parent.keys[i] = parent.children[i - 1].keys.pop()
                if len(parent.children[i - 1].children) > 0:
                    node.children.insert(
                        0, parent.children[i - 1].children.pop())
            elif len(parent.children[i + 1].keys) > self.t - 1:
                node.keys.append(parent.keys[i])
                parent.keys[i] = parent.children[i + 1].keys.pop(0)
                if len(parent.children[i + 1].children) > 0:
                    node.children.append(
                        parent.children[i + 1].children.pop(0))
            else:
                parent.children[i - 1].keys.append(parent.keys.pop(i - 1))
                parent.children[i - 1].keys.extend(node.keys)
                parent.children.pop(i)

    def _find_successor(self, node):
        if node.is_leaf:
            return node
        else:
            return self._find_successor(node.children[0])

    # 트리를 출력
    def print_tree(self, node, l=0):
        print("Level ", l, " ", end=":")
        for i in node.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(node.children) > 0:
            for i in node.children:
                self.print_tree(i, l)

def main():
    B = BTree(2)

    for i in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
        B.insert(i)

    B.print_tree(B.root)

    if B.search(80) is not None:
        print("\n80 Found")
    else:
        print("\n80 Not found")

    for val in [50, 60]:
        print(f'delete val : {val}')
        B.delete(val)
        print(B.search(val))

if __name__ == '__main__':
    main()
