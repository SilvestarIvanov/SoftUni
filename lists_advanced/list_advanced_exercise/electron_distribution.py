def electron_distribution(num_electrons):
    shells = []
    shell_num = 1

    while num_electrons > 0:
        max_electrons = 2 * shell_num ** 2
        if num_electrons >= max_electrons:
            shells.append(max_electrons)
            num_electrons -= max_electrons
        else:
            shells.append(num_electrons)
            num_electrons = 0
        shell_num += 1

    return shells


num_electrons = int(input())
distribution = electron_distribution(num_electrons)
print(distribution)
