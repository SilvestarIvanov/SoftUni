def increment_version(current_version):
    version_parts = current_version.split('.')
    version_nums = [int(part) for part in version_parts]
    version_nums[-1] += 1

    for i in range(len(version_nums) - 1, 0, -1):
        if version_nums[i] > 9:
            version_nums[i] = 0
            version_nums[i - 1] += 1

    next_version_parts = [str(num) for num in version_nums]
    next_version = '.'.join(next_version_parts)
    return next_version


current_version = input()
print(increment_version(current_version))

