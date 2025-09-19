class Solution:
    # ------------------------------------------------------
    def plusOne1(self, digits: list[int]) -> list[int]:
        # This method converts the list of digits to an integer,
        # adds one to it, and then converts it back to a list of digits.

        number = 0
        length = 0

        # Convert the list of digits to a number
        for digit in digits:
            number = number * 10 + digit
            length += 1

        length += 1
        result = [0] * length  # Prepare a list to store the result

        # Add 1 to the number
        number += 1

        # Convert the number back to a list of digits
        for i in range(length - 1, -1, -1):
            result[i] = number % 10
            number //= 10

        # If the first element is 0, remove it (this happens when the number has increased in length)
        if result[0] == 0:
            return result[1:]

        return result

    # Time Complexity: O(n), where n is the length of the digits array.
    # - We loop through the digits twice: once to convert to number, and once to extract the digits back.
    # Space Complexity: O(n), because we store the result in an array of length n+1 (or n when we remove the leading 0).
    # ------------------------------------------------------


class Solution:
    def reverse_array(self, array: list[int]) -> None:
        # This helper method reverses the array in-place.

        left = 0
        right = len(array) - 1

        # Swap elements from both ends of the array towards the center
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    def plusOne(self, digits: list[int]) -> list[int]:
        # This method handles addition by reversing the list, adding 1,
        # and then reversing it back.

        self.reverse_array(digits)  # Reverse the digits
        one = 1  # Start with adding 1
        i = 0

        while one:
            # Iterate through the reversed digits and add 1
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0  # Carry over if 9 is found
                    one = 1  # Continue adding 1
                else:
                    digits[i] += 1  # No carry-over, just add 1
                    one = 0  # No further carry-over needed

            else:
                # If the list is exhausted, append 1 to the digits
                digits.append(1)
                one = 0  # Stop the loop

            i += 1

        # Reverse the list back before returning
        self.reverse_array(digits)

        return digits

    # Time Complexity: O(n), where n is the length of the digits array.
    # Space Complexity: O(1), as the algorithm uses constant space (modifying the list in place).
    # ------------------------------------------------------
    def plusOne3(self, digits: list[int]) -> list[int]:
        # This method directly adds one to the number without reversing
        # the array, in-place modifying the digits list.

        n = len(digits)

        # Traverse the digits from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # Add 1 if the digit is less than 9
                return digits

            digits[i] = 0  # Reset the digit to 0 if it's 9 (carry-over)

        # If all digits are 9, prepend 1 to the list
        return [1] + digits

    # Time Complexity: O(n), where n is the length of the digits array.
    # - We iterate through the digits once from the last to the first digit.
    # Space Complexity: O(1), because we modify the digits list in place without using extra space.
