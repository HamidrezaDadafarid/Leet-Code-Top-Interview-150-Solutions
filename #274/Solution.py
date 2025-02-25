from typing import List


class Solution:

    # First approach: Iterative method
    # Time Complexity: O(n log n) due to sorting.
    # Space Complexity: O(1) extra space, since we sort in place.
    def hIndex1(self, citations: List[int]) -> int:
        # h_index initialized to 0
        h_index = 0

        # Sort citations in reverse order to find the highest h-index
        citations.sort(reverse=True)

        # Iterate through the sorted list and calculate h-index
        for i in range(len(citations)):
            # If citations[i] is greater than the current index, increment h_index
            if citations[i] > i:
                h_index += 1
            else:
                # If a paper with fewer citations than the current index is found, stop
                break

        return h_index

    # Second approach: Brute-force approach
    # Time Complexity: O(n^2) because it checks each possible h-index and counts papers for each h.
    # Space Complexity: O(1) extra space.
    def hIndex2(self, citations: List[int]) -> int:
        h = 0

        # Try all possible h-index values from 0 to len(citations)
        for h in range(len(citations) + 1):
            number_of_papers = 0

            # Count how many papers have at least h citations
            for citation in citations:
                if number_of_papers >= h:
                    break
                if citation >= h:
                    number_of_papers += 1

            # If fewer papers than h, return h-1
            if number_of_papers < h:
                return h - 1

        return h

    # Third approach: Counting sort
    # Time Complexity: O(n) for counting citations and iterating through the papers_count array.
    # Space Complexity: O(n) for the papers_count array.
    def hIndex3(self, citations: List[int]) -> int:
        n = len(citations)

        # Create a list to count papers with each citation count
        papers_count = [0] * (n + 1)

        # Count the number of papers with at least a certain citation number
        for citation in citations:
            if citation >= len(papers_count):
                papers_count[
                    n
                ] += 1  # If citation count exceeds max papers, count in last slot
                continue
            papers_count[citation] += 1

        papers = 0

        # Iterate backwards to find the highest h-index
        for h in range(n, -1, -1):
            papers += papers_count[h]

            # If the total number of papers with at least h citations is greater than or equal to h
            if papers >= h:
                return h
