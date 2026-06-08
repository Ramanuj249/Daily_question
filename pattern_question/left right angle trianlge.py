def print_right_angle_triangle(num):
    for i in range(1,num+1):
        print((num-i+1)*"* ")


print_right_angle_triangle(5)


def print_right_angle_triangle_reverse(num):
    for i in range(1,num+1):
        print(i*"* ")


print_right_angle_triangle_reverse(5)


def print_number_triangle(num):
    for i in range(1,num+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

print_number_triangle(5)

def print_number_triangle_reverse(num):
    for i in range(1,num+1):
        for j in range(1,num+2-i):
            print(j, end=" ")
        print()

print_number_triangle_reverse(5)