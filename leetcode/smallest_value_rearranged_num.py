        if num == 0:
            return 0

        sign = -1 if num < 0 else 1
        digits = sorted(str(abs(num)))

        if sign == -1:
            digits.reverse()
        else:
            if digits[0] == '0':
                zeros = digits.count('0')
                digits = [digits[zeros]] + ['0'] * zeros + digits[zeros+1:]

        return sign * int("".join(digits))