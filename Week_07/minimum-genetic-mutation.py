class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        changes = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        queue = [(start, 0)]
        visit = set()
        while queue:
            node, count = queue.pop(0)
            if node == end:
                return count
            for n in range(len(node)):
                for i in changes[node[n]]:
                    new_node = node[:n] + i + node[n + 1:]
                    if new_node in visit or new_node not in bank:
                        continue
                    visit.add(new_node)
                    queue.append((new_node, count + 1))
        return -1
        # bank = set(bank)
        # if end not in bank:
        #     return -1

        # dictionary = {"A":"CGT", "C":"AGT", "G":"ACT", "T":"ACG"}
        # front_queue = {start}
        # end_queue = {end}
        # step = 0

        # while front_queue:
        #     step += 1
        #     next_front = set()

        #     for word in front_queue:
        #         for i in range(len(word)):
        #             for c in dictionary.get(word[i]):
        #                 new_word = word[:i] + c + word[i+1:]
        #                 if new_word in end_queue: # 相遇
        #                     return step
        #                 if new_word in bank:
        #                     next_front.add(new_word)
        #                     bank.remove(new_word)

        #     front_queue = next_front

        #     if len(end_queue) < len(front_queue):
        #         front_queue, end_queue = end_queue, front_queue

        # return -1