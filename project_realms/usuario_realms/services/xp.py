def gain_xp(profile, xp):

    profile.xp += xp

    level_up(profile)



def level_up(profile):

    xp_needed = profile.level * 100


    while profile.xp >= xp_needed:

        profile.xp -= xp_needed

        profile.level += 1


        xp_needed = profile.level * 100



    profile.save()