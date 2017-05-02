def draw_line(tick_len, tick_label=''):
    print('-' * tick_len + ' ' + str(tick_label))

def draw_interval(center_len):
    if center_len > 0:
        draw_interval(center_len - 1)
        draw_line(center_len)
        draw_interval(center_len - 1)

def draw_ruler(num_inches, major_len):
    for i in range(0, num_inches + 1):
        draw_line(major_len, i)
        if i == num_inches:
            break
        draw_interval(major_len - 1)

if __name__ == '__main__':
    draw_ruler(3,3)