import media
import fresh_tomatoes
toy_story= media.Movie("Toy Story",
                            "A story of a boy and his toys that come to life",
                           " https://static.comicvine.com/uploads/scale_small/0/40/1065087-toy_story_ver1.jpg",
                            "https://www.youtube.com/watch?v=ZZv1vki4ou4")
#print(toy_story.storyline)

znmd=media.Movie("zindagi na milegi dobara",
                        "friends go out on a trip",
                      "http://www.impawards.com/intl/india/2011/posters/zindagi_na_milegi_dobara_ver4_xlg.jpg",
                      "https://www.youtube.com/watch?v=FJrpcDgC3zU")
#print(znmd.storyline)
#znmd.SHOW_TRAILER()

bareilly_ki_barfi=media.Movie("bareilly ki barfi",
                        "story about bitti ,chirag and vidrohi ",
                      "http://torrentmovies.co/wp-content/uploads/2017/08/Bareilly-Ki-Barfi-Torrent-1.jpg",
                      "https://www.youtube.com/watch?v=Ds2JXPKZB6s")
movies=(toy_story,znmd,bareilly_ki_barfi)
fresh_tomatoes.open_movies_page(movies)
#print(moviemedia.Movie.valid_rating)
print(media.Movie.__doc__)
