学习笔记

## 字典树
    1、节点本身不存完整单词
    2、从根节点到某一结点，路径上经过的字符连接起来，为该节点对应的字符串
    3、每个节点的所有子节点路径代表的字符都不相同
    
    核心思想：
    Trie树的核心思想是空间换时间
    利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。
    
## 并查集
    适用场景
    1、组团、配对问题
    2、Group or not?
    
## BFS代码模板
    def BFS(graph,start,end):
        visited = set()
        queue = []
        queue.append([start])
        while queue:
            node = queue.pop(0)
            process(node)
            nodes = generate_related_nodes(node)
            for node in nodes:
                if node in visited:
                    continue
                visited.add(node)
                queue.append(node)
        

## AVL总结
    1、平衡二叉搜索树
    2、每个节点存balance factor = {-1,0,1}
    3、四种旋转操作（左旋，右旋，左右旋，右左旋）
    
    不足：节点需要存储额外信息，且调整次数频繁

## 红黑树

    红黑树是一种近似平衡的二叉搜索树，它能够确保任何一个节点的左右子树的高度差小于两倍。
    1、每个节点要么是红色要么是黑色
    2、根节点是黑色
    3、每个叶节点（NIL节点，空节点）是黑色的
    4、不能有相邻接的两个红色节点
    5、从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点。

## AVL和红黑树比较
    1、查找：AVL比红黑树快
    2、插入和删除：红黑树比AVL快
    3、内存：AVL比红黑树要占用大
