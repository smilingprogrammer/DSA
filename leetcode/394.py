class Solution:
    def decodeString(self, s: str) -> str:
        
        number_stack = []
        character_stack = []

        current_num = 0

        current_string = ''

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                number_stack.append(current_num)
                character_stack.append(current_string)
                current_num = 0
                current_string = ''

            elif char == ']':
                prev_string = character_stack.pop()
                repeat_num = number_stack.pop()
                current_string = prev_string + current_string * repeat_num

            else:
                current_string += char

        return current_string