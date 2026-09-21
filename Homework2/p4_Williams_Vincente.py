def display_top_collaborations():
    cast = None
    rate = None
    diction = {}
    titles = []
    collaborations = {}
    try:
        cast = open("imdb-top-casts.csv", "r", encoding = 'utf-8')
        rate = open("imdb-top-rated.csv", "r", encoding = 'utf-8')


        for line in cast:
        #splits cast and store movie title, directors and actors in a dictionary
            splitcast = line.split(",")
            title = splitcast[0]
            director = splitcast[2]
            actors = splitcast[3:]
            diction[title] = (director, actors)

        for line in rate:
            splitrate = line.split(",")
            title = splitrate[1]
            titles.append(title)

        for title in titles:
            if title in diction:
                director, actors = diction[title]
                for actor in actors:
                    if actor:
                        key = (director, actor)
                        if key in collaborations:
                            collaborations[key] += 1
                        else:
                            collaborations[key] = 1
        sorted_items = sorted(collaborations.items(),
                              key=lambda kv: kv[1],
                              reverse=True)

        collab_list = [(director, actor, count)
                       for (director, actor), count in sorted_items]
        return collab_list                 
    except FileNotFoundError:
        print("File does not exist.")
        raise

    except Exception:
        print("Unknown error occurred")
        raise

    finally:
        if cast is not None: 
            cast.close()

        if rate is not None: 
            rate.close()

def display_top_actors():
    gross = None
    cast = None
    money_by_actor = {}
    actor_movies = {}   # actor -> set of movie titles (avoids double-counting)
    try:
        gross = open("imdb-top-grossing.csv", "r", encoding='utf-8')
        cast = open("imdb-top-casts.csv", "r", encoding='utf-8')

        next(gross)   # skip header row: "Rank,Title,Year,USA Box Office"

        # Build a mapping: movie title -> box office money
        money_by_title = {}
        for line in gross:
            splitgross = line.strip().split(",")
            title = splitgross[1]              # index 1 = Title
            money = float(splitgross[3])       # index 3 = USA Box Office
            money_by_title[title] = money

        # For each movie in the cast file, add its money to every actor in it
        for line in cast:
            splitcast = line.strip().split(",")
            title = splitcast[0]
            actors = splitcast[3:]

            if title in money_by_title:
                for actor in actors:
                    actor = actor.strip()
                    if actor:
                        if actor not in actor_movies:
                            actor_movies[actor] = set()
                        if title not in actor_movies[actor]:
                            actor_movies[actor].add(title)
                            if actor in money_by_actor:
                                money_by_actor[actor] += money_by_title[title]
                            else:
                                money_by_actor[actor] = money_by_title[title]

        # Sort actors by total money, descending
        sorted_items = sorted(money_by_actor.items(),
                              key=lambda kv: kv[1],
                              reverse=True)

        actor_list = [(actor, total) for actor, total in sorted_items]
        return actor_list

    except FileNotFoundError:
        print("File does not exist.")
        raise
    except Exception:
        print("Unknown error occurred")
        raise
    finally:
        if gross is not None:
            gross.close()
        if cast is not None:
            cast.close()

def main():
    collabs = display_top_collaborations()
    if collabs:
        for i, (director, actor, count) in enumerate(collabs[:10], 1):
            print(f"{i}. {director} & {actor}: {count}")
        actors = display_top_actors()
    if actors:
        for i, (actor, total) in enumerate(actors[:10], 1):
            print(f"{i}. {actor}: ${total:,.2f}")
main()