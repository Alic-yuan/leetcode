学习笔记

## 面试做题步骤:
    1、和面试官共同把题目搞清楚
    2、想解决方案，并从中找出最优的(time & space)
    3、code
    4、test cases
  
## 二叉树遍历:
    1、前序：根-左-右
    2、中序：左-根-右
    3、后序：左-右-根
  
二叉搜索树，时间复杂度一般为O(log n)<br />

## 二叉堆性质：
    通过完全二叉树来实现
    性质一：完全二叉树
    性质二：树中任意节点的值总是大于子节点的值

## 二叉堆实现细节：
    1、二叉堆一般都通过数组来实现
    2、假设第一个元素在数组中的索引为0的话，则父节点和子节点的位置关系如下：
       （01）索引为i的左孩子的索引是（2*i+1）
       （02）索引为i的右孩子的索引是（2*i+2）
       （03）索引为i的父节点的索引是（i-1）//2 
   
## 大顶堆常见操作：
    find-max  O(1)
    delete-max O(log n)
    insert O(log n) or O(1)
   
## insert 插入操作：
    1、先插入到堆的尾部
    2、依次向上浮动

## delete 删除堆顶操作：
    1、用堆尾的元素替换堆顶
    2、从根部向下浮动
    
二叉堆是堆的一种常见且简单的实现，但是并不是最优的实现。


   

