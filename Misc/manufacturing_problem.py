import sys

item_map = {}


def parseInput():
    target = ''
    item_list = []

    for line in sys.stdin:
        if not target:
            target = line.strip()
            item_list.append(target)
        else:
            temp = line.split(',')
            name = str(temp[0])

            if item_list.count(name) > 0:
                item_list.remove(name)
            else:
                item_list.append(name)

            price = temp[1]
            numInput = int(temp[2])
            inputProducts = temp[3].strip().split(';') if int(numInput) > 0 else None

            if numInput > 0:
                for item in inputProducts:
                    if item_list.count(item) > 0:
                        item_list.remove(item)
                    else:
                        item_list.append(item)

            item_map[name] = (price, inputProducts)

            if len(item_list) == 0:  # no more input
                break

    return target


# Recursive function
def sol(target_product, sum, cost):
    if item_map[target_product][1] is None:
        # Raw material - base case
        return float(item_map[target_product][0])
    else:
        # Not a raw material
        for item in item_map[target_product][1]:
            res = sol(item, sum, cost)  # Recursive call
            if res is not None:
                sum += res

        direct_buy = item_map[target_product][0]

        if direct_buy == 'null':
            cost += sum
        elif float(direct_buy) > sum:
            cost += sum
        else:
            cost += float(direct_buy)

        return cost


def main():
    target = parseInput()
    result = sol(target, 0, 0)
    print(result)


if __name__ == '__main__':
    main()