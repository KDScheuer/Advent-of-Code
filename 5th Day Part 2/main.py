with open('input.txt', 'r') as f:
    all_seeds, *data = f.read().split('\n\n')
    all_seeds = list(map(int, all_seeds.split(':')[1].split()))
    seeds = []

    for index in range(0, len(all_seeds), 2):
        seeds.append((all_seeds[index], all_seeds[index] + all_seeds[index + 1]))

    for step in data:
        ranges = []
        for line in step.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new_seed_value = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for dst, src, lng in ranges:
                overlap_start = max(start, src)
                overlap_end = min(end, src + lng)
                if overlap_start < overlap_end:
                    new_seed_value.append((overlap_start - src + dst, overlap_end - src + dst))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new_seed_value.append((start, end))

        seeds = new_seed_value

    print(min(seeds)[0])
