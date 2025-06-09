def get_estimated_spread(audience_followers):

    # array are my followers and the element is the number of followers each of my followers 
    # has
    num_followers = len(audience_followers)
    if num_followers == 0:
        return 0
    
    sum = 0
    for n in audience_followers:
        sum = sum + n
    avg = sum/num_followers

    spread = avg*(num_followers ** 1.2)

    return spread


