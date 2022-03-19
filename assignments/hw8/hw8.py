"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = int(nums[i]) + 10
    return nums

def square_each(nums):
    for i in range(len(nums)):
        if isinstance(nums[i], int) == True:
            nums[i] = int(nums[i]) ** 2
        else:
            nums[i] = float(nums[i]) ** 2
    return nums


def sum_list(nums):
    total = 0
    for i in range(len(nums)):
        if isinstance(nums[i], int) == True:
            total += int(nums[i])
        else:
            total += float(nums[i])
    return total


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])
    return nums

def sum_of_squares(nums):
    sums = []
    for i in range(len(nums)):
        split_nums = nums[i].split(",")
        to_numbers(split_nums)
        square_each(split_nums)
        sums.append(sum_list(split_nums))
    return sums

def starter(weight, wins):
    if (weight >= 150) and (weight < 160) and (wins >= 5):
        return True
    elif (weight > 199 or wins > 20):
        return True
    else:
        return False


def leap_year(year):
    if yr % 400 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    d1, d2 = circle_one.getCenter(), circle_two.getCenter()
    dis = math.sqrt(pow(d1.getX() - d2.getX(), 2) + pow(d1.getY() - d2.getY(), 2))

    if circle_one.getRadius() + circle_two.getRadius() < dis:
        return False
    else:
        return True


if __name__ == '__main__':
    list_nums = [1, 3, 8]
    print(add_ten(list_nums))
    list_nums2 = [1, 3.0, 8]
    print(square_each(list_nums2))
    list_nums3 = [1, 3.0, 8]
    print(sum_list(list_nums3))
    list_nums4 = ["1", "3.0", "8"]
    print(to_numbers(list_nums4))
    list_nums5 = ["3, 5, 7", "3, 7.2, 9"]
    print(sum_of_squares(list_nums5))
    print(starter(150, 5))
    print(starter(200, 5))
    print(starter(199, 5))
    print(leap_year(2000))
    print(leap_year(2100))
    print(leap_year(2400)
    circle_overlap()
