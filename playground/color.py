
def find_black(list_of_colors):
    """Find blacks

    Find local minima for a given list of intensities. 
    Intensities are defined as local maxima if the 
    intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.

    Args:
        list_of_intensities (list of floats or ints): a list of
            numeric values

    Returns:
        list of floats: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)
    """
    summed_list =[]
    for el in list_of_colors:
        summed_list.append(sum(el))
    min_value = 0
    list_of_min = []
    for pos, element in enumerate(summed_list):
        if pos == 0:
            continue
        if pos == len(summed_list) - 1:
            continue
        if summed_list[pos - 1] > element < summed_list[pos + 1]:
            min_value = element
            list_of_min.append(list_of_colors[pos])
    return list_of_min
