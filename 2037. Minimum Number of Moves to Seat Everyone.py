class Solution:
    def minMovesToSeat(self, seats, students):
        seats = sorted(seats)
        students = sorted(students)

        counter = 0

        for x in range(len(seats)):
            counter += abs(seats[x]-students[x])

        return counter