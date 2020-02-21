def sorted_star():
    '''
    import stars' data
    '''
    data = generate_data()

    '''
    sort by distance
    '''
    sorted_list = sorted(data, key = lambda dis: dis[1])
    '''
    extract names and distances from sorted_list
    and store in a table
    '''
    ranked_by_dis = [[ele[0] for ele in sorted_list], [ele[1] for ele in sorted_list]]

    print("Ranked by Distance :")
    for i in range(len(ranked_by_dis[0])):
        print('{}:  {}'.format(ranked_by_dis[0][i], ranked_by_dis[1][i]))
    print

    '''
    sort by apparent brightness
    '''
    sorted_list = sorted([(ele[2], ele[0]) for ele in data])
    '''
    extract names and apparent brightness from sorted_list
    and store in a table
    '''
    ranked_by_app_bri = [[item[1] for item in sorted_list], [item[0] for item in sorted_list]]

    print("Ranked by Apparent Brightness :")
    for i in range(len(ranked_by_app_bri[0])):
        print('{}:  {}'.format(ranked_by_app_bri[0][i], ranked_by_app_bri[1][i]))
    print

    '''
    sort by absolute brightness
    '''
    sorted_list = sorted([(ele[3], ele[0]) for ele in data])
    '''
    extract names and absolute brightness from sorted_list
    and store in a table
    '''
    ranked_by_abs_bri = [[item[1] for item in sorted_list], [item[0] for item in sorted_list]]
    print("Ranked by Absolute Brightness :")
    for i in range(len(ranked_by_abs_bri[0])):
        print('{}:  {}'.format(ranked_by_abs_bri[0][i], ranked_by_abs_bri[1][i]))

def generate_data():
    data = []
    data.append(("Alpha Centauri A", 4.3, 0.26, 1.56))
    data.append(("Alpha Centauri B", 4.3, 0.077, 0.45))
    data.append(("Alpha Centauri C", 4.2, 0.00001, 0.00006))
    data.append(("Barnard's Star", 6.0, 0.00004, 0.0005))
    data.append(("Wolf 359", 7.7, 0.000001, 0.00002))
    data.append(("BD +36 degrees 2147", 8.2, 0.0003, 0.006))
    data.append(("Luyten 726-8 A", 8.4, 0.000003, 0.00006))
    data.append(("Luyten 726-8 B", 8.4, 0.000002, 0.00004))
    data.append(("Sirius A", 8.6, 1.00, 23.6))
    data.append(("Sirius B", 8.6, 0.001, 0.003))
    data.append(("Ross 154", 9.4, 0.00002, 0.0005))
    return data
    
if __name__ == "__main__":
    sorted_star()