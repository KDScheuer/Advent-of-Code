with open('input.txt', 'r') as f:
    seeds, *data = f.read().split('\n\n')
    seeds = list(map(int, seeds.split(':')[1].split()))

    for step in data:
        ranges = []
        for line in step.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new_seed_value = []
        for seed in seeds:
            for dst, src, lng in ranges:
                if seed in range(src, src + lng):
                    new_seed_value.append(seed - src + dst)
                    break
            else:
                new_seed_value.append(seed)

        seeds = new_seed_value

    print(min(seeds))
