def update_rank(profile):


    if profile.level < 5:

        profile.rank = "Iniciante"


    elif profile.level < 10:

        profile.rank = "Bronze"


    elif profile.level < 25:

        profile.rank = "Prata"


    elif profile.level < 50:

        profile.rank = "Ouro"


    elif profile.level < 75:

        profile.rank = "Platina"


    elif profile.level < 100:

        profile.rank = "Diamante"


    elif profile.level < 150:

        profile.rank = "Mestre"


    else:

        profile.rank = "Lendário"



    profile.save()