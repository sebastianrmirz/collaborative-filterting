import math

def pearsons(r, i, j, num_items):
    """ Computes pearsons similarity coefficient

        parameters
        r         -- vector of ratings, where r[i][k] represents the rating user i gave to item k
        i         -- user i
        j         -- user j
        num_items -- number of items
    """

    avg_r_i = sum(r[i])/len(r[i])
    avg_r_j = sum(r[j])/len(r[j])

    i_ratings = [(r[i][k] - avg_r_i) for k in range(num_items)]
    j_ratings = [(r[j][k] - avg_r_j)for k in range(num_items)]

    sim = sum(a * b for a,b in zip(i_ratings, j_ratings))

    i_sqrd = (a*a for a in i_ratings)
    j_sqrd = (b*b for b in j_ratings)

    var = math.sqrt(sum(i_sqrd)) * math.sqrt(sum(j_sqrd))

    return sim / var


