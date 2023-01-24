'''
没什么,从左到右翻译就好.
'''
class Solution:
    def interpret(self, command: str) -> str:

        ans = []
        i = 0
        while i != len(command):
            if command[i] == 'G':
                ans.append('G')
                i += 1
            elif command[i] == '(':
                if command[i + 1] == ')':
                    ans.append('o')
                    i += 2
                else:
                    ans.append('al')
                    i += 4

        return "".join(ans)

