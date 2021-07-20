from DB import DB


if __name__ =='__main__':
    db = DB()
    univ_list = db.get_all_university()
    univ_abbrev_list = list(map(lambda x:x.univ_abbrev.upper(), univ_list))
    univ_abbrev_list.append("OTEHR")

    print(univ_abbrev_list)

'''
    # Following implement some handy function at first
    # if need some advanced query or operation can direct access db.session to operate
    univ_list=[]
    univ_list.append({
        'univ_abbrev':"NYU",
        'univ_name':"New York University",
        'region':'New York'
    })
    univ_list.append({
        'univ_abbrev':"CMU",
        'univ_name':"Carneige Mellon University",
        'region':'Pittsburgh'
    })
    univ_list.append({
        'univ_abbrev':"UCI",
        'univ_name':"UC Irvine",
        'region':'Irvine'
    })
    # add_universities will read a list of univ dict, univ_abbrev is required
    db.add_universities(univ_list) 

    # Get all allumni in the same university, KEY: if university not created yet, will be error
    alums = db.get_university_alums('CMU')
    for alumni in alums:
        print(alumni.user_id)
    
    # Add new university, May can read from a json file.
    univ_list=[]
    univ_list.append({
        'univ_abbrev':"NYU",
        'univ_name':"New York University",
        'region':'New York'
    })
    univ_list.append({
        'univ_abbrev':"CMU",
        'univ_name':"Carneige Mellon University",
        'region':'Pittsburgh'
    })
    univ_list.append({
        'univ_abbrev':"UCI",
        'univ_name':"UC Irvine",
        'region':'Irvine'
    })
    # add_universities will read a list of univ dict, univ_abbrev is required
    db.add_universities(univ_list) 



    # Add new user, May can read from a json file.
    user = {
        "user_id" : "brian#862236"
    }
    db.add_users(user)

    # Update user info, by find user by user_id,
    user_id = 'brian#862236'
    user_info = {
        'user_name' : "Brian Chen",
        'univ_abbrev' : "CMU",
    }
    db.update_user_by_ID(user_id, user_info)

    # Same operation for update_univ_by_abbrev
    univ_abbrev = 'CMU'
    univ_info = {
        'univ_name' : "Carneigee Mellon University",
    }
    db.update_univ_by_abbrev(univ_abbrev, univ_info)


    # get user object by ID
    user = db.get_user_by_ID('brian#862236')
    # Note should directly access its attributes
    print(user.user_id)
    print(user.user_name)
    print(user.univ_abbrev)
    print(user.user_status)
'''



