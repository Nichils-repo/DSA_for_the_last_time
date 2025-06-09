def vanity(influencer):
    return influencer.num_bio_links * 5 + influencer.num_selfies

def vanity_sort(influencers):
    return sorted(influencers, key = vanity)


