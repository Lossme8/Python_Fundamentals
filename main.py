def most_bought(tomatoes_total, onions_total, beetroot_total, carrots_total, cabbage_total):
    if tomatoes_total >= onions_total and tomatoes_total >= beetroot_total and tomatoes_total >= carrots_total and tomatoes_total >= cabbage_total:
        return tomatoes_total
    elif onions_total >= tomatoes_total and onions_total >= beetroot_total and onions_total >= carrots_total and onions_total >= cabbage_total:
        return onions_total
    elif beetroot_total >= tomatoes_total and beetroot_total >= onions_total and beetroot_total >= carrots_total and beetroot_total >= cabbage_total:
        return beetroot_total
    elif carrots_total >= tomatoes_total and carrots_total >= onions_total and carrots_total >= beetroot_total and carrots_total >= cabbage_total:
        return carrots_total
    else:
        return cabbage_total


def least_bought(tomatoes_total, onions_total, beetroot_total, carrots_total, cabbage_total):
    if tomatoes_total <= onions_total and tomatoes_total <= beetroot_total and tomatoes_total <= carrots_total and tomatoes_total <= cabbage_total:
        return tomatoes_total
    elif onions_total <= tomatoes_total and onions_total <= beetroot_total and onions_total <= carrots_total and onions_total <= cabbage_total:
        return onions_total
    elif beetroot_total <= tomatoes_total and beetroot_total <= onions_total and beetroot_total <= carrots_total and beetroot_total <= cabbage_total:
        return beetroot_total
    elif carrots_total <= tomatoes_total and carrots_total <= onions_total and carrots_total <= beetroot_total and carrots_total <= cabbage_total:
        return carrots_total
    else:
        return cabbage_total


print("\nThe most bought items is: " + str(most_bought(307092, 578034, 792523, 281287, 329373)))
print("\nThe least bought items is: " + str(least_bought(307092, 578034, 792523, 281287, 329373)))
